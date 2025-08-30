import discord
import random
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)


@client.event
async def on_message(message):
    if message.author == client.user:  # Evita que el bot se responda a sí mismo
        return


    if message.content.startswith("$elegir"):
        partes = message.content.split()[1:]  
        
        if not partes:
            await message.channel.send("❌ Debes darme opciones. Ejemplo: `!elegir pizza hamburguesa pasta`")
        else:
            eleccion = random.choice(partes)
            await message.channel.send(f"🤔 Yo elijo: **{eleccion}**")

cara_o_cruz = ["cara", "cruz"]
@client.event
async def on_message(message):
    if message.author == client.user:  # Evita que el bot se responda a sí mismo
        return

 
    if message.content.startswith("$lanzarmoneda"):
        resultado_c_o_c = random.choice(cara_o_cruz)
        await message.channel.send(f"🪙 Ha salido: **{resultado_c_o_c}**")

client.run("token aqui")
