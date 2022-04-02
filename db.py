from pymongo import MongoClient

def get_db():
    client = MongoClient(host='dbmongo',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")

    db = client["pymongodb"]

    return db

