# -*- coding:utf-8 -*-
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import sys
import io
import telepot
import random
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


async def wow_old(bot,letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    q=chat.replace('/누구 ','')
    w=q
    q=quote(q)
    url = 'https://worldofwarcraft.com/ko-kr/search/character?q='+q
    INFO=[]
    lvls=[]
    svrs=[]
    aohs=[]
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    slave_lvl = soup.select('body > div.body > div > div.Pane.Pane--full.Pane--dirtDark > div.Pane-content > div > div.Pane-content > div > div.SortTable.SortTable--stretch > div.SortTable-body > a > div.SortTable-col.SortTable-data.text-nowrap.align-center')
    slave_svr = soup.select('body > div.body > div > div.Pane.Pane--full.Pane--dirtDark > div.Pane-content > div > div.Pane-content > div > div.SortTable.SortTable--stretch > div.SortTable-body > a > div:nth-of-type(6)')
    slave_aoh = soup.select('body > div.body > div > div.Pane.Pane--full.Pane--dirtDark > div.Pane-content > div > div.Pane-content > div > div.SortTable.SortTable--stretch > div.SortTable-body > a > div:nth-of-type(5)')
    for lvl in slave_lvl:
        print(lvl.text)
        lvls.append(lvl.text)
    for svr in slave_svr:
        print(svr.text)
        svrs.append(svr.text)
    m=lvls+svrs
    for i in range(int(len(m)/2)):
        #print(m[i],m[i+int((len(m)/2))])
        if m[i] =='120':
            #print qoute(m[i+int((len(m)/2))])
            url='https://raider.io/api/v1/characters/profile?region=kr&realm=' + quote(m[i+int((len(m)/2))]) +'&name='+ q +'&fields=gear%2Cmythic_plus_weekly_highest_level_runs%2Cmythic_plus_best_runs%2Cguild'
            #print(url)
            #print(m[i+int((len(m)/2))])
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            r=requests.get(url,headers=headers).json()
            try: head = r['name']+'@'+tr(m[i+int((len(m)/2))])+'\n<'+r['guild']['name']+'>\n'+str(r['gear']['item_level_equipped'])+' '+tr(r['active_spec_name']+' '+r['class'])+'\n - - - -\n'
            except: head = r['name']+'@'+tr(m[i+int((len(m)/2))])+'\n'+str(r['gear']['item_level_equipped'])+' '+tr(r['active_spec_name']+' '+r['class'])+'\n - - - -\n'
            brun = r['mythic_plus_best_runs']
            rrun = r['mythic_plus_weekly_highest_level_runs']

            #for run in rrun:
            #    print(tr(run['short_name']),str(run['mythic_level']),tr(run['num_keystone_upgrades']))
            try:rru = '주차: '+tr(rrun[0]['short_name'])+str(rrun[0]['mythic_level'])+tr(rrun[0]['num_keystone_upgrades'])
            except:rru='주차 없음'
            bru=''
            for run in brun:
                rru = rru+'\n'+tr(run['short_name'])+str(run['mythic_level'])+tr(run['num_keystone_upgrades'])
            #print(bru)
            await bot.sendMessage(chid, head+rru)
        else:
            await bot.sendMessage(chid, w+'@'+m[i+int((len(m)/2))]+'('+m[i]+')')

def test():
    list1=['1','2','3','4','5']
    list2=['q','w','e','r','t']
    n=[]
    m=list1+list2
    print(m)
    for i in range(int(len(m)/2)):
        print(m[i],m[i+int((len(m)/2))])
    for i in range(len(list1)):
        #tmp=[list1[i],list2[i]]
        n.append([list1[i],list2[i]])
    print('n')
    print(n)
    print(len(n))
    print(n[0][0])
def tr(req):
    list = {
    'ProtectionWarrior': '전탱', 
    'ArmsWarrior': '무전', 
    'FuryWarrior': '분전', 
    'Beast MasteryHunter': '야냥', 
    'MarksmanshipHunter': '격냥', 
    'SurvivalHunter': '생냥', 
    'ElementalShaman': '정술', 
    'RestorationShaman': '복술', 
    'EnhancementShaman': '고술', 
    'BrewmasterMonk': '양조', 
    'WindwalkerMonk': '공옾', 
    'MistweaverMonk': '운무', 
    'AssassinationRogue': '암살', 
    'OutlawRogue': '무법', 
    'SubtletyRogue': '잠행', 
    'BloodDeath Knight': '혈죽', 
    'FrostDeath Knight': '냉죽', 
    'UnholyDeath Knight': '부죽', 
    'FireMage': '화법', 
    'FrostMage': '냉법', 
    'ArcaneMage': '비법', 
    'GuardianDruid': '야탱', 
    'FeralDruid': '야딜', 
    'BalanceDruid': '부엉', 
    'RestorationDruid': '회드', 
    'ProtectionPaladin': '보기', 
    'RetributionPaladin': '징기', 
    'HolyPaladin': '신기', 
    'ShadowPriest': '암사', 
    'DisciplinePriest': '수사', 
    'HolyPriest': '신사', 
    'AfflictionWarlock': '고흑', 
    'DemonologyWarlock': '악흑', 
    'DestructionWarlock': '파흑', 
    'VengeanceDemon Hunter': '악탱', 
    'HavocDemon Hunter': '악딜', 
    
    'VOTW': '금고', 
    'BRH': '검때', 
    'NL': '넬타', 
    'COS': '별궁', 
    'ARC': '비전', 
    'EOA': '아즈', 
    'DHT': '어숲', 
    'MOS': '아귀', 
    'HOV': '용맹', 
    'UPPR': '상층', 
    'LOWR': '하층', 
    'COEN': '성당', 
    'SEAT': '삼두',
    
    'AD': '아탈', 
    'FH': '자지', 
    'TD': '톨다', 
    'TOS': '세스', 
    'UNDR': '썩굴', 
    'SIEGE': '보랄', 
    'SOTS': '폭풍', 
    'KR': '왕안', 
    'WM': '저택', 
    'ML': '광산', 
    'ZX': '메하',
    'CV': '메상',
    
    0:'-', 
    1:'★', 
    2:'★★', 
    3:'★★★',
    
    '가로나':'가로나', 
    '굴단':'굴단', 
    '노르간논':'노르', 
    '달라란':'달라란', 
    '데스윙':'데스윙', 
    '듀로탄':'듀로', 
    '렉사르':'렉사', 
    '말퓨리온':'말퓨', 
    '불타는 군단':'불군', 
    '세나리우스':'세나', 
    '스톰레이지':'스톰', 
    '아즈샤라':'아즈', 
    '알렉스트라자':'알렉', 
    '와일드해머':'해머', 
    '윈드러너':'윈드', 
    '줄진':'줄진', 
    '하이잘':'하이잘', 
    '헬스크림':'헬스',
    
    'Fortified':'경',
    'Tyrannical':'폭',
    'Sanguine':'피',
    'Bursting':'파',
    'Bolstering':'강',
    'Raging':'분',
    'Teeming':'무',
    'Explosive':'폭',
    'Volcanic':'화',
    'Grievous':'치',
    'Quaking':'전',
    'Overflowing':'과',
    'Skittish':'변',
    'Necrotic':'괴',
    'Infested':'',
    'Reaping':'',
    'Beguiling':'',
    'eeeeeeee':''
    
    }
    
    if list.get(req)==None:return req
    else: return list.get(req)



def liner(req):
    res = ''
    list=[
    'ᚠ','ᚰ','ᛀ','ᛐ','ᛠ',
    'ᚡ','ᚱ','ᛁ','ᛑ','ᛡ',
    'ᚢ','ᚲ','ᛂ','ᛒ','ᛢ',
    'ᚣ','ᚳ','ᛃ','ᛓ','ᛣ',
    'ᚤ','ᚴ','ᛄ','ᛔ','ᛤ',
    'ᚥ','ᚵ','ᛅ','ᛕ','ᛥ',
    'ᚦ','ᚶ','ᛆ','ᛖ','ᛦ',
    'ᚧ','ᛇ','ᛗ','ᛧ','ᚨ',
    'ᚨ','ᚸ','ᛈ','ᛘ','ᛨ',
    'ᚩ','ᚹ','ᛉ','ᛙ','ᛩ',
    'ᚪ','ᚺ','ᛊ','ᛚ','ᛪ',
    'ᚫ','ᚻ','ᛋ','ᛛ','᛫',
    'ᚬ','ᚼ','ᛌ','ᛜ','᛬',
    'ᚭ','ᚽ','ᛍ','ᛝ','᛭',
    'ᚮ','ᚾ','ᛎ','ᛞ','ᛮ',
    'ᚯ','ᚿ','ᛏ','ᛟ','ᛯ',
    'ᛰ','-',' ',' ','_'
    ]
    for i in range(req):
        res = res+random.choice(list)
    return res

def wow(query):
#    name, chid, chat = letter['name'], letter['chid'], letter['chat']
#    query=chat.replace('/누구 ','')
    q=quote(query)
    url = 'https://worldofwarcraft.com/ko-kr/search/character?q='+q
    lvls,svrs,res=[],[],{}
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    slave_lvl = soup.select('body > div.body > div > div.Pane.Pane--full.Pane--dirtDark > div.Pane-content > div > div.Pane-content > div > div.SortTable.SortTable--stretch > div.SortTable-body > a > div.SortTable-col.SortTable-data.text-nowrap.align-center')
    slave_svr = soup.select('body > div.body > div > div.Pane.Pane--full.Pane--dirtDark > div.Pane-content > div > div.Pane-content > div > div.SortTable.SortTable--stretch > div.SortTable-body > a > div:nth-of-type(6)')
    for lvl in slave_lvl: lvls.append(lvl.text)
    for svr in slave_svr: svrs.append(svr.text)
    for i in range(len(lvls)): res[svrs[i]]={'name':query,'server':svrs[i],'level':lvls[i],'gear':lvls[i]}
    print(res)
    print('-----')
    for key in res.keys():
        if res[key]['level']== '120':
            print(key)
    ### RAIDER.IO 검색 ###
            url='https://raider.io/api/v1/characters/profile?region=kr&realm='+quote(key)+'&name='+ q +'&fields=gear%2Cmythic_plus_weekly_highest_level_runs%2Cmythic_plus_best_runs%2Cmythic_plus_scores_by_season:previous%2Cguild'
            print(url)
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            r=requests.get(url,headers=headers).json()
            #print(r)
            try: res[key]['guild']='<'+str(r['guild']['name'])+'>'
            except : res[key]['guild']='길드 없음'
            res[key]['gear']=str(r['gear']['item_level_equipped'])
            res[key]['spec']=tr(r['active_spec_name']+r['class'])
            res[key]['rader']=r['mythic_plus_scores_by_season'][0]['scores']['all']
            res[key]['brun']= b_run(r['mythic_plus_best_runs'])
            res[key]['rrun']= r_run(r['mythic_plus_weekly_highest_level_runs'])

    
    print(res)
    print(type(res))
    
    
    
    
    
def r_run(r):
    try:
        droptable={2:'(445)',3:'(445)',4:'(450)',5:'(450)',6:'(455)',7:'(455)',8:'(460)',9:'(460)',10:'(465)',11:'(465)',12:'(470)',13:'(470)',14:'(470)',15:'(475)'}
        parking=r[0]['mythic_level']
        if parking >=15: parking = 15
        box=droptable.get(parking)
        return '\n'+tr(r[0]['short_name'])+str(r[0]['mythic_level'])+' | '+tr(r[0]['num_keystone_upgrades'])+' '+box
    except: return '주차 없음'
    
    
    
    
    
    
    
def b_run(r):
    re=''
    for e in r:
        ra=''
        for a in e['affixes']:
            ra=ra+tr(a['name'])
        re=re+'\n'+ra+' | '+tr(e['short_name'])+str(e['mythic_level'])+' | '+tr(e['num_keystone_upgrades'])
    print(re)
    return re
    
    #rru = rru+'\n'+tr(run['affixes']+tr(run['short_name'])+str(run['mythic_level'])+' '+tr(run['num_keystone_upgrades'])

def afx(r):
    affix=''
    for ax in affx:
        affix=affix+tr(r['name'])

wow('포로리')