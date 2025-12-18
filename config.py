#Coded by the @legend580 💛❤️

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

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1865366440:AAEzQuAZcw5t8F9JdBgSqe5aHMHOGD7eTfg") #testing bot 1 (mj btn)
    #BOT_TOKEN = os.environ.get("BOT_TOKEN", "5872747581:AAHVN_3OP9uffBCKdesYZXFigzVuRYWLYOY") #testing bot 2 (url_v3)
    
    API_ID = int(os.environ.get("API_ID", "3393749"))

    API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

    OWNER_ID = int(os.environ.get("OWNER_ID", "1061576483")) #me legend580
    
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5092726834 5049943931 1827457712 5068888843 7601081539 1187985752 5864451133 1061576483").split())

    AUTH_USERS = list(AUTH_USERS)
    
    AUTH_USERS.append(OWNER_ID)
    
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    #DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://cs:cs@cluster0.ecpmvsv.mongodb.net/?retryWrites=true&w=majority")

    DATABASE_NAME = os.environ.get("DATABASE_NAME", "CS")
    
    LOGGER = logging
    
    #Port
    PORT = os.environ.get("PORT", "8080")
