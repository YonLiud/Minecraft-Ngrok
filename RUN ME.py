import discord
import mc
from discord.ext import commands
import time
import datetime
bot = commands.Bot(command_prefix='>')
from dotenv import dotenv_values

channel = bot.get_channel(709057578486726720) # <- ID OF CHANNEL GOES HERE

config = dotenv_values(".env")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Ngrok Tunnels"))
    print("Bot Ready")
    await send_data()
    mc.server.wait()
    await stop_server_msg()

async def stop_server_msg():
    time.sleep(2)
    embed = discord.Embed(title=f"Minecraft Server", timestamp=datetime.datetime.utcnow(), color=discord.Color.red(), )
    embed.add_field(name="SERVER CLOSED", value=mc.minecraft_tunnels)
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://img.icons8.com/bubbles/452/minecraft-logo--v1.png")
    await channel.send(embed=embed)
    quit()
    

async def send_data():
    await channel.send("Server has started.\nPlease wait for a tunnel to open!")
    time.sleep(2)
    embed = discord.Embed(title=f"Minecraft Server", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), )
    embed.add_field(name="Ip address: ", value=mc.minecraft_tunnels)
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://img.icons8.com/bubbles/452/minecraft-logo--v1.png")
    embed.set_footer(text="y0nliud#1545", icon_url="https://i.pinimg.com/originals/14/26/57/142657a83da1a1536ff4591bded4743b.gif")
    await channel.send(embed=embed)
    


bot.run(config["TOKEN"])