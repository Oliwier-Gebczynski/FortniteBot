import discord
import requests
import key
import json
import datetime

token = key.TOKEN
api_key = key.API

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
        text = f"{element['item']['name']} - {element['item']['description']}"
        list.append(text)
        list.append(element['item']['rarity'])
        list.append(element['item']['type'])
        list.append(f"Cost: {element['store']['cost']} VB")
        result.append(list)

    return result

def get_player_id(headers, name):
    url = f"https://fortnite-api.theapinetwork.com/users/id?username={name}"

    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text, response

@client.event
async def on_ready():
    print("Online | Welcome! ")

@client.event
async def on_message(message):
    if message.content.startswith('!Hello'):
        await message.channel.send('Hello there!')

    elif message.content.startswith('!help'):
        await message.channel.send("1. Commands: /p_info, /m_history, /store, /challenges. 2. Docs: https://github.com/Oliwier-Gebczynski/SoundCloudBot")

    elif message.content.startswith('!store'):
        message_type = str(message.content).split(" ")
        store = get_store(headers)

        embed = discord.Embed(
            title=f"Shop {datetime.date.today()}",
            description=f"[Check here!](https://fnbr.co/shop)",
            color=discord.Color.purple()
        )

        for item in store:
            embed.add_field(name=item[0], value=item[3], inline=False)

        await message.channel.send(embed=embed)

    elif message.content.startswith('!statistics'):
        name = (message.content).split(' ')[1]
        id = get_player_id(headers, name)

        print(id)

        #await message.channel.send(f"Song {message.content[3:]} added to playlist!")

client.run(token)