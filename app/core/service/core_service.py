""""
API Services
"""
from pymongo import MongoClient
from typing import List

class CoreService():
    
  def init_db(self) -> List[str]:
      CONNECTION_STRING = "mongodb+srv://jclgenavia:root@jcldevmongodb.f8fijeh.mongodb.net/"
      client = MongoClient(CONNECTION_STRING)
        
      database_names = client.list_database_names()

      return database_names  


  def display_value(self, val1: int, val2: int) -> int:

      return val1+val2
        
# if __name__ == "__main__":
#     core_service = CoreService()
