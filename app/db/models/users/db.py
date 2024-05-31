from pymongo import MongoClient

from app.db.models.users.user import User
from app.utils.env import env
from app.db.DBClient import Client


class UserDB:

    def __init__(self):
        self.MONGODB_USER_COLLECTION_NAME = env.get("MONGODB_USER_COLLECTION_NAME", "users")
        self.db = Client.getConnection()
        self.collection = self.db[self.MONGODB_USER_COLLECTION_NAME]

    def createUser(self, user: User):
        try:
            data = user.getUser()
            self.collection.insert_one(data)
            return True
        except Exception as e:
            return False
