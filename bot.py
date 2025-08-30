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


# Función para generar contraseñas
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password


# Lista para cara o cruz
cara_o_cruz = ["cara", "cruz"]

@client.event
async def on_message(message):
    if message.author == client.user:  # Evita que el bot se responda a sí mismo
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")

    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(10))

    elif message.content.startswith('$elegir'):
        partes = message.content.split()[1:]  
        if not partes:
            await message.channel.send("❌ Debes darme opciones. Ejemplo: `$elegir pizza hamburguesa pasta`")
        else:
            eleccion = random.choice(partes)
            await message.channel.send(f"🤔 Yo elijo: **{eleccion}**")

    elif message.content.startswith('$lanzarmoneda'):
        resultado_c_o_c = random.choice(cara_o_cruz)
        await message.channel.send(f"🪙 Ha salido: **{resultado_c_o_c}**")

    elif message.content.startswith('$dado'):
        partes = message.content.split()
        # Si el usuario puso un número, ese será el número de caras
        if len(partes) > 1 and partes[1].isdigit():
            caras = int(partes[1])
        else:
            caras = 6  # Por defecto, dado de 6 caras
        resultado = random.randint(1, caras)
        await message.channel.send(f"🎲 El dado de {caras} caras cayó en: **{resultado}**")



client.run("TOKEN_AQUI")
