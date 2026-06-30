# ==========================================
# Product Sentiment Analyzer Backend
# ==========================================

from flask import Flask
from flask_cors import CORS

from routes import api
from config import DEBUG

app = Flask(__name__)

CORS(app)

app.register_blueprint(api)


@app.route("/")
def home():

    return {

        "status": "success",

        "message": "Product Sentiment Analyzer Backend Running Successfully"

    }


if __name__ == "__main__":

    app.run(debug=DEBUG)