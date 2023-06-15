import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
dbs = client.list_database_names()
if "mydb" not in dbs:
    db = client.mydb
    print("Database created")
else:
    print("Database already exists")