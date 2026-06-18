from pymongo import MongoClient
import pandas as pd

class mongo_operations:
    def __init__(self, client_url, database_name):
        self.client = MongoClient(client_url)
        self.db = self.client[database_name]

    def bulk_insert(self, data: pd.DataFrame, collection_name: str):
        collection = self.db[collection_name]
        collection.insert_many(data.to_dict("records"))

    def find(self, collection_name: str):
        collection = self.db[collection_name]
        data = collection.find({}, {"_id": 0})
        return pd.DataFrame(list(data))
