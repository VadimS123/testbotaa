import discord
from discord.ext import commands
import os
 
Bot = commands.Bot(command_prefix='<')
 
 
@Bot.event
async def on_ready():
    print("Now bot is online")
 
 
@Bot.command(pass_context=True)
async def test(ctx):
    await Bot.say("Look it works!")

@Bot.command(pass_context=True)
async def author(ctx):
    await Bot.say("Автор бота: Вадим#2677")
 
 @Bot.command(pass_context=True)
async def helloe(ctx):
    await Bot.say("(@everyone)Привет всем!")

@Bot.command(pass_context=True)
async def ping(ctx):
    await Bot.say("Pong!")

 @Bot.command(pass_context=True)
async def rules(ctx):
    await Bot.say("Правила читать в кнале #Правила")

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
