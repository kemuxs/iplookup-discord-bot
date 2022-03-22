#Ip lookup bot made by kemi
#please don't repost as you're own
import discord
from discord.ext import commands
import requests
import json

prefix = "!" # prefix here
bot = commands.Bot(command_prefix=prefix, help_command=None)
owners = [ur acc id here not token id]
token = 'discord bot token here'
api = "http://ip-api.com/json/" # API used

@bot.event
async def on_ready():
    print("Bot has started!!")
    print("Token used" + token)

def json1(arg):
    response = requests.get(api + arg)
    json_data = json.loads(response.text)
    return(json_data)


@bot.command()
async def ip(ctx, arg):
    json2 = json1(arg)
    isp = json2['isp']
    country = json2['country']
    city = json2['city']
    asn = json2['as']
    embed = discord.Embed(color=0xffffff)
    embed.set_author(name="IP lookup", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Globe_icon_2.svg/800px-Globe_icon_2.svg.png")
    embed.add_field(name="ISP:", value=isp, inline=False)
    embed.add_field(name="country:", value=country, inline=False)
    embed.add_field(name="city:", value=city, inline=False)
    embed.add_field(name="as:", value=asn, inline=False)
    embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0xffffff)
    embed.add_field(name="IP", value="This command will be used like ip 1.1.1.1(This is an example).")
    embed.add_field(name="clear", value="This command will clear the chat the command is typed in!")
    await ctx.send(embed=embed)

@bot.command()
async def clear(ctx):
    if ctx.author.id not in owners:
        embed = discord.Embed(title='Error you do not have owner role', color=0xffffff)
        await ctx.send(embed=embed)

    else:
        if clear:
            await ctx.channel.purge()

bot.run(token)
