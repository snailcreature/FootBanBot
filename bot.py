import discord
from dotenv import load_dotenv
import os
from random import choice

responses = ["No f-word!", "We talked about this, come on...", "Stop.", "None of that.", "We don't serve your kind here..."]
nonos = ["football", "footy", "foot ball"]
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    for word in nonos:
        if word in message.content.lower():
            await message.reply("%s :angry:" % str(choice(responses)))

client.run(os.getenv("TOKEN"))
