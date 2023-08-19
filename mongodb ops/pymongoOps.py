import pymongo
from pymongo.mongo_client import MongoClient


class db_operations_mongodb:

    __error = 0
    __msg = ''

    try:
        DEFAULT_CONNECTION_URL = "mongodb://localhost:27017"
        client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
        client.server_info()
    except:
        print("connection error")

    def __int__(self, db_name, collection_name):
        self.db_name = db_name
        self.collection_name = collection_name


    def __checkExistence_DB(self, db_name, client):
        """It verifies the existence of DB"""
        DBlist = client.list_database_names()
        if db_name in DBlist:
            print(f"DB: '{db_name}' already exists")
            return True
        print(f"DB: '{db_name}' not yet present OR no collection is present in the DB")
        return False


    def __checkExistence_COL(self, COLLECTION_NAME, db_name, db):
        """It verifies the existence of collection name in a database"""
        collection_list = db.list_collection_names()

        if COLLECTION_NAME in collection_list:
            print(f"Collection:'{COLLECTION_NAME}' in Database:'{db_name}' exists")
            return True

        print(f"Collection:'{COLLECTION_NAME}' in Database:'{db_name}' does not exists OR \n\
        no documents are present in the collection")
        return False


    def create_database(self, db_name, collection_name, record):
        try:
            database = self.client[db_name]
            collection = database[collection_name]

            if type(record) != dict:
                self.__error = 1
                self.__msg = "error! record much be key value pairs"
                return self.__msg
            collection.insert_one(record)
            return "data inserted"

        except Exception as e:
            print(str(e))
            self.__error = 2
            self.__msg = "error while establishing connection"
            return self.__msg


    def __get_collection(self, db_name, collection_name):
        return self.client[db_name][collection_name]


    def delete_record(self, db_name, collection_name, delete_query):
        try:
            collection = self.__get_collection(db_name, collection_name)
            if type(delete_query) != dict:
                self.__error = 3
                self.__msg = "error! delete query much be key value pairs"
                return self.__msg
            collection.delete_one(delete_query)
            return "deleted successfully"
        except Exception as e:
            print(str(e))
            self.__error = 4
            self.__msg = "error while deleting"
            return self.__msg

