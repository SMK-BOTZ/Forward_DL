from pyrogram import Client
import asyncio

async def urclone(client, message):
    try:
        # Send instructions to the user to provide a bot token
        await message.reply_text("Please provide the bot token for the cloned bot:", quote=True)

        # Wait for the user's response (the token for the clone bot)
        response = await client.listen(message.chat.id)

        # Get the user-provided bot token
        user_bot_token = response.text.strip()

        # Ensure the bot token is valid
        if not user_bot_token:
            await message.reply_text("❌ You must provide a valid bot token.", quote=True)
            return

        # Create the clone bot client using the user's token
        clone_bot = Client(
            "cloned_bot",  # The session name can be dynamic if needed
            api_id="28243586",  # Your main bot's API ID
            api_hash="4022d5686b9b7a7cf8891205921a0ab3",  # Your main bot's API Hash
            bot_token=user_bot_token  # The user's bot token
        )

        # Start the clone bot
        await clone_bot.start()

        # Send instructions to the user
        clone_instructions = f"""
        ✅ Clone Bot Created!

        Bot Token: `{user_bot_token}`

        **Deployment Steps (optional)**:
        1. Download the repository: [GitHub Link to Repo or Source URL]
        2. Place the above token into `config.py` (or wherever the bot token is stored).
        3. Deploy the bot on your platform of choice (Heroku, VPS, etc.), if required.

        The bot is already started and running via the main bot!
        """
        await message.reply_text(clone_instructions, quote=True)

        # Wait until the clone bot is stopped (in this case, we stop it after the task is done)
        await clone_bot.stop()

    except Exception as e:
        await message.reply_text(f"❌ Error occurred while creating the clone: {e}", quote=True)
