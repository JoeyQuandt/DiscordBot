import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

class Music(commands.Cog):


    def __init__(self,client):
        self.client=client
    @commands.command()
    async def test(self,ctx):
        await ctx.send('test')
    @commands.command(pass_context=True)
    async def join(self,ctx):
        global voice  
        channel=ctx.message.author.voice.channel
        voice=get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connect():
            await voice.move_to(channel)
        else:
            voice=await channel.connect()

        await ctx.send(f'Joined {channel}')
    @commands.command(pass_context=True)
    async def leave(self,ctx):
        channel=ctx.message.author.voice.channel
        voice=get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f'Left {channel}')
        else:
            await ctx.send('Dont think i am in the voice channel....')
    @commands.command(pass_context=True)
    async def play(self,ctx,url: str):
        song_there=os.path.isfile('song.mp3')
        try:
            if song_there:
                os.remove('song.mp3')
        except PermissionError:
            await ctx.send('Error music is not playing')
            return
        await ctx.send('Getting everything ready now')

        voice=get(self.client.voice_clients, guild=ctx.guild)
        ydl_opts={
            'format':'bestaudio/best',
            'quiet':True,
            'postprocessors':[{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192',
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                name=file
                os.rename(file, 'song.mp3')
        
        voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f'{name} has finished playing'))
        voice.source= discord.PCMVolumeTransformer(voice.source)
        voice.source.volume=0.25

        nname=name.rsplit('-',2)
        await ctx.send(f'Playing: {nname}')
    @commands.command(pass_context=True)
    async def pause(self,ctx):
        voice=get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.pause()
            await ctx.send('Music paused')
        else:
            await ctx.send('There was no music playing...')
    @commands.command(pass_context=True)
    async def resume(self,ctx):
        voice=get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_paused():
            voice.resume()
            await ctx.send('Music is playing again')
        else:
            await ctx.send('There was no music paused...')
    @commands.command(pass_context=True)
    async def stop(self,ctx):
        voice=get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.stop()
            await ctx.send('Music is stopped')
        else:
            await ctx.send('There was no music playing...')


def setup(client):
    client.add_cog(Music(client))