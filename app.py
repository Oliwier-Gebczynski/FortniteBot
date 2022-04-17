import discord
import requests
import key
import json

token = key.TOKEN
api_key = key.API
print(api_key)

headers = {
        'Authorization': api_key
}

print("Logging in...")

client = discord.Client()

def get_store(headers):
    url = f"https://fortnite-api.theapinetwork.com/store/get"
    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

@client.event
async def on_ready():
    print("Online | Welcome! ")

@client.event
async def on_message(message):
    if message.content.startswith('/Hello'):
        await message.channel.send('Hello there!')

    elif message.content.startswith('/help'):
        await message.channel.send("1. Commands: /p_info, /m_history, /store, /challenges. 2. Docs: https://github.com/Oliwier-Gebczynski/SoundCloudBot")

    elif message.content.startswith('/store'):
        store = get_store(headers)
        print(store)
        await message.channel.send(store)

    elif message.content.startswith('/p'):
        await message.channel.send(f"Song {message.content[3:]} added to playlist!")




client.run(token)
