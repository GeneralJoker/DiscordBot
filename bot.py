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



whitelist = ('.jpg', '.png', '.bmp', '.jpeg')

@client.listen()
async def on_message(message):
    if not message.attachments:
        return

    if any(a.filename.casefold().endswith(whitelist) for a in message.attachments):
        await message.add_reaction('⬆️')
        await message.add_reaction('⬇️')


@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if payload.emoji.name == "⬇️":
        if message.attachments:
            for react in message.reactions:
                if react.count > 3:
                    await message.delete()


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def breathe(ctx):
    await ctx.send('https://tenor.com/view/spongebob-roast-boy-gif-5259347')

client.run('NjU4NzAwNTQ2NTU0NzI0NDIy.XgeYbQ.Aho0H0n4cR6pvKwXMdKQ9bNMvpU')
