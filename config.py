# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "28243586")
    API_HASH = environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7242493073:AAFZ2FOAshfsAHiP-dzChR6FqmpZZN7_dWQ") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6551906246').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    # Get this from https://my.telegram.org
    DB_URI = "mongodb+srv://madarazbotz:Squ7qrKySvxFVpuD@cluster0.cjp2q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # MongoDB connection URI
    DB_NAME = "cluster0"          # Database name
    CLONE_MODE = True                       
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://smkbotz:Ur3UZGbmzAvq9ig0@cluster0.s2vqa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
