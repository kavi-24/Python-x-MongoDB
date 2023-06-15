import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
col = db["mycol"]

x = col.delete_many({})

print(x.deleted_count, "documents deleted.")