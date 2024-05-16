# Imports 
import discord 
from discord.ext import commands

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Custom Status
@bot.event
async def on_ready():
    print("The bot is now online")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="CUSTOM-STATUS"))

# Command hello
@bot.command()
async def hello(ctx):
    embed = discord.Embed(
        description='Hello {ctx.user}',
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

# Command ip
@bot.command()
async def ip(ctx):
    embed = discord.Embed(
        title='SERVER-NAME',
        description='SERVER-IP',
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

# Command version
@bot.command()
async def version(ctx):
    embed = discord.Embed(
        title='SERVER-NAME',
        description='SERVER-VERSION',
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

# Say System
@bot.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(
        title='Message from ' + str(ctx.author),
        description=message,
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

bot.run("YOUR-BOT-TOKEN")
