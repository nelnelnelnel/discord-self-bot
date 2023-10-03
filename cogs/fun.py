from discord.ext import commands
import discord
from gtts import gTTS
import io
import asyncio

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # TTS
    @commands.command(pass_context=True)
    async def tts(self, ctx, *, message: str):
        await ctx.message.delete()
        f = io.BytesIO()
        tts = gTTS(text=message.lower(), lang="en")
        tts.write_to_fp(f)
        f.seek(0)
        buff = f
        await ctx.send(file=discord.File(buff, f"{message}.wav"))

    # L33t encode
    @commands.command(pass_context=True)
    async def encode_leet(self, ctx, *, message: str):
        await ctx.message.delete()
        encoded = message.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')
        await ctx.send(f"{encoded}")

    # Boom
    @commands.command(pass_context=True)
    async def boom(self, ctx):
        await ctx.message.delete()
        message = await ctx.send(""":airplane:          :office::office:""")
        await asyncio.sleep(0.5)
        await message.edit(content=""":airplane:      :office::office:""")
        await asyncio.sleep(0.5)
        await message.edit(content=""":airplane:  :office::office:""")
        await asyncio.sleep(0.5)
        await message.edit(content=""":airplane::office::office:""")
        await asyncio.sleep(0.5)
        await message.edit(content=""":boom: :boom: :boom: """)

def setup(client):
    client.add_cog(Fun(client))