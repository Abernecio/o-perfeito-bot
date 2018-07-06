import discord
import urllib
import json
from discord.ext import commands

TOKEN = "NDY0NDU0NjU3MzEwMTk1NzEy.Dh_25Q.cq2Jyk6REUE9Kkq51qoCLxuGgZM"

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping():
    await client.say('Pong!')


@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


#@client.command()
#async def gif(*args):
#    pesquisa = ''
#    for word in args:
#        pesquisa += word
#        pesquisa += '+'
#    dados = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=" + pesquisa + "&api_key=QeQVWnlDZG7fNtNBtB87kMhaxb2RLNsx&limit=5"))


@client.event
async def on_message(message):
    if message.content.startswith('!cringe'):
        author = message.author.name
        embed = discord.Embed(title='CRIIIIINGE!', description=author + ' achou isso cringe!', color=0x00ff00)
        embed.set_image(url="https://i.imgur.com/g62kBxJ.gif")
        await client.send_message(message.channel, embed=embed)

client.run(TOKEN)
