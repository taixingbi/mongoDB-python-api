from pymongo import MongoClient
from bson import ObjectId



class MongoDb:
    def __init__(self):
        print("\nMongoDb...")
        username='kaden';
        password='1234';
        uri = "mongodb://" + username + ":" + password + "@54.87.133.19:27017/ml-test";
        #uri = "mongodb://54.87.133.19:27017/ml-test";
        self.client = MongoClient(uri, 27017)
        #print(client)

    def get(self, name_docoment, name_collection):
        print("\nget...")

        db = self.client[name_docoment] 
        collection = db[name_collection]
        # print(collection)
        
        cursor = collection.find({})
        print('cursor', type(cursor))

        documents=[]
        for document in cursor:
            del document['_id']
            documents.append(document)          
        print(documents) 

        return documents

    def post(self, name_db, name_doc, data):
        db = self.client[name_db] 
        document = db[name_doc]
        print(document)

        result = document.insert_one(data)

    def delete(self, name_db, name_doc, query):
        db = self.client[name_db] 
        document = db[name_doc]
        document.delete_one(query)


if __name__ == "__main__": 
    import time;
    session_id = str(int(time.time()))
    MD= MongoDb()

    data = {
        'name': 'hunter',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott'
    }

    name_db= 'ml-test'
    name_doc= "session_id"


    # MD.post(name_db, name_doc, data)

    # query = { "name": "hunter"}
    # MD.delete(name_db, name_doc, query)

    MD.get(name_db, name_doc)

    print("done")