# discord_bot.py

import discord
import asyncio
import requests
import yaml

class DiscordConnector:
    """Custom connector to receive messages from Discord and send to Rasa via REST API."""

    def __init__(self, token, channel_id, rasa_url="http://localhost:5005/webhooks/rest/webhook"):
        self.token = token
        self.channel_id = int(channel_id)
        self.rasa_url = rasa_url

        # Enable required intents
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True  # <-- Important! Allows reading message content
        self.client = discord.Client(intents=intents)

    def run(self):
        client = self.client

        @client.event
        async def on_ready():
            print(f"{client.user} has connected to Discord!")

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return
            if message.channel.id != self.channel_id:
                return

            # Send message to Rasa
            payload = {"sender": str(message.author.id), "message": message.content}

            # DEBUG: print the payload before sending
            print("Sending to Rasa:", payload)

            try:
                response = requests.post(self.rasa_url, json=payload)

                # DEBUG: print the raw response from Rasa
                print("Raw response from Rasa:", response.text)

                for msg in response.json():
                    if "text" in msg:
                        await message.channel.send(msg["text"])
            except Exception as e:
                print("Error sending message to Rasa:", e)

        asyncio.run(client.start(self.token))


if __name__ == "__main__":
    # Read token and channel ID from discord_config.yml
    with open("discord_config.yml") as f:
        creds = yaml.safe_load(f)

    # Access the nested 'discord' dictionary
    bot = DiscordConnector(
        token=creds["discord"]["token"],
        channel_id=creds["discord"]["channel_id"]
    )
    bot.run()