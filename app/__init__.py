from pymongo.errors import ConnectionFailure
from app.utils.env import env


env()
env.loadEnv()

if env.get('ENV', "development") == "development":
    env.loadFromJson('.env/env.json')

from app.utils.Logger import logger
from app.db.DBClient import Client

logger.info("serverStarted", f"env={env.get('ENV', 'development')}")

# Connecting to DB
try:
    client = Client.getClient()
    client.admin.command('ping')
    logger.info("dbConnected")
except ConnectionFailure:
    logger.error("dbConnectionFailed")
    exit(1)
