from pymongo import MongoClient

def conexao():
    try:
        client = MongoClient("mongodb-service", 27017)
        db = client.spyface
        return db
    except Exception as e:
        print(e)