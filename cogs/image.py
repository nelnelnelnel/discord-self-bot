from discord.ext import commands
import alexflipnote

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.alex_api = alexflipnote.Client()

    # PH logo
    @commands.command(pass_context=True)
    async def ph(self, ctx, message1: str, message2: str):
        await ctx.message.delete()
        url = await self.alex_api.pornhub(message1, message2)
        await ctx.send(f"{url}")

    # Achievement
    @commands.command(pass_context=True)
    async def achivement(self, ctx, *, message: str):
        await ctx.message.delete()
        url = await self.alex_api.achievement(message)
        await ctx.send(f"{url}")

def setup(client):
    client.add_cog(Image(client))