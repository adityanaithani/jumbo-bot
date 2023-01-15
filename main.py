import discord
from discord.ext import commands
import os
import flights

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    channel = bot.get_channel(1063999449204011088)
    await channel.send("NYOOM Jumbo is here!")


# test command
@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)


# display general flight info (flight number, origin, destination, departure time, arrival time)
@bot.command()
async def flight(ctx, arg):
    airport = flights.get_arrival(arg)
    if airport == "Flight not found":
        await ctx.send("Flight not found")
    else:
        await ctx.send(airport)


@bot.command()
async def embed(ctx):

    embed = discord.Embed(
        title="Flight Info",
        description="Information for flight ____",
        color=discord.Color.green(),
    )

    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

    embed.add_field(name="Flight Number", value="____", inline=False)
    embed.add_field(name="Origin", value="____", inline=True)
    embed.add_field(name="Destination", value="____", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=False)
    embed.add_field(name="Departure Time", value="____", inline=True)
    embed.add_field(name="Arrival Time", value="____", inline=True)

    embed.set_footer(text="Made with ❤️ by adi#4917")

    await ctx.send(embed=embed)


# if running on replit, replace token with os.getenv('TOKEN')
bot.run("MTA2MzMxNTIwODk2NzI5MDkxMA.GYwO1b.2q1k_9l5Th8TOP3GFqJE83MPEmQT4L2PEfjimM")
