import discord
import requests
import yaml

class DiscordConnector:
    """Custom connector to receive messages from Discord and send to Rasa via REST API."""

    def __init__(self, token, channel_id, rasa_url="http://localhost:5005/webhooks/rest/webhook"):
        self.token = token
        self.channel_id = int(channel_id)
        self.rasa_url = rasa_url
        intents = discord.Intents.default()
        intents.message_content = True
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

            payload = {"sender": str(message.author.id), "message": message.content}
            try:
                response = requests.post(self.rasa_url, json=payload)
                for msg in response.json():
                    if "text" in msg:
                        await message.channel.send(msg["text"])
            except Exception as e:
                print("Error sending message to Rasa:", e)

        client.run(self.token)


if __name__ == "__main__":
    with open("credentials.yml") as f:
        creds = yaml.safe_load(f)

    bot = DiscordConnector(token=creds["discord_token"], channel_id=creds["discord_channel_id"])
    bot.run()
