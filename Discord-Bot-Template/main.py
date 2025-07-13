import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# Get the Discord Token from the .env file.
# NOTE: This is not tracked for security reasons. Create a .env file to hold the discord token.
# - Load token securely from .env file.
# - Retrieve the bot token from the environment
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Define bot intents: controls what events the bot recieves from Discord.
intents = discord.Intents.default()
intents.message_content = True

### --- This is Example code to verify that the bot is working --- ###
### MyClient class can be removed.
class MyClient(discord.Client):
    # Events: Bot is ready and connected
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # If the message content is "ping", reply with "pong"
        if message.content == 'ping':
            await message.channel.send('pong')

# Creat an instance of the bot client, passing in the specified intents
client = MyClient(intents=intents)

# Run the bot
client.run(token)