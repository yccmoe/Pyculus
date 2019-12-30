import pafy
from youtube_search import YoutubeSearch
import json
import os
def ysrch(q):
    #name, chid, chat = letter['name'], letter['chid'], letter['chat']
    #q=chat.replace('!','')
    res = YoutubeSearch(q, max_results=1).to_json()
    res=res.replace('\\','')
    d=json.loads(res)
    return 'Https://youtube.com'+str(d['videos'][0]['link'])
    
    
def down(q):
    v= pafy.new(ysrch(q))
    audio=v.audiostreams
    for a in audio:
        
        print(a.bitrate, a.extension, a.get_filesize())
    audio[2].download()
    
down('조매력 미려적신화')
    