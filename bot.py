import discord
from discord.ext import commands
import os
 
Bot = commands.Bot(command_prefix='<')

Bot.remove_command('help')

@Bot.event
async def on_ready():
    print("Now bot is online")
 
@Bot.command(pass_context=True)
async def test(ctx):
    await Bot.say("Работаю стабильно!")
  
@Bot.command(pass_context= True)
async def help(ctx):
 emb = discord.Embed(title= "Мои комманды:", colour= 0x39d0d6
 emb.add_field(name= "{}help".format(prefix), value= "Меню помощи")
 emb.add_field(name= "{}author".format(prefix),value= "Автор бота")
 emb.add_field(name= "{}hello".format(prefix),value= "посылает всем привет")
 emb.add_field(name= "{}ping".format(prefix),value= "Задержка")
 emb.add_field(name= "{}info @user".format(prefix),value= "информация о пользователе")
 await Bot.say (embed= emb)
 await Bot.delete_message(ctx.message)
 

@Bot.command(pass_context=True)
async def author(ctx):
    await Bot.say("Автор бота: Вадим#2677")
 
@Bot.command(pass_context=True)
async def hello(ctx):
    await Bot.say("(@everyone) Привет всем!")

@Bot.command(pass_context=True)
async def ping(ctx):
    await Bot.say("Pong!")
  


@Bot.command(pass_context= True)
async def info(ctx,user: discord.User):
 emb = discord.Embed(title= "Информация о пользователе {}".format(user.name),colour= 0x39d0d6)
 emb.add_field(name= "Name", value= user.name)
 emb.add_field(name= "ID:",value= user.id)
 emb.set_thumbnail(url= user.avatar_url)
 emb.set_author(name= Bot.user.name,url= "https://discordapp.com/oauth2/authorize?&client_id=570899950649606144&scope=bot&permissions=8")
 emb.set_footer(text= "Запрошено: {}".format(user.name), icon_url= user.avatar_url)
 await Bot.say(embed= emb)
 await Bot.delete_message(ctx.message)
 


token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
