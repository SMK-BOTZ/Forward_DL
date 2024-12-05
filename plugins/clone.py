from pyrogram import Client

# Dictionary to track clone bots by their session names (user bot tokens)
clone_bots = {}

async def urclone(client, message):
    try:
        # Ask the user to provide the bot token for the clone
        await message.reply_text("Please provide the bot token for the cloned bot:", quote=True)

        # Wait for the user's response with the token
        response = await client.listen(message.chat.id)

        # Extract the user-provided bot token
        user_bot_token = response.text.strip()

        # Check if the token is valid
        if not user_bot_token:
            await message.reply_text("❌ You must provide a valid bot token.", quote=True)
            return

        # Create the clone bot using the provided token
        clone_bot = Client(
            f"cloned_bot_{user_bot_token}",  # Session name for the cloned bot (can be dynamic)
            api_id="28243586",  # Main bot's API ID
            api_hash="4022d5686b9b7a7cf8891205921a0ab3",  # Main bot's API Hash
            bot_token=user_bot_token  # User's bot token
        )

        # Add the clone bot to the tracking dictionary
        clone_bots[user_bot_token] = clone_bot

        # Start the clone bot (this will run continuously)
        await message.reply_text(f"✅ Clone Bot Created!\nBot Token: `{user_bot_token}`\nThe bot is now running.", quote=True)
        
        # Run the clone bot continuously
        clone_bot.run()

    except Exception as e:
        await message.reply_text(f"❌ Error occurred while creating the clone: {e}", quote=True)
