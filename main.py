from decouple import config
import discord
from discord.ext import commands
import os
import flights


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


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
    # origin airport
    origin = flights.get_departure(arg)
    # destination airport
    destination = flights.get_arrival(arg)
    # departure time
    departure_time = flights.get_departure_time(arg)
    # arrival time
    arrival_time = flights.get_arrival_time(arg)
    # departure gate
    # arrival gate

    embed = discord.Embed(
        title="General Flight Data",
        description="Flight " + arg + "  to " + destination,
        color=discord.Color.green(),
    )

    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)

    embed.add_field(name="Origin", value=origin, inline=False)
    embed.add_field(name="Destination", value=destination, inline=False)
    embed.add_field(name="Departure Time", value=departure_time, inline=False)
    embed.add_field(name="Arrival Time", value=arrival_time, inline=True)

    embed.set_footer(text="Made with ❤️ by adi#4917")

    await ctx.send(embed=embed)


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


bot.run(config("TOKEN"))
