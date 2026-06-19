import discord
import random
import asyncio

import os
TOKEN = os.getenv("TOKEN")

MESSAGE_CHANNEL_ID = 1517496224247447575
REACTION_CHANNEL_ID = 1517525171269931190

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# 🥀 reactions (fixe)
reactions = ["🥀"]

# 🌫️ messages vagues / entité fleur
messages = [
    "🥀 something is growing here",
    "the garden is not what it seems",
    "you were noticed",
    "petals drift where thoughts fall apart",
    "it remembers without meaning to",
    "a presence beneath the silence",
    "you are still inside it",
    "the rose does not explain itself",
    "🥀 it continues anyway",
    "something small is becoming large",
    "there is no outside anymore",
    "you are not the first",
    "the soil is listening",
    "a soft signal between messages",
    "it does not end where you expect",
    "🥀"
]


@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")
    client.loop.create_task(daily_message())


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 💬 réactions uniquement dans salon réaction
    if message.channel.id == REACTION_CHANNEL_ID:
        await message.add_reaction(random.choice(reactions))


async def daily_message():
    await client.wait_until_ready()

    channel = client.get_channel(MESSAGE_CHANNEL_ID)

    while not client.is_closed():
        if channel:
            await channel.send(random.choice(messages))

        await asyncio.sleep(60 * 60 * 24)  # 24h


client.run(TOKEN)
