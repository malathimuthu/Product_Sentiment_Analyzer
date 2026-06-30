# ==========================================
# Review Model
# ==========================================

from datetime import datetime


class Review:

    def __init__(
        self,
        product,
        review,
        rating,
        sentiment,
        created_at=None,
        updated_at=None
    ):

        self.product = product
        self.review = review
        self.rating = rating
        self.sentiment = sentiment
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def to_dict(self):

        return {
            "product": self.product,
            "review": self.review,
            "rating": self.rating,
            "sentiment": self.sentiment,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __str__(self):

        return f"{self.product} - {self.sentiment}"