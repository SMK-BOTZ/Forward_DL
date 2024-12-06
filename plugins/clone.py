from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
from config import API_ID, API_HASH, DB_URI, DB_NAME, CLONE_MODE

# MongoDB setup
mongo_client = MongoClient(DB_URI)
mongo_db = mongo_client[DB_NAME]
bot_tokens_collection = mongo_db["bot_tokens"]

@app.on_message(filters.command("clone") & filters.private)
async def clone_bot(client, message: Message):
    if not CLONE_MODE:
        await message.reply_text("Cloning is currently disabled.")
        return

    # Step 1: Request Bot Token
    await message.reply_text(
        "Send me your bot token (obtained from BotFather). Use /cancel to exit."
    )

    bot_token_msg = await app.listen(message.chat.id)
    bot_token = bot_token_msg.text

    if bot_token.lower() == "/cancel":
        await message.reply_text("Cloning process cancelled.")
        return

    # Step 2: Validate Bot Token
    try:
        test_bot = Client("test_bot", bot_token=bot_token)
        await test_bot.start()
        bot_info = await test_bot.get_me()
        await test_bot.stop()

        # Store bot token in MongoDB
        bot_tokens_collection.insert_one({
            "user_id": message.from_user.id,
            "bot_username": bot_info.username,
            "bot_token": bot_token,
        })

        await message.reply_text(
            f"Cloning successful! Your bot @{bot_info.username} is ready."
        )
    except Exception as e:
        await message.reply_text(f"Invalid token or error: {e}")
