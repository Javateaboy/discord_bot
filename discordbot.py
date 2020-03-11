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
    print('ready ok')

# メッセージ受信時
@client.event
async def on_message(message):
    # BOT時は無視
    if message.author.bot:
        return

    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('すっきりしたね')
        else:
            await message.channel.send('は？黙れ')

    # メンバーのリストを取得して表示
    if message.content == '/members':
        print(message.guild.members)

    # 役職のリストを取得して表示
    if message.content == '/roles':
        print(message.guild.roles)

    # テキストチャンネルのリストを取得して表示
    if message.content == '/text_channels':
        print(message.guid.text_channnels)

    # カテゴリチャンネルのリストを取得して表示
    if message.content == '/category_channels':
        print(message.guild.categories)

    if client.user in message.mentions:
        reply = f'{message.author.mention} 呼んだ？'
        await message.channel.send(reply)

    # 先頭がmesschから始まる・・・
    if re.match('messch', message.content):
        await message.channel.send('にゃーん')

# リアクション追加時
@client.event
async def on_reaction_add(reaction, user):
    return

# 新規メンバー参加時
@client.event
async def on_member_join(member):
    return

client.run(TOKEN)