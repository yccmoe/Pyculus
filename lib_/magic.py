import os
import asyncio
import telepot
import telepot.aio

async def ping (bot, letter, TOKEN):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    fromdir = os.path.dirname(os.path.abspath(__file__))
    await bot.sendMessage(chid, '안녕하새요!!', parse_mode='markdown')
    return 'okay'

async def ping_full (bot, letter, TOKEN):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    fromdir = os.path.dirname(os.path.abspath(__file__))
    await bot.sendMessage(chid, "시스템 정보...\n\n`@/home/yamcc/Pyculus/Main.py\n@"+fromdir+"\n\nkey_"+TOKEN+"\n\nchid@"+str(chid)+"\n\nuser@"+name+"`", parse_mode='markdown')
    return 'okay'    