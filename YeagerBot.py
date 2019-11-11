import discord
import random
import os
import youtube_dl
from discord.ext import commands

client=commands.Bot(command_prefix='!')
client.remove_command('help')

#load,unload files
@client.event
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
@client.event
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


#Bot ready
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Attack on Titan'))
    print("Bot is ready")
#Commands
@client.command()
async def ping(ctx):
    await ctx.send(f'pong!')
#Help command
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help commands", color=discord.Color.red())
    embed.add_field(name="!help",value="gives a summary of all commands of this bot",inline=False)
    embed.add_field(name="!ping",value="returns an pong!", inline=False)
    embed.add_field(name="!question",value="the bot answers your question", inline=False)
    embed.add_field(name="!coinflip", value="the bot plays coinflip with you", inline=False)
    embed.add_field(name="!clear", value="clears the chat for you, if no input is given it clears five", inline=False)
    embed.add_field(name="!join", value="The bot will join youre channel and can play music", inline=False)
    embed.add_field(name="!play", value="The bot will play an song for you if you provide an url", inline=False)
    embed.add_field(name="!pause", value="The bot will pause the song for you", inline=False)
    embed.add_field(name="!stop", value="The bot will stop the song for you", inline=False)
    embed.add_field(name="!leave", value="The bot will youre voice channel", inline=False)

    await ctx.send(embed=embed)
#!Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You have not typed anything....')

#list of cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NjM5Nzg1Mzk2Mzc2NTY3ODA4.XclL0w.6wjcR3kuINqe1WY065pPqvP6DXQ')
