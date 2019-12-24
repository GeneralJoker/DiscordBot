import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'Share a bunch of quality memes {member}.')

@client.event
async def on_member_remove(member):
    print(f'{member} is done sharing memes.')


client.run('NjU4NzAwNTQ2NTU0NzI0NDIy.XgDpHw.jKv-mXWIP8fg2S9EveOtiJhw8T0')
