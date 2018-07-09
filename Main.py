import discord
import safygiphy
import requests
from discord.ext import commands

TOKEN = "NDY0NDU0NjU3MzEwMTk1NzEy.Dh_25Q.cq2Jyk6REUE9Kkq51qoCLxuGgZM"

client = commands.Bot(command_prefix='.')

g = safygiphy.Giphy(token='QeQVWnlDZG7fNtNBtB87kMhaxb2RLNsx')


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


@client.event
async def on_message(message):
    if message.content.startswith('!cringe'):
        author = message.author.name
        embed = discord.Embed(title='CRIIIIINGE!', description=author + ' achou isso cringe!', color=0x00ff00)
        embed.set_image(url="https://i.imgur.com/g62kBxJ.gif")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!gif'):
        gif_tag = message.content[5:]
        randgif = g.random(tag=str(gif_tag))
        resposta = requests.get(
            str(randgif.get('data', {}).get('image_original_url')), stream=True
        )
        await client.send_message('Eis um gif com a tag: ' + gif_tag)
        await client.send_file(message.channel, io.BytesIO(resposta.raw.read()), filename='video.gif')

client.run(TOKEN)
