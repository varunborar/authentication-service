from pymongo import MongoClient

from app.utils.env import env


class DBClient:

    def __init__(self):
        self.client = None
        if not env.get("MONGODB_HOST"):
            raise ValueError("MONGODB_HOST env variable not set")
        self.MONGODB_HOST = env.get("MONGODB_HOST")

        if not env.get("MONGODB_PORT"):
            raise ValueError("MONGODB_PORT env variable not set")
        self.MONGODB_PORT = int(env.get("MONGODB_PORT"))

        if not env.get("MONGODB_DATABASE"):
            raise ValueError("MONGODB_DATABASE env variable not set")
        self.MONGODB_DATABASE = env.get("MONGODB_DATABASE")

        if env.get("MONGODB_USER"):
            self.MONGODB_USER = env.get("MONGODB_USER")

        if env.get("MONGODB_PASSWORD"):
            self.MONGODB_PASSWORD = env.get("MONGODB_PASSWORD")

    def getClient(self):
        if not self.client:
            if self.MONGODB_USER and self.MONGODB_PASSWORD:
                self.client = MongoClient(self.MONGODB_HOST, self.MONGODB_PORT, username=self.MONGODB_USER, password=self.MONGODB_PASSWORD)
            else:
                self.client = MongoClient(self.MONGODB_HOST, self.MONGODB_PORT)
        return self.client

    def getConnection(self, dbName=None):
        client = self.getClient()
        if not dbName:
            return client[self.MONGODB_DATABASE]
        else:
            return client[dbName]

    def closeConnection(self):
        self.client.close()

    @staticmethod
    def getCollection(connection, collectionName):
        return connection[collectionName]


Client = DBClient()
