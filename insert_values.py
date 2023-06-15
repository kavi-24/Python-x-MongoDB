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
    col = db.mycol

value = {"name": "John", "age": 30, "city": "New York"}
col.insert_one(value)

values = [
    {"name": "Peter", "age": 20, "city": "Washington"},
    {"name": "Amy", "age": 30, "city": "San Francisco"},
    {"name": "Kevin", "age": 25, "city": "Las Vegas"},
]
col.insert_many(values)

values_with_id = [
    {"_id": 1, "name": "Harry", "age": 20, "city": "Washington"},
    {"_id": 2, "name": "Sally", "age": 30, "city": "Sydney"},
    {"_id": 3, "name": "Mary", "age": 25, "city": "Paris"},
]
col.insert_many(values_with_id)

values_with_gender = [
    {"name": "SA", "gender": "M"},
    {"name": "AK", "gender": "F"},
]
col.insert_many(values_with_gender)