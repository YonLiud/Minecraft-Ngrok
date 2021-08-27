import discord
import mc
from discord.ext import commands
import time
import datetime
bot = commands.Bot(command_prefix='>')
from dotenv import load_dotenv

config = load_dotenv(".env")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Ngrok Tunnel"))
    print("Bot Ready")
    await send_data()


async def send_data():
    channel = bot.get_channel(709057578486726720)
    await channel.send("Server has started.\nPlease wait for a tunnel to open!")
    time.sleep(2)
    embed = discord.Embed(title=f"Ngrok Tunnel", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), )
    embed.add_field(name="Ip address: ", value=mc.minecraft_tunnels)
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://img.icons8.com/bubbles/452/minecraft-logo--v1.png")
    embed.set_footer(text="y0nliud#1545", icon_url="https://i.pinimg.com/originals/14/26/57/142657a83da1a1536ff4591bded4743b.gif")
    await channel.send(embed=embed)
    


bot.run(config["TOKEN"])