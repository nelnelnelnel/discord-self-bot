from discord.ext import commands
import discord
import requests
import json

class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Help
    @commands.command(pass_context=True)
    async def help(self, ctx):
        await ctx.message.delete()
        await ctx.send("""# :scroll: Commands 
# <> = required | [] = optional
### Fun
tts <message> - Sends your message with Google TTS
encode_leet <message> - Encode your message to l33t speak
boom - 9/11
### Image
ph <message1, message2> - Generates a PornHub logo with your text
achivement <message> - Generates a Minecraft achivement with your text
### Stats
help - This command
info - Information about the self bot
ping - Gets the ping for the self bot
get_user <@user> - Gets the users information in a server
token_info <token> - Get the information about a Discord token
### User
export_friends - Saves your friends list to a txt file
export_servers - Saves your server list to a txt file
leave_servers - Leaves all the servers you are in
mass_dm - Sends a message to all of your friends
remove_friends - Unadds all of your friends
playing <message> - Sets your playing status to the message
listening_to <message> - Sets your listeningto status to the message
watching <message> - Sets your watching status to the message
stop_activity - Stops all custom statuses""")

    # Info
    @commands.command(pass_context=True)
    async def info(self, ctx):
        await ctx.message.delete()
        await ctx.send(
            f"""# :information_source: xohw selfbot info
### Servers
{len(self.client.guilds)}
### Friends
{len(self.client.user.friends)}
### Developer
xohw
### Language
Python
### Made for fun! ❤""")

    # Ping
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.message.delete()
        await ctx.send(
            f"""# 🏓 Pong!
{round(self.client.latency * 1000 / 1000)}ms""")

    # Get user
    @commands.command(pass_context=True)
    async def get_user(self, ctx, *, member: discord.Member = None):
        await ctx.message.delete()
        if not (member):
            await ctx.send("Invalid member")
            return
        
        if (member.bot):
            bot = "✔️"
        else:
            bot = "❌"

        avatar = member.avatar
        if avatar == None:
            avatar = "N/A"
        else:
            avatar = f"https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.webp?size=4096"
        
        await ctx.send(f"""# :information_source: {member.display_name}
### ID
{member.id}
### Is a bot
{bot}
### Created at
{member.created_at.strftime("%d/%m/%Y")}
### Joined at
{member.joined_at.strftime("%d/%m/%Y")}
### Voice state
{member.voice.channel if member.voice else "None"}
### Roles
{len(member.roles)}
### Avatar url
{avatar}""")
        
    # Token info
    @commands.command(pass_context=True)
    async def token_info(self, ctx, *, token: str):
        await ctx.message.delete()
        response = requests.get("https://discord.com/api/users/@me", headers={"Content-Type": "application/json", "Authorization": token})
        user = json.loads(response.text)
        await ctx.send(f"""# :information_source: {token}
### ID
{user["id"]}
### Global username
{user["global_name"]}
### Username
{user["username"]}
### Verified
{user["verified"]}
### Email
{user["email"]}
### Phone number
{user["phone"]}
### 2FA enabled
{user["mfa_enabled"]}
### Locale
{user["locale"]}
### Premium type
{user["premium_type"]}
### Purchased premium
{user["purchased_flags"]} times
### Bio
{user["bio"]}""")

def setup(client):
    client.add_cog(Stats(client))