# -*- coding:utf-8 -*-
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import sys
import io
import telepot
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

q = '저주'
async def wow(bot,letter):
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
    m=list1+list2
    print(m)
    for i in range(int(len(m)/2)):
        print(m[i],m[i+int((len(m)/2))])
        
def tr(req):
    list = {'Protection Warrior': '전탱', 'Arms Warrior': '무전', 'Fury Warrior': '분전', 'Beast Mastery Hunter': '야냥', 'Marksmanship Hunter': '격냥', 'Survival Hunter': '생냥', 'Elemental Shaman': '정술', 'Restoration Shaman': '복술', 'Enhancement Shaman': '고술', 'Brewmaster Monk': '양조', 'Windwalker Monk': '공옾', 'Mistweaver Monk': '운무', 'Assassination Rogue': '암살', 'Outlaw Rogue': '무법', 'Subtlety Rogue': '잠행', 'Blood Death Knight': '혈죽', 'Frost Death Knight': '냉죽', 'Unholy Death Knight': '부죽', 'Fire Mage': '화법', 'Frost Mage': '냉법', 'Arcane Mage': '비법', 'Guardian Druid': '야탱', 'Feral Druid': '야딜', 'Balance Druid': '부엉', 'Restoration Druid': '회드', 'Protection Paladin': '보기', 'Retribution Paladin': '징기', 'Holy Paladin': '신기', 'Shadow Priest': '암사', 'Discipline Priest': '수사', 'Holy Priest': '신사', 'Affliction Warlock': '고흑', 'Demonology Warlock': '악흑', 'Destruction Warlock': '파흑', 'Vengeance Demon Hunter': '악탱', 'Havoc Demon Hunter': '악딜', 'VOTW': '금고', 'BRH': '검때', 'NL': '넬타', 'COS': '별궁', 'ARC':'비전', 'EOA': '아즈', 'DHT': '어숲', 'MOS': '아귀', 'HOV': '용맹', 'UPPR': '상층', 'LOWR': '하층', 'COEN': '성당', 'SEAT': '삼두', 'AD': '아탈', 'FH': '자지', 'TD': '톨다', 'TOS': '세스', 'UNDR': '썩굴', 'SIEGE': '보랄', 'SOTS': '폭풍', 'KR': '왕안', 'WM': '저택', 'ML': '광산', 0: ' -소진- ' , 1:' ★' , 2:' ★★', 3:' ★★★','가로나':'가로나', '굴단':'굴단', '노르간논':'노르', '달라란':'달라란', '데스윙':'데스윙', '듀로탄':'듀로', '렉사르':'렉사', '말퓨리온':'말퓨', '불타는 군단':'불군', '세나리우스':'세나', '스톰레이지':'스톰', '아즈샤라':'아즈', '알렉스트라자':'알렉', '와일드해머':'해머', '윈드러너':'윈드', '줄진':'줄진', '하이잘':'하이잘', '헬스크림':'헬스'}
    try: return list.get(req)
    except: return req

