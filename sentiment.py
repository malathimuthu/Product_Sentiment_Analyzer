# ==========================================
# Sentiment Analysis
# ==========================================

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER Analyzer
analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    """
    Analyze sentiment using TextBlob and VADER.
    Returns:
        sentiment, polarity, compound_score
    """

    if not text:
        return "Neutral", 0.0, 0.0

    # ---------- TextBlob ----------
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # ---------- VADER ----------
    vader_score = analyzer.polarity_scores(text)
    compound = vader_score["compound"]

    # Final Decision
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, round(polarity, 2), compound