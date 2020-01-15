# _*_ coding: utf-8 _*_ 
import sys 
from PIL import Image 
from PIL import ImageDraw 
from PIL import ImageFont


import urllib.request


def ask(q):
    list = {
    'Pandarenmale':(500,250,1012,762),
    'Pandarefemale' : (600,600,512,512),
    'monk' : '#00FF96',
    'deathknight':'#C41F3B',
    'demonhunter':'#A330C9',
    'druid':'#FF7D0A',
    'Hunter':'#A9D271',
    'Mage':'#40C7EB',
    'Paladin':'#F58CBA',
    'Priest':'#FFFFFF',
    'Rogue':'#FFF569',
    'Shaman':'#0070DE',
    'Warlock':'#8787ED',
    'Warrior':'#C79C6E'
    'alliance':'#4747c9',
    'horde':'#c94747',
    '-':'#9d9d9d',
    0:'#ffffff',
    1:'#1eff00',
    2:'#0070dd',
    3:'#a335ee',
    4:'#ff8000',
    5:'#e6cc80'
    }
    print(q)
    print (list.get(q))
    return list.get(q)




imgname = 'wcc.jpg'
race = 'Pandaren'
gender = 'male'
clss = 'monk'
faction= 'alliance'
urllib.request.urlretrieve('https://render-kr.worldofwarcraft.com/character/burning-legion/224/103098592-main.jpg',imgname)
#https://render-kr.worldofwarcraft.com/character/hellscream/3/78131459-main.jpg
img = Image.open(imgname)


cropimg = img.crop(mug('Pandaren','male'))
cropimg.show()
print(cropimg.size)


    
mug('Pandaren','male')    
    
    
    
    
###
'''휴먼 00 오크 20
드웦 01 트롤 21
나엘 02 타우 22
노움 03 언데 23
드레 04 블엘 24
늑인 05 고블 25
판다 06 판다 26
공엘 07 마오 27
검드 08 높타 28
빛드 09 나본 29
쿨티 10 잔트 30
기놈 11 불페 31'''
###