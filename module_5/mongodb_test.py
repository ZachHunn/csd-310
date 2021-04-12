from pymongo import MongoClient

db_url = "mongodb+srv://admin:admin@cluster0.nsmhu.mongodb.net/test"

client = MongoClient(db_url)

db = client.pytech

print(db.list_collection_names())
