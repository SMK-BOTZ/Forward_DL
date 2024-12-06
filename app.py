
from pyrogram import Client

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from jisshu'


if __name__ == "__main__":
    app.run()
