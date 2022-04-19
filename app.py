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
    result = []

    response = requests.request("GET", url, headers=headers, data=payload).json()
    elements = response['data']

    for element in elements:
        list = []
        text = f"{element['item']['name']} - {element['item']['description']} (Price: {element['store']['cost']} VB)"
        list.append(text)
        list.append(element['item']['rarity'])
        list.append(element['item']['type'])
        result.append(list)

    return result

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
        store_result = []
        message_type = str(message.content).split(" ")
        type = message_type[1]

        store = get_store(headers)

        for item in store:
            if item[2] == type:
                store_result.append(item)

        await message.channel.send(store_result)

    elif message.content.startswith('/p'):
        await message.channel.send(f"Song {message.content[3:]} added to playlist!")


client.run(token)
