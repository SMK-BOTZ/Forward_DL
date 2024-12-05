from pyrogram import Client, filters

# Replace these with your main bot's API credentials
MAIN_API_ID = "28243586"
MAIN_API_HASH = "4022d5686b9b7a7cf8891205921a0ab3"

# Handle /urclone command
@Client.on_message(filters.private & filters.command(['urclone']))
async def urclone(client, message):
    try:
        # Step 1: Bot sends a message asking for the token
        await message.reply_text(
            "Please provide the bot token that you want to use for the cloned bot.",
            quote=True
        )

        # Wait for the user's response with the bot token
        response = await client.listen(message.chat.id)

        # Step 2: Get the bot token from user input
        user_bot_token = response.text.strip()

        # Step 3: Create a new bot using the provided token and main bot's API credentials
        clone_bot = Client(
            "cloned_bot",  # This is the session name for the cloned bot
            api_id=MAIN_API_ID,  # Main bot's API ID
            api_hash=MAIN_API_HASH,  # Main bot's API Hash
            bot_token=user_bot_token  # User's bot token
        )

        # Step 4: Start the cloned bot (this doesn't run it in the same process, but initiates it)
        await clone_bot.start()

        # Step 5: Send instructions to the user on how to deploy their cloned bot
        clone_instructions = f"""
        ✅ Clone Bot Created!

        Bot Token: `{user_bot_token}`

        **Deployment Steps:**
        1. Download the repository: [GitHub Link to Repo or Source URL]
        2. Place the above token into `config.py` (or wherever the bot token is stored).
        3. Deploy the bot on your platform of choice (Heroku, VPS, etc.).

        Once deployed, the clone bot will function the same as the main bot, with the same features and behavior.
        """
        
        await message.reply_text(clone_instructions, quote=True)

        # Step 6: Stop the cloned bot after it’s initialized
        await clone_bot.stop()

    except Exception as e:
        # Handle any errors that might occur
        await message.reply_text(f"❌ Error occurred while creating the clone: {e}", quote=True)


# Main bot configuration (the bot that handles the /urclone command)
if __name__ == "__main__":
    main_bot = Client(
        "main_bot",  # This is the session name for the main bot
        api_id=MAIN_API_ID,  # Main bot's API ID
        api_hash=MAIN_API_HASH,  # Main bot's API Hash
        bot_token="your_main_bot_token"  # Your main bot token
    )
    
    main_bot.run()  # Start the main bot
