import discord
import os
import asyncio
import re

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()
guild = discord.Guild

# 起動時
@client.event
async def on_ready():
    print('Fuck you')

# メッセージ受信時
@client.event
async def on_message(message):
    # BOT時は無視
    if message.author.bot:
        return
    # 先頭がmesschから始まる・・・
    if re.match('messch', message.content):
        await message.channel.send('にゃーん')

client.run(TOKEN)