import discord
from discord.ext import commands
from discord.ext.commands import Bot
 
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

@Bot.command(pass_context=True)
async def say(ctx):
    say_at_me = input("Введите сообщение через консоль: ")
    await Bot.say(say_at_me)

Bot.run(NTcwODk5OTUwNjQ5NjA2MTQ0.XMLD_Q.9O_oA_k0pgWTc5GvK6QxTCE0an4)