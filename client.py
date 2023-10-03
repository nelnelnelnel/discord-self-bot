# Imports
from discord.ext import commands
import json
from colorama import Fore
from pypresence import Presence
import time

# Load the config
with open("config.json") as file:
    config = json.load(file)

# Global vars
token = config["token"]
prefix = config["prefix"]
rpc_enabled = config["rpc_enabled"]
rpc_details = config["rpc_details"]
rpc_state = config["rpc_state"]

# Init client
client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command("help")
client.load_extension("cogs.fun")
client.load_extension("cogs.image")
client.load_extension("cogs.stats")
client.load_extension("cogs.user")

# Start discord rpc
RPC = Presence("1158759194439200839")
RPC.connect()
if rpc_enabled == True:
    RPC.update(details=rpc_details, state=rpc_state, start=time.time())
else:
    RPC.clear()
    RPC.close()

# Events
@client.event
async def on_command_error(ctx, error):
    error = getattr(error, "original", error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Missing arguments: {error}")

# Ready
@client.event
async def on_ready():
    print(Fore.RED + """
 ▄▄▄██▀▀▀█     █░█    ██  ▄████▄       ██████ ▓█████  ██▓      █████▒▄▄▄▄    ▒█████  ▄▄▄█████▓
   ▒██  ▓█░ █ ░█░██  ▓██▒▒██▀ ▀█     ▒██    ▒ ▓█   ▀ ▓██▒    ▓██   ▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
   ░██  ▒█░ █ ░█▓██  ▒██░▒▓█    ▄    ░ ▓██▄   ▒███   ▒██░    ▒████ ░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▓██▄██▓ ░█░ █ ░█▓▓█  ░██░▒▓▓▄ ▄██▒     ▒   ██▒▒▓█  ▄ ▒██░    ░▓█▒  ░▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
 ▓███▒  ░░██▒██▓▒▒█████▓ ▒ ▓███▀ ░   ▒██████▒▒░▒████▒░██████▒░▒█░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
 ▒▓▒▒░  ░ ▓░▒ ▒ ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
 ▒ ░▒░    ▒ ░ ░ ░░▒░ ░ ░   ░  ▒      ░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░     ▒░▒   ░   ░ ▒ ▒░     ░    
 ░ ░ ░    ░   ░  ░░░ ░ ░ ░           ░  ░  ░     ░     ░ ░    ░ ░    ░    ░ ░ ░ ░ ▒    ░      
 ░   ░      ░      ░     ░ ░               ░     ░  ░    ░  ░        ░          ░ ░           
                         ░                                                ░                   
    """)
    print(Fore.MAGENTA + "Selfbot made by @jwuc")
    print(Fore.BLUE + f"Connected to Discord as @{client.user.name}!")
    print(Fore.YELLOW + f"{client.user.email} | {client.user.id} | {len(client.guilds)} servers | {len(client.user.friends)} friends" + Fore.RESET)

# Start client
client.run(token, bot=False)

# Update rpc
if rpc_enabled == True:
    while True:
        time.sleep(10)