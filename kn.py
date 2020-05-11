botversion = '1.2.6od rev AKO'
print("___________________________________________________")
print("""
            _  __                    _  
           | |/ /__ _ _ _  _ _  __ _| | 
           | ' </ _` | ' \| ' \/ _` |_| 
           |_|\_\__,_|_||_|_||_\__,_(_) 
""")
print("             The Kawaii Discord bot !           ")
print("                                                   ")
print("                      "+botversion+"                      ")
print("                                                   ")
print("___________________________________________________")
print()
import time
from time import *
print(('[' + ctime()) + "] Lib 'time' successfully imported !")
import os
print(('[' + ctime()) + "] Lib 'os' successfully imported !")
import datetime
from datetime import *
print(('[' + ctime()) + "] Lib 'datetime' successfully imported !")
import random
from random import *
print(('[' + ctime()) + "] Lib 'random' successfully imported !")
import sys
from sys import exit, version
print(('[' + ctime()) + "] Lib 'sys' [exit, version] successfully imported !")
import asyncio
from asyncio import *
print(('[' + ctime()) + "] Lib 'asyncio' [exit, version] successfully imported !")
import discord
from discord.ext import commands
print(('[' + ctime()) + "] Lib 'discord' successfully imported !")
print(('[' + ctime()) + '] Establishing connection with the bot...')
bot = commands.Bot(description='Kanna - The Kawaii Discord bot - Server management bot ©2018 Poulpe#2356', command_prefix=':3')
bot.remove_command('help')

async def status_task():
    while True:
        names = [':3help', 'taquiner Soja', 'caresser Soja', f'vec {len(bot.users)} personnes']
        for name in names:
            await bot.change_presence(activity=discord.Game(name=name))
            await asyncio.sleep(60*60)

@bot.event
async def on_ready():
    print(('[' + ctime()) + '] Connection successfully established with the bot user :', bot.user.name)
    print('Bot user ID :', bot.user.name)
    await bot.change_presence(activity=discord.Game(name=f'with {len(bot.users)} users, on {len(bot.guilds)} servers | k!help'))
    print(('[' + ctime()) + '] Presence successfully updated !')
    print('___________________________________________________')
    bot.loop.create_task(status_task())

@bot.event
async def on_member_join(member):
    chan = bot.get_channel(691697960274362371)
    a = """Prends les différents rôles proposés :

— <#647732883254935553>
— <#681109048229495001>
— <#691534231976935504>

Lis le <#708834260169129994> et viens nous saluer dans <#640251005908287505>, on veut faire ta connaissance ! ewe

Des questions ? Contacte <@580590592577503243>."""
    if member.guild.id == 640251005476405268:
        e = discord.Embed(title=f"Bienvenue, {member.username} !"), description=a, color = 0xf9bbec)
        e.set_image(url="https://cdn.discordapp.com/attachments/691975441879269397/708574268815835136/image0.gif")
        await chan.send(embed=e)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('I am sorry, but it looks like you dont have the required permissions !')
        await asyncio.sleep(0.5)
        await ctx.send("I can't let you do that !")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.say('Member not found. Sorry... Retry please !')
    elif isinstance(error, commands.BadArgument):
        await ctx.say('Member not found. Retry please !')

@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction('❌')

def is_owner(ctx):
    if ctx.author.id == 580590592577503243:
        return True
    else :
        return False

@bot.group(invoke_without_command=True, aliases=['hlp', 'commandlist', 'commands'])
async def help(ctx):
    e = discord.Embed(description="🔰 Catégories d'aide", title='➡️Interactive help', color=0x33CC33, timestamp=datetime.utcnow())
    e.add_field(name='`info`', value='Infos du bot')
    e.add_field(name='`utilities`', value='Utilitaires')
    e.add_field(name='`moderator`', value='Modération')
    e.add_field(name='`fun`', value='Commandes de divertissement')
    e.set_footer(text='Entrez :3help <catégorie> pour afficher les commandes spécifiques à chaque catégorie')
    if ctx.author.id == 458586186328571913 :
        e.add_field(name='`master`', value="My master's commands !")
    await ctx.send(embed=e)

@help.command(name="info")
async def help_info(ctx):
    e = discord.Embed(description="📎 Commandes de base", title='➡️Commands list', color=0x00FFC0, timestamp=datetime.utcnow())
    e.add_field(name='`info`', value="Apprenez-en plus sur moi :3")
    e.add_field(name='`ping`', value="Testez ma réactivité !")
    e.add_field(name='`help`', value="Message d'aide d'origine")
    await ctx.send(embed=e)

@help.command(name='all')
async def help_all(ctx):
    c = discord.Embed(description="📚 Toutes les commandes", title="➡️Commands list", color=0x003366, timestamp=datetime.utcnow())
    c.set_thumbnail(url="https://cdn.discordapp.com/emojis/471044511804686348.gif?v=1")
    c.add_field(name="`help`, `info`, `ping`, `kick <membre/id>`,`ban <membre/id> <raison>`, `clear <nombre de messages>`, `pp <utilisateur>`, `roll <nombre>`", value="Liste complète")
    c.add_field(name="`info`, `utilities`, `moderator`, `fun`", value="Catégories d'aide")
    await ctx.send(embed=c)

@help.command(name='utilities')
async def help_utilities(ctx):
    c = discord.Embed(description='⚒️ Utilitaires', title='➡️Commands list', color=0x003366, timestamp=datetime.utcnow())
    c.add_field(name='`pp <utilisateur>`', value='Retourne la photo de profil d\'un utilisateur')
    await ctx.send(embed=c)

