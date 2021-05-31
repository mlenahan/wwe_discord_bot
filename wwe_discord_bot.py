import os
import discord
import random
from dotenv import load_dotenv
from discord.ext.commands import Bot
import embededlinks

bot = Bot(command_prefix='!')


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def wwe(ctx):
    chosen_image = random.choice(embededlinks.wrestler_links)
    embed = discord.Embed(color=0xff69b4)
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Requested by: {ctx.author.name}")
    await ctx.send(embed=embed)


bot.run(TOKEN)