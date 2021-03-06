import os
import sys
import asyncio
import telepot
import telepot.aio
import datetime
import random
import re
from sympy import sympify
import wolframalpha
import urllib3
import urllib.request
import os
import json

message_with_inline_keyboard = None

if __name__ == '__main__':
    print('이 모듈을 직접 실행하셨군요.')


async def template(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    await bot.sendMessage(chid, '- - - some text - - -')
    await asyncio.sleep(1)
    return 'okay'

##웃어주기
async def funnybell(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    res = 'ㅋ' * random.randint(2, 22)
    roll = random.randint(1, 100)
    if roll >= 95:
        await bot.sendMessage(chid, res)
    return 'okay'

##타이머
async def hglass(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    print(chat)
    minn = int(chat.replace('분 타이머', ''))
    print(minn)
    if minn <= 60:
        target = datetime.datetime.now() + datetime.timedelta(minutes=minn)
        print(target)
        A = 22
        send = await bot.sendMessage(chid, str(minn) + '분\n→카운트 시작합니다!')
        msg_idf = telepot.message_identifier(send)
        while A > 1:
            count = target - datetime.datetime.now()
            A = count.total_seconds()
            B = str(count)
            B = re.sub('\.[0-9]+$', '', B)
            try:
                B = datetime.datetime.strptime(B, "%H:%M:%S")
                H, M, S = B.hour, B.minute, B.second
            except:
                H, M, S = 0, 0, 0
            print(A)
            print(B)
            print(H, M, S)
            if A < 10:
                w = 1
            elif A > 600:
                w = random.randint(34, 82)
            else:
                w = random.randint(8, 12)
            await bot.editMessageText(msg_idf, str(minn) + '분\n→ ' + str(M) + ' : ' + str(S))
            await asyncio.sleep(w)
        await bot.editMessageText(msg_idf, str(minn) + '분\n→ 땡!!')
    else:
        await bot.sendMessage(chid, str(minn) + '분: 너무 길어요.')
    return 'okay'

## UAkey 필요함!!!
async def celc(bot, letter, UAkey):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    n=re.compile('[0-9]+')
    f=re.compile('[0-9.]+')
    print(UAkey)
    try:
        chat = chat.replace('루트', ' root')
        chat = chat.replace('√', ' root')
        chat = chat.replace('인치', ' inch to cm')
        chat = chat.replace('야드', ' yard to m')
        chat = chat.replace('마일', ' mile to km')
        chat = chat.replace('온스', ' ounce to g')
        chat = chat.replace('갤런', ' gallon to litre')

        chat = chat.replace('파운드', ' pound to kg')
        chat = chat.replace('달러', ' usd to krw')
        chat = chat.replace('엔', ' jpy to krw')
        chat = chat.replace('위안', ' cny to krw')
        chat = chat.replace('유로', ' euro to krw')
        chat = chat.replace('부가세', 'multiply 0.09090909...')

        client = wolframalpha.Client(UAkey)
        UAres = client.query(chat)
        UAres = str(next(UAres.results).text)
        UAres = UAres.replace('sqrt', '√')
        UAres = UAres.replace('~~', ' ≒ ')
        UAres = UAres.replace(',   ', '\n')
        UAres = UAres.replace('\:20a9', '')
        UAres = UAres.replace('(irreducible)', '')
        UAres = UAres.replace('(Korean won)', '')

        UAres = UAres.replace('million', 'x1000000(백만)')
        UAres = UAres.replace('billion', 'x1000000000(십억)')
        print(len(UAres))
        try:
            if 'rreducible ' in UAres:
                UAres = UAres.replace('(irreducible)', '')
                alpha = '(무한소수)'
                print('ta--da')

            else:
                alpha = ''
            UAres = str(round(float(sympify(UAres)),2))
        except: pass
        if len(UAres) > 50:
            try:
                UAres = UAres.replace('...','')
                UAres = str(round(float(UAres), 10))+'...'
                print('ta-da')
            except:pass
        n=re.compile('[0-9]+')
        A=n.findall(UAres)
        B=[]
        for i in range(len(A)):
            B.append(format(int(A[i]),','))
        for i in range(len(A)):
            UAres = UAres.replace(str(A[i]),str(B[i]))
        await bot.sendMessage(chid, '<code>' + UAres + '</code>', parse_mode='HTML')
    except:
        await bot.sendMessage(chid, chat + ' 는 올바른 계산이 아닙니다')
    return 'okay'

##카운트
async def dbm_pull(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']

    e = int(chat.replace('/pull ',''))
    if e > 22 :
        await bot.sendMessage(chid, '최대 22초 까지 카운트 합니다.')
    else :
        send = await bot.sendMessage(chid, 'Count '+str(e)+' sec\n('+name+'님 이 보냄)')
        await asyncio.sleep(3)
        msg_idf = telepot.message_identifier(send)
        while e > 0:
            await bot.editMessageText(msg_idf, str(e))
            await asyncio.sleep(3)
            e = e -1
        await bot.editMessageText(msg_idf, '땡!!!!!!!!!')
    return 'okay'

async def ready(bot, letter, key):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    bot = telepot.aio.Bot(letter['key_'])
    await bot.sendMessage(288115423, '코드 준비됨!')
    return 'okay'

async def eetime(val):
    n = datetime.datetime.now() + datetime.timedelta(hours=9)
    if val == 'epoch' or val == 'e':
        return int(n.strftime('%s'))
    elif val == 'yy':
        return int(n.year)
    elif val == 'mm':
        return int(n.month)
    elif val == 'dd':
        return int(n.day)
    elif val == 'h':
        return int(n.hour)
    elif val == 'm':
        return int(n.minute)
    else:
        return 'BAD'

async def keystone(bot, letter):
    chid = letter['chid']
    http = urllib3.PoolManager()
    url =  'https://raider.io/api/v1/mythic-plus/affixes?region=kr&locale=ko'
    v = http.request('GET', url)
    v = json.loads(v.data.decode('utf-8'))
    aff_title = v["title"]
    aff_list = v["affix_details"]
    aff=[]
    for affix in aff_list:
        aff.append(affix['description'])
    await bot.sendMessage(chid, '이번주 쐐기는 '+aff_title+'입니다.')
    await bot.sendMessage(chid, ' - '+aff[0]+'\n - '+aff[1]+'\n - '+aff[2]+'\n - '+aff[3])
    return 'okay'

##번역
async def papago(bot, letter, naver):
    chid, chat = letter['chid'], letter['chat']
    id, pw = naver['id'], naver['pw']
    chat=chat.replace('>>','')
    chat=chat.replace('»','')
    chat=chat.replace('zh-','')
    reg = re.compile('@[a-z]{2}$')
    t = re.findall(reg,chat)
    if t ==[]: t=['@nn']
    to_lang = t[0].replace('@','')
    possible = ['ko', 'en', 'ja', 'zh-CN', 'cn', 'zh-TW', 'tw', 'vi', 'id', 'th', 'de', 'ru', 'es', 'it', 'fr','nn']
    chat = re.sub(reg,'',chat)
    encQuery = urllib.parse.quote(chat)
    data = "query=" + encQuery
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", id)
    request.add_header("X-Naver-Client-Secret", pw)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        res = response.read()
        fr_lang = json.loads(res.decode('utf-8'))['langCode']
    else:
        return 'okay'
    if fr_lang not in possible :
        await bot.sendMessage(chid, '알 수 없는 언어 오류!')
        return 'okay'
    if to_lang not in possible:
        await bot.sendMessage(chid, '번역코드 오류!\n @ko 한국어\n @en 영어\n @ja 일본어\n @cn 중국어 간체\n @tw 중국어 번체\n @vi 베트남어\n @id 인도네시아어\n @th 태국어\n @de 독일어\n @ru 러시아어\n @es 스페인어\n @it 이탈리아어\n @fr 프랑스어')
        return 'okay'
    if to_lang == 'cn' :
        to_lang = 'zh-CN'
    if to_lang == 'tw':
        to_lang = 'zh-TW'
    elif fr_lang == 'ko' and to_lang == 'nn':
        to_lang = 'en'
    elif to_lang == 'nn':
        to_lang = 'ko'
    print(to_lang)
    print(fr_lang)
    chat = urllib.parse.quote(chat)
    data = 'source='+fr_lang+'&target='+to_lang+'&text=' + chat
    url = "https://openapi.naver.com/v1/papago/n2mt"
    try:
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", id)
        request.add_header("X-Naver-Client-Secret", pw)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            ee = json.loads(response_body.decode('utf-8'))
            fr_, alpha, to_, res = ee['message']['result']['srcLangType'], ' → ',ee['message']['result']['tarLangType'], ee['message']['result']['translatedText']
        else: fr_, alpha, to_, res='','','','뭔가 좀 이상한데요;;;'
    except: fr_, alpha, to_, res='','','','뭔가 좀 이상한데요;;;'
    await bot.sendMessage(chid, res+'\n\n'+fr_+alpha+to_)
    return 'okay'
        ## >>text en to kr 이런식으로 작동...
async def papago_help(bot, letter, naver):
    chid, chat = letter['chid'], letter['chat']
    await bot.sendMessage(chid, '번역 도움말입니다.\n"번역할 문장 @en" 형식으로 입력해 주세요. \n입력된 문장은 "자동감지" 입니다.\n번역 코드가 없으면 기본값은 "한영-영한" 입니다.\n\n번역코드\n @ko 한국어\n @en 영어\n @ja 일본어\n @cn 중국어 간체\n @tw 중국어 번체\n @vi 베트남어\n @id 인도네시아어\n @th 태국어\n @de 독일어\n @ru 러시아어\n @es 스페인어\n @it 이탈리아어\n @fr 프랑스어')
    return 'okay'

async def dice(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    res=random.randint(1,100)
    fog=random.randint(1,20)
    sticker_head='/home/yamcc/Pyculus/img_/DICE/n_'
    sticker_tale='.webp'
    if res<=60 and fog == 1:
        ress=res*2
        say =name+'님이 주사위를 굴려 나온 '+ str(res)+be(res)+' 더블!!!! \n'+str(ress) + be(ress)+' 나왔습니다!!'
        sticker = str(res)+'x'
    elif fog == 3 or fog == 4:
        ress = res+10
        say =name+'님이 전쟁벼림 주사위를 굴려 '+str(ress)+be(ress)+' 나왔습니다!'
        sticker = str(ress)+'+'
    elif fog == 5 :
        ress = res +15
        say =name+'님이 티탄벼림 주사위를 굴려 '+str(ress)+be(ress)+' 나왔습니다!!'
        sticker = str(ress)+'++'
    else:
        ress = res
        say =name+'님이 주사위를 굴려 '+str(ress)+be(ress)+' 나왔습니다.'
        sticker = str(res)
    await bot.sendMessage(chid, say)
    await bot.sendSticker(chid, open(sticker_head+sticker+sticker_tale,'rb'))
    if ress>100 :
        await bot.sendMessage(chid, '미터기 터져요!!!')
    return 'okay'

def be(ress):
    if str(ress)[-1] in ('2','4','5','9'): return'가'
    else: return'이'

async def fif_gui(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    mapcard=[
    '□ ','□ ','□ ','□ ','□ ',
    '□ ','□ ','□ ','□ ','□ ',
    '□ ','□ ','□ ']
    trasure=['♧ ','■ ','★ ','◎ ','△ ','☆ ']
    random.shuffle(trasure)
    mapcard.append(trasure[0])
    mapcard.append(trasure[1])
    random.shuffle(mapcard)
    mapcard.insert(5, '\n')
    mapcard.insert(11, '\n')
    ground=''
    for i in range(len(mapcard)):
        ground=ground+mapcard[i]
    await bot.sendMessage(chid, ground+'\n..\n')
    return 'okay'
