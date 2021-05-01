import discord
from discord.ext import commands
import json
import requests
import os 
from datetime import datetime
from time import strftime
from datetime import date
d = datetime.now()
print(d.strftime("%d/%m/%y"))


intents = discord.Intents.default()
intents.members = True
guild_subscriptions = True
bot = commands.Bot(command_prefix="!", intents=intents)

token = os.getenv("DISCORD_BOT_TOKEN")



@bot.command()
async def stats(ctx, arg1, arg2):
    plateform = arg1
    nom_du_joueur = arg2
    r = requests.get(url="https://public-api.tracker.gg/v2/apex/standard/profile/"+ plateform + "/" + nom_du_joueur, headers={"TRN-Api-Key":"16e7d718-8c74-4146-be31-8c31cf8ada29"})
    data = r.json()

    if arg1 == "origin":
        embed=discord.Embed(title="**Stats pour** " +arg2+ " **[PC]**", colour=0xff0000)
        embed.add_field(name="**Level:**", value=data['data']['segments'][0]['stats']['level']['displayValue'])
        embed.add_field(name="**Rank:**", value=data['data']['segments'][0]['stats']['rankScore']['metadata']['rankName'])
        embed.add_field(name="**Rank Score:**", value=data['data']['segments'][0]['stats']['rankScore']['value'])
        embed.add_field(name="**Kills:**", value=data['data']['segments'][0]['stats']['kills']['displayValue'])
        embed.add_field(name="Légende actuelle:", value=data['data']['segments'][1]['metadata']['name'])
        embed.set_thumbnail(url=data['data']['segments'][1]['metadata']['imageUrl'])
        embed.set_author(name=arg2, icon_url=data['data']['platformInfo']['avatarUrl'])
        embed.set_image(url=f"{data['data']['segments'][0]['stats']['rankScore']['metadata']['iconUrl']}")
        embed.set_footer(text=d.strftime("%d/%m/%y"), icon_url="https://cdn.discordapp.com/avatars/837916744667627521/2e0ad68b06a29f287b51a9eac5bc99e8.png?size=128")
        embed.add_field(name="Kill avec "+ data['data']['segments'][1]['metadata']['name'], value=arg2+" à fait " + data['data']['segments'][0]['stats']['kills']['displayValue']+ " kills avec " + data['data']['segments'][1]['metadata']['name'])
        embed.add_field(name="Kill avec " + data['data']['segments'][2]['metadata']['name'], value=arg2+" à fait " + data['data']['segments'][0]['stats']['kills']['displayValue'] + ' kills avec '+ data['data']['segments'][2]['metadata']['name'])
        embed.add_field(name="Plus d'info sur :", value="https://apex.tracker.gg/apex/profile/"+ arg1 +"/"+arg2+"/overview", inline=False)

        await ctx.send(embed=embed)

    if arg1 == "psn":
        embed = discord.Embed(title="**Stats pour** " + arg2 + " **[PLAYSTATION]**", colour=0xff0000)
        embed.add_field(name="**Level:**", value=data['data']['segments'][0]['stats']['level']['displayValue'])
        embed.add_field(name="**Rank:**",
                        value=data['data']['segments'][0]['stats']['rankScore']['metadata']['rankName'])
        embed.add_field(name="**Rank Score:**", value=data['data']['segments'][0]['stats']['rankScore']['value'])
        embed.add_field(name="**Kills:**", value=data['data']['segments'][0]['stats']['kills']['displayValue'])
        embed.add_field(name="Légende actuelle:", value=data['data']['segments'][1]['metadata']['name'])
        embed.set_thumbnail(url=data['data']['segments'][1]['metadata']['imageUrl'])
        embed.set_author(name=arg2, icon_url=data['data']['platformInfo']['avatarUrl'])
        embed.set_image(url=f"{data['data']['segments'][0]['stats']['rankScore']['metadata']['iconUrl']}")
        embed.set_footer(text=d.strftime("%d/%m/%y"),
                         icon_url="https://cdn.discordapp.com/avatars/837916744667627521/2e0ad68b06a29f287b51a9eac5bc99e8.png?size=128")
        embed.add_field(name="Kill avec " + data['data']['segments'][1]['metadata']['name'],
                        value=arg2 + " à fait " + data['data']['segments'][0]['stats']['kills'][
                            'displayValue'] + " kills avec " + data['data']['segments'][1]['metadata']['name'])
        embed.add_field(name="Kill avec " + data['data']['segments'][2]['metadata']['name'],
                        value=arg2 + " à fait " + data['data']['segments'][0]['stats']['kills'][
                            'displayValue'] + ' kills avec ' + data['data']['segments'][2]['metadata']['name'])
        embed.add_field(name="Plus d'info sur :",
                        value="https://apex.tracker.gg/apex/profile/" + arg1 + "/" + arg2 + "/overview", inline=False)

        await ctx.send(embed=embed)


    if arg1 == "xbl":
        embed = discord.Embed(title="**Stats pour** " + arg2 + " **[XBOX]**", colour=0xff0000)
        embed.add_field(name="**Level:**", value=data['data']['segments'][0]['stats']['level']['displayValue'])
        embed.add_field(name="**Rank:**",
                        value=data['data']['segments'][0]['stats']['rankScore']['metadata']['rankName'])
        embed.add_field(name="**Rank Score:**", value=data['data']['segments'][0]['stats']['rankScore']['value'])
        embed.add_field(name="**Kills:**", value=data['data']['segments'][0]['stats']['kills']['displayValue'])
        embed.add_field(name="Légende actuelle:", value=data['data']['segments'][1]['metadata']['name'])
        embed.set_thumbnail(url=data['data']['segments'][1]['metadata']['imageUrl'])
        embed.set_author(name=arg2, icon_url=data['data']['platformInfo']['avatarUrl'])
        embed.set_image(url=f"{data['data']['segments'][0]['stats']['rankScore']['metadata']['iconUrl']}")
        embed.set_footer(text=d.strftime("%d/%m/%y"),
                         icon_url="https://cdn.discordapp.com/avatars/837916744667627521/2e0ad68b06a29f287b51a9eac5bc99e8.png?size=128")
        embed.add_field(name="Kill avec " + data['data']['segments'][1]['metadata']['name'],
                        value=arg2 + " à fait " + data['data']['segments'][0]['stats']['kills'][
                            'displayValue'] + " kills avec " + data['data']['segments'][1]['metadata']['name'])
        embed.add_field(name="Kill avec " + data['data']['segments'][2]['metadata']['name'],
                        value=arg2 + " à fait " + data['data']['segments'][0]['stats']['kills'][
                            'displayValue'] + ' kills avec ' + data['data']['segments'][2]['metadata']['name'])
        embed.add_field(name="Plus d'info sur :",
                        value="https://apex.tracker.gg/apex/profile/" + arg1 + "/" + arg2 + "/overview", inline=False)

        await ctx.send(embed=embed)


@stats.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Le joueur que vous essayez de chercher n'a pas été trouver ! Veuillez rentrer !apex plateform(origin pour pc, psn pour playstation, xbl pour xbox) et son identifiant !")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Veuillez rentrer !apex plateform(origin pour pc, psn pour playstation, xbl pour xbox) et son identifiant !")

@bot.command()
async def h(ctx):
    embed = discord.Embed(title="Help", description="Prefix: !", colour=0xff0000)
    embed.add_field(name="stats:", value="Donne le stats d'un joueur !stats origin player, !stats xbl player et !stats psn player")
    embed.add_field(name="support:", value="Donne le serveur discord du support !")
    embed.add_field(name="invite:", value="Donne l'invite du bot !")


    await ctx.send(embed=embed)

@bot.command()
async def support(ctx):
    await ctx.send("Voici le lien discord du support: https://discord.gg/QcK8CWHUg9")

@bot.command()
async def invite(ctx):
    await ctx.send("Voici le lien d'invite du bot: https://discord.com/api/oauth2/authorize?client_id=837916744667627521&permissions=8&scope=bot")

bot.run(token)
