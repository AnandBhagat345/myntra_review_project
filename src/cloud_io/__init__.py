import os
import sys
import pandas as pd
from src.database_connect.mongo_operation import mongo_operations as mongo
from pymongo import MongoClient
from urllib.parse import quote_plus
from src.constants import MONGODB_URL_KEY, MONGO_DATABASE_NAME
from src.exception import CustomException


class MongoIO:
    """
    MongoDB Input Output Operations
    """

    mongo_ins = None  # class-level singleton instance

    def __init__(self):
        try:
            if MongoIO.mongo_ins is None:
                # Encode username and password for URL safety
                username = "anandbhagat345"
                password = "MilyYoZdlunsiq59"
                mongo_db_url = f"mongodb+srv://{quote_plus(username)}:{quote_plus(password)}@cluster0.3yla3.mongodb.net/?appName=Cluster0"

                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set")

                # Create Mongo operations instance
                MongoIO.mongo_ins = mongo(
                    client_url=mongo_db_url,
                    database_name=MONGO_DATABASE_NAME
                )

            self.mongo_ins = MongoIO.mongo_ins

        except Exception as e:
            raise CustomException(e, sys)

    def store_reviews(self, product_name: str, reviews: pd.DataFrame):
        """
        Store scraped reviews into MongoDB
        """
        try:
            collection_name = product_name.replace(" ", "_")
            self.mongo_ins.bulk_insert(reviews, collection_name)

        except Exception as e:
            raise CustomException(e, sys)

    def get_reviews(self, product_name: str):
        """
        Retrieve reviews from MongoDB
        """
        try:
            collection_name = product_name.replace(" ", "_")
            data = self.mongo_ins.find(collection_name)
            return data

        except Exception as e:
            raise CustomException(e, sys)
