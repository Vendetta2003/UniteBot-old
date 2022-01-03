from logging import info
import discord
import asyncio
from workings import  get_card
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound,  MissingRequiredArgument , CommandInvokeError
from time import time


bot = commands.Bot(command_prefix='>>' , help_command = None )

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.idle, activity=discord.Game("Helping Trainers."))
    print("Bot ready!")


@bot.command(name = "info")
async def get_info(ctx ,*,trainer):
    t1 = time()
    await ctx.send("`Searching Unite API....Please wait for 15 seconds :)`")
    embed = discord.Embed(title = "Trainer Info", color = 0xFFC0CB)
    card = get_card(trainer)
    embed.add_field(name = "*Trainer Name* - " , value = f"***{str(card['Name'])}***")
    embed.add_field(name = "*Trainer Code* - " , value = str(card['Code']) , inline = False)
    embed.add_field(name = "*Level* - " , value = str(card['Level']) , inline = True)
    embed.add_field(name = "*Competitive Rank* - " , value = f"**{str(card['Rank'])}**" , inline = True)
    embed.add_field(name = "*Elo* - " , value = f"**{str(card['Elo'])}**" , inline = False)
    embed.add_field(name = "*Fairplay points* - " , value = str(card['Fp-points']) , inline = False)
    embed.add_field(name = "*Total battles* - " , value = str(card['Tb']) , inline = True)
    embed.add_field(name = "*Total Wins* - " , value = str(card['Wins']) , inline = True)
    embed.add_field(name = "*Win rate* - " , value = f"**{str(card['Wr'])}**" , inline = False)
    embed.add_field(name = "*Full info*  - " , value = f"https://uniteapi.dev/{trainer}")
    embed.set_thumbnail(url  = card['img'])
    await ctx.send(embed = embed)
    t2 = time()
    await ctx.send(f"`Time taken to search profile - {str(t2-t1)} seconds`")


@get_info.error
async def nouser(ctx, error):
    if isinstance(error , CommandInvokeError):
        await ctx.send("`User not Found!`")


bot.run(BOT_TOKEN)
