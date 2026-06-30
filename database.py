from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

# Always create the variable
reviews_collection = None

try:
    client = MongoClient(MONGO_URI)

    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully")

    db = client[DATABASE_NAME]
    reviews_collection = db[COLLECTION_NAME]

except Exception as e:
    print("❌ MongoDB Connection Failed")
    print("ERROR:", e)