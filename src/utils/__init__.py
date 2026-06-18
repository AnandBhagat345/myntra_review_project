import sys
import os
from src.cloud_io import MongoIO
from src.constants import MONGO_DATABASE_NAME
from src.exception import CustomException





def fetch_product_from_cloud():
    try:
        mongo = MongoIO()
        collection_names = mongo.mongo_ins._mongo_operation_connect_database.list_collection_name()
        return [collection_name.replace('_',' ')
                for collection_name in collection_names]

                
                
    except Exception as e:
        raise CustomException(e,sys)