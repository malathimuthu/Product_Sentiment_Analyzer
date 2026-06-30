# ==========================================
# API Routes
# ==========================================

from flask import Blueprint, jsonify, request
from bson import ObjectId
from datetime import datetime

from database import reviews_collection
from sentiment import analyze_sentiment
from utils import save_csv

api = Blueprint("api", __name__)


# ==========================================
# Home
# ==========================================

@api.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Product Sentiment Analyzer API Running"
    })


# ==========================================
# Get All Reviews
# ==========================================

@api.route("/reviews", methods=["GET"])
def get_reviews():

    reviews = []

    try:

        product = request.args.get("product")
        sentiment = request.args.get("sentiment")

        query = {}

        if product:
            query["product"] = {
                "$regex": product,
                "$options": "i"
            }

        if sentiment:
            query["sentiment"] = sentiment

        for item in reviews_collection.find(query):

            item["_id"] = str(item["_id"])

            reviews.append(item)

        return jsonify(reviews)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# Add Review
# ==========================================

@api.route("/reviews", methods=["POST"])
def add_review():

    try:

        data = request.get_json()

        product = data.get("product")
        review = data.get("review")
        rating = data.get("rating", 0)

        if not product or not review:

            return jsonify({
                "error": "Product and Review are required."
            }), 400

        sentiment, polarity, compound = analyze_sentiment(review)

        review_data = {

            "product": product,
            "review": review,
            "rating": rating,
            "sentiment": sentiment,
            "polarity": polarity,
            "compound_score": compound,
            "created_at": datetime.now()

        }

        reviews_collection.insert_one(review_data)
        reviews = list(reviews_collection.find({}, {"_id": 0}))
        save_csv(reviews)

        return jsonify({

            "message": "Review Added Successfully",
            "sentiment": sentiment

        })

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# ==========================================
# Update Review
# ==========================================

@api.route("/reviews/<review_id>", methods=["PUT"])
def update_review(review_id):

    try:

        data = request.get_json()

        review = data.get("review")

        sentiment, polarity, compound = analyze_sentiment(review)

        reviews_collection.update_one(

            {"_id": ObjectId(review_id)},

            {
                "$set": {

                    "review": review,
                    "rating": data.get("rating"),
                    "sentiment": sentiment,
                    "polarity": polarity,
                    "compound_score": compound,
                    "updated_at": datetime.now()

                }

            }

        )

        return jsonify({
            "message": "Review Updated Successfully"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# Delete Review
# ==========================================

@api.route("/reviews/<review_id>", methods=["DELETE"])
def delete_review(review_id):

    try:

        reviews_collection.delete_one({
            "_id": ObjectId(review_id)
        })

        return jsonify({
            "message": "Review Deleted Successfully"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# Export CSV
# ==========================================

@api.route("/export", methods=["GET"])
def export_csv():

    try:

        reviews = list(reviews_collection.find({}, {"_id": 0}))

        save_csv(reviews)

        return jsonify({
            "message": "CSV Exported Successfully"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# Statistics
# ==========================================

@api.route("/statistics", methods=["GET"])
def statistics():

    try:

        positive = reviews_collection.count_documents({
            "sentiment": "Positive"
        })

        negative = reviews_collection.count_documents({
            "sentiment": "Negative"
        })

        neutral = reviews_collection.count_documents({
            "sentiment": "Neutral"
        })

        return jsonify({

            "positive": positive,
            "negative": negative,
            "neutral": neutral,
            "total": positive + negative + neutral

        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500