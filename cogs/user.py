from discord.ext import commands
import discord
from colorama import Fore

class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Export friends list
    @commands.command(pass_context=True)
    async def export_friends(self, ctx):
        await ctx.message.delete()
        with open("./exported/friends.txt", "w") as f:
            for user in self.client.user.friends:
                f.write(f"{user.name}\n")
                print(f"{Fore.LIGHTGREEN_EX}Exported \"{user.name}\"" + Fore.RESET)

    # Export server list
    @commands.command(pass_context=True)
    async def export_servers(self, ctx):
        await ctx.message.delete()
        with open("./exported/servers.txt", "w") as f:
            for server in self.client.guilds:
                f.write(f"{server.name}\n")
                print(f"{Fore.LIGHTGREEN_EX}Exported \"{server.name}\"" + Fore.RESET)

    # Mass dm
    @commands.command(pass_context=True)
    async def mass_dm(self, ctx, *, message: str):
        await ctx.message.delete()
        for user in self.client.user.friends:
            u = await self.client.fetch_user(user.id)
            await u.send(message)
            print(f"{Fore.LIGHTGREEN_EX}Sent message \"{message}\" to {user.name}" + Fore.RESET)

    # Remove friends
    @commands.command(pass_context=True)
    async def remove_friends(self, ctx):
        await ctx.message.delete()
        for user in self.client.user.friends:
            await user.remove_friend()
            print(f"{Fore.LIGHTGREEN_EX}Unadded {user.name}" + Fore.RESET)

    # Leave servers
    @commands.command(pass_context=True)
    async def leave_servers(self, ctx):
        await ctx.message.delete()
        for server in self.client.guilds:
            try:
                await server.leave()
                print(f"{Fore.LIGHTGREEN_EX}Left {server.name}" + Fore.RESET)
            except: 
                print(f"{Fore.RED}Cannot leave {server.name} because you own that server" + Fore.RESET)

    # Stop status
    @commands.command(pass_context=True)
    async def stop_activity(self, ctx):
        await ctx.message.delete()
        await self.client.change_presence(activity=None, status=discord.Status.dnd)
        print(Fore.GREEN + "Stopped your status" + Fore.RESET)

    # Set playing status
    @commands.command(pass_context=True)
    async def playing(self, ctx, *, message: str):
        await ctx.message.delete()
        game = discord.Game(
            name=message
        )
        await self.client.change_presence(activity=game)
        print(Fore.GREEN + f"Changed your playing status to \"{message}\"" + Fore.RESET)

    # Set listening to status
    @commands.command(pass_context=True)
    async def listening_to(self, ctx, *, message: str):
        await ctx.message.delete()
        await self.client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=message,
            )
        )
        print(Fore.GREEN + f"Changed your listening to status to \"{message}\"" + Fore.RESET)

    # Set watching status
    @commands.command(pass_context=True)
    async def watching(self, ctx, *, message: str):
        await ctx.message.delete()
        await self.client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=message,
            )
        )
        print(Fore.GREEN + f"Changed your watching status to \"{message}\"" + Fore.RESET)

def setup(client):
    client.add_cog(User(client))