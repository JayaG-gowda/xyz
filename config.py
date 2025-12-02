#Coded by KA18 the @legend580 💛❤️

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class tuple_(object):
    def __init__(self):
        return

class Config(object):

    #BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5869954207:AAG2sJbYvKujDQd2GFoiQxF0T5L41hdvNME") #testing bot 1 (mj btn)
    #BOT_TOKEN = os.environ.get("BOT_TOKEN", "5872747581:AAHVN_3OP9uffBCKdesYZXFigzVuRYWLYOY") #testing bot 2 (url_v3)
    
    API_ID = int(os.environ.get("API_ID", "3393749"))

    API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

    OWNER_ID = int(os.environ.get("OWNER_ID", "1061576483")) #me legend580
    
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    AUTH_USERS = list(AUTH_USERS)
    
    AUTH_USERS.append(OWNER_ID)
    
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    #DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Jaya:Jaya@cluster0.4ot2upm.mongodb.net/?appName=Cluster0")

    DATABASE_NAME = os.environ.get("DATABASE_NAME", "CS")
    
    LOGGER = logging
    
    #Port
    PORT = os.environ.get("PORT", "8080")
