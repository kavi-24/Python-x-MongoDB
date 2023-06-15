import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
dbs = client.list_database_names()
if "mydb" not in dbs:
    db = client.mydb # create db if not exist
    print("Database created")
else:
    print("Database already exists")
    db = client.mydb

cols = db.list_collection_names()
if "mycol" not in cols:
    col = db.mycol # create col if not exist
    print("Collection created")
else:
    print("Collection already exists")