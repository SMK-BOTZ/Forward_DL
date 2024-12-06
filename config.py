# bot developer @mr_jisshu
from os import environ 

    #clone
API_ID = "28243586"  # Get this from https://my.telegram.org
API_HASH = "4022d5686b9b7a7cf8891205921a0ab3"  # Replace with your Telegram API Hash
DB_URI = "mongodb+srv://sahilkaleech:ffmFFKUQXBFDgtxr@cluster0.fn00j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your MongoDB URI
DB_NAME = "Cluster0"  # Replace with your database name
CLONE_MODE = True  # Set to True to enable cloning

class Config:
    
    API_ID = environ.get("API_ID", "28243586")
    API_HASH = environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7242493073:AAFZ2FOAshfsAHiP-dzChR6FqmpZZN7_dWQ") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6551906246').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://smkbotz:Ur3UZGbmzAvq9ig0@cluster0.s2vqa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002056677294'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "vr_unreal") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
