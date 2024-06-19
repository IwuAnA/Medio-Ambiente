import discord, random
from discord.ext import commands

reciclaje = ['#. Separa tus reciduos', '#. Limpia tus envases', '#. Reutiliza lo que puedas', '#. Reduce el uso de plasticos', '#. Informate y participa con tu comunidad']
desechoss = ['#. Adopte una dieta mas sostenible', '#. Compre solo lo que necesite', '#. Almacene los alimentos con sensatez', '#. Comprenda el etiquetado de los alimentos', '#. Haga uso de los alimentos antes de desecharlos']
ahorros = ['#. Desenchufar dispositivos que no esten en uso', '#. Disminuir el uso de aparatos electronicos', '#. Elegir aparatos de mayor eficiencia energita', '#. Recordar apagar las luces', '#. Realizar duchas mas rapidas']
ayudas = ['$reciclar', '$desechos', '$ahorro']


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Bienvenido {member.mention} a {guild.name}!, Los comandos que hay los puedes revisar en $helper'
        await guild.system_channel.send(to_send)

@bot.command()
async def helper(ctx):

    await ctx.send(ayudas)

@bot.command()
async def reciclar(ctx):
    
    select = random.choice(reciclaje)
    await ctx.send(select)

@bot.command()
async def desechos(ctx):
    
    select = random.choice(desechoss)
    await ctx.send(select)

@bot.command()
async def ahorro(ctx):
    
    select = random.choice(ahorros)
    await ctx.send(select)


bot.run('')