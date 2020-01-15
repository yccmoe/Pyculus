import pafy
from youtube_search import YoutubeSearch
import json
import os
import telepot
import telepot.namedtuple
import asyncio


import datetime
import re
import pymysql
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

message_with_inline_keyboard = None
async def ysrch(letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    q=chat.replace('!','')
    res = YoutubeSearch(q, max_results=5).to_json()
    res=res.replace('\\','')
    d=json.loads(res)
    print(d)
    say=q+' 검색결과.'
    rtn=[]
    result=[]
    for i in range(len(d['videos'])):
        v=pafy.new(d['videos'][i]['id'])
        if v.length <=900:
            #rtn.append(v.title)
            #rtn.append(v.videoid)
            tmp=[v.title,v.videoid]
            rtn.append(tmp)
    print(rtn)        
    for i in range(len(rtn)):
        print(rtn[i][0] + ' : ' +rtn[i][1])
        result=result+[dict(text=rtn[i][0],callback_data='ytdw♡a♡'+rtn[i][1])]
    markup = InlineKeyboardMarkup(inline_keyboard=[ [i] for i in result])
#        v=pafy.new('Https://youtube.com'+str(d['videos'][i]['link']))
#        rtn.append()
    return say,markup
    
    
    
def ready(q):
    
    v=pafy.new(q)
    best = v.getbestaudio(preftype='m4a')
    best.download()
    print(v.audiostreams)
    
async def down(id):
    v= pafy.new(id)
    audio=v.audiostreams
    print(audio)
    for a in audio:
        if a.extension == 'm4a':
            print(a.bitrate, a.extension, a.get_filesize())
            print(a)
        #audio[2].download()
    best = v.getbestaudio(preftype='m4a')
    ado = v.title+'.m4a'
    ado = ado.replace('/','')
    ado = ado.replace('\\','')
    file = best.download(ado)
    
    print(ado)
#    ado=ado.replace('_','')
    await bot.sendAudio(chid, open(ado, 'rb'), title=v.title)
    
#ysrch('리쌍 챔피언')
ready('c7rCyll5AeY')