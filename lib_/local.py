#-*- coding:utf-8 -*-

import json
from youtube_search import YoutubeSearch
import requests
            
url='https://raider.io/api/v1/characters/profile?region=kr&realm=불타는 군단&name=왕츤츤&fields=gear%2Cmythic_plus_weekly_highest_level_runs%2Cmythic_plus_best_runs%2Cguild'
r=requests.get(url)
r=json.decode(r)

print(r)

q='미려적신화 조매력'
res = YoutubeSearch(q, max_results=1).to_json()
res=res.replace('\\','')
d=json.loads(res)
e=res.json()
print(d)
print(e)