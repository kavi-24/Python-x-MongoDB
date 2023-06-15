import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
dbs = client.list_database_names()
if "mydb" not in dbs:
    db = client.mydb
    print("Database created")
else:
    print("Database already exists")
    db = client.mydb

cols = db.list_collection_names()
if "mycol" not in cols:
    col = db.mycol
    print("Collection created")
else:
    col = db.mycol
    print("Collection already exists")

for doc in col.find():
    print(doc)