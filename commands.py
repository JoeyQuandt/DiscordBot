import discord
import random
from discord.ext import commands

class Commands(commands.Cog):


    def __init__(self, client):
        self.client=client
    @commands.command()
    async def coinflip(self,ctx,*antwoord):
        side=random.randint(1,2)
        if antwoord=="head" and side==1:
            await ctx.send(f'You have won!\n The answer was head')
        elif antwoord=="tail" and side==2:
            await ctx.send(f'You have won!\n The answer was tail')
        else:
            await ctx.send(f'You have lost!')
    @commands.command()
    async def question(self,ctx,*,question):
        answers=["It is certain",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')
    @commands.command()
    async def clear(self,ctx,amount=5):
        await ctx.channel.purge(limit=amount)
        

    

def setup(client):
    client.add_cog(Commands(client))