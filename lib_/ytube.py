import pafy
from youtube_search import YoutubeSearch
import json
import os
import telepot
import telepot.namedtuple
def ysrch(q):
    #name, chid, chat = letter['name'], letter['chid'], letter['chat']
    #q=chat.replace('!','')
    res = YoutubeSearch(q, max_results=1).to_json()
    res=res.replace('\\','')
    d=json.loads(res)
    return 'Https://youtube.com'+str(d['videos'][0]['link'])
    
    
async def down(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    q = chat.replace('!sr','')
    v= pafy.new(ysrch(q))
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
    
#down('리쌍 챔피언')