@help.command(name="moderator")
async def help_moderator(ctx):
    a = discord.Embed(description="🛡️ Modération", title='➡️Commands list', color=0xffff00, timestamp=datetime.utcnow()) 
    a.set_thumbnail(url="https://cdn.discordapp.com/emojis/474539445379661824.png?v=1")
    a.add_field(name='`kick <member/id>`', value='Exclure un membre')
    a.add_field(name='`ban <member/id> <reason>`', value='Bannir un membre')
    a.add_field(name='`clear <amount of messages>`', value='Supprimer un nombre de messages')
    await ctx.send(embed=a)

@help.command(name="fun")
async def help_fun(ctx):
    d = discord.Embed(description='🎀 Fun', title='➡️Commands list', color=0xFFA2DD, timestamp=datetime.utcnow())
    d.set_thumbnail(url="https://cdn.discordapp.com/emojis/398860813881835533.png?v=1")
    d.add_field(name='`roll <number>`', value="Jetez un dé.")
    await ctx.send(embed=d)

@commands.check(is_owner)
@help.command(name="master")
async def help_master(ctx):
    b = discord.Embed(description='♥️ Commandes réservées', title='➡️Commands list', color=0xFF0000, timestamp=datetime.utcnow())
    b.set_thumbnail(url="https://cdn.discordapp.com/attachments/476653267036930049/498859365046943745/1538964466545.png")
    b.add_field(name='`say <channel> <text>`', value='Faites-moi dire des trucs. :P')
    b.add_field(name='`shutdown`', value='ÉTEIGNEZ-MOI AAAAAAH')
    try:
        await ctx.send(embed=b)
    except:
        await ctx.send("DENIED")

#fun

@bot.command()
async def roll(ctx, value: int):
    try:
        result=randint(1,value)
        msg = await ctx.send(f'Et le résultat est...')
        await asyncio.sleep(2)
        await msg.edit(content=f'Et le résultat est... {result} ! 🎉')
    except:
        await ctx.send('Entrée invalide')

@bot.command(aliases=['utilities', 'moderator', 'all', 'master'])
async def fun(ctx):
    await ctx.send("Usage correct pour cette commande : `:3help <categorie>`")

#utils

@bot.command(aliases=['profilepic', 'ppic', 'avatar'])
async def pp(ctx, usr: discord.User):
    e = discord.Embed(description="👤 Photo de profil de {}".format(usr.name), title='➡️Avatar', color=0x5D5DFF, timestamp=datetime.utcnow())
    e.set_image(url=usr.avatar_url)
    await ctx.send(embed=e)

@commands.check(is_owner)
@bot.command(pass_context=True)
async def say(ctx, channel: discord.TextChannel, *, text):
    try:
        await ctx.channel.send(text)
    except Exception as e:
        print(e.args)

@say.error
async def say_handler(ctx, err):
    if isinstance(err, commands.CheckFailure):
        await ctx.send('Seule ma maîtresse peut utiliser cette com. UwU')
    else:
        raise err

@commands.check(is_owner)
@bot.command()
async def shutdown(ctx):
    try:
        await ctx.send('Bye !')
        print(('[' + ctime()) + '] Succesfully shutted down.')
        sys.exit()
    except Exception as e:
        print(e.args)
        await ctx.send('Une erreur est survenue.')

@shutdown.error
async def shutdown_handler(ctx, err):
    if isinstance(err, commands.CheckFailure):
        await ctx.send('Back off !')
    else:
        raise err

@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, member: discord.Member, *, reason: str = None):
    try:
        if reason==None:
            await member.ban()
            await ctx.send(f'{member.name} a été banni <3')
            await ctx.send('And dont come back !')
        else:
            await member.ban(reason=reason)
            await ctx.send(f'{member} a été banni ! Raison : ```{reason}```')
    except Exception as e:
        print(e.args)
        await ctx.send('Une erreur est survenue.')

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, *, member: discord.Member):
    try:
        await member.kick()
        await ctx.send(f'{member} a été exclu du serveur.')
    except Exception as e:
        print(e.args)
        await ctx.send('Une erreur est survenue.')

@commands.has_permissions(manage_messages=True)
@bot.command()
async def clear(ctx, amount: int):
    amount=amount+1
    try:
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"`{len(deleted)}` messages supprimés avec succès !", delete_after = 5)
    except:
        await ctx.send("Une erreur est survenue.")

@kick.error
async def kick_handler(ctx, err):
    if isinstance(err, commands.has_permissionsFailure):
        await ctx.send('Ne me fais pas faire quelque chose que tu n\'as pas le droit de faire !')
    else :
        raise err

@bot.command()
async def info(ctx):
    a = """Créé par une pieuvre
serveur de la pieuvre : [cliquez ici](https://discord.gg/JEUUM8c)"""
    e = discord.Embed(description="ako-bot", color=0xF4A2FF, timestamp=datetime.utcnow())
    e.add_field(name="Informations", value=a)
    e.set_footer(text=botversion)
    e.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=e)

@bot.command()
async def ping(ctx):
    t = await ctx.send('Pong!')
    ms = (t.timestamp - ctx.message.timestamp).total_seconds() * 1000
    await t.edit(new_content=f'Pong! Latence : **{int(ms)} milliseconds** !')


bot.run(os.environ['TOKEN'])
