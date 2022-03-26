import discord

token = ""
print("Logging in...")

client = discord.Client()

songList = []

@client.event
async def on_ready():
    print("Online | Welcome! ")

@client.event
async def on_message(message):
    if message.content.startswith('/Hello Cloudy'):
        await message.channel.send('Hello there!')

    elif message.content.startswith('/help'):
        await message.channel.send('1. If you want add song try this "/p linkFromSoundCloud" . 2. Docs: https://github.com/Oliwier-Gebczynski/SoundCloudBot')

    elif message.content.startswith('/playlist'):
        await message.channel.send(songList)

    elif message.content.startswith('/p'):
        songList.append(message.content[3:])
        await message.channel.send(f"Song {message.content[3:]} added to playlist!")
        print(songList)

client.run(token)
