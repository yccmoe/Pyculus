from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import random
okay='okay'

def start():
    res=[]
    res=res+[dict(text= '빠른 올랜덤', callback_data= 'menupann♡Run')]
    res=res+[dict(text= '태그 선택', callback_data= 'menupann♡allowTag'),dict(text= '종료', callback_data= 'menupann♡Exit')]
    
    keyboard=InlineKeyboardMarkup(inline_keyboard=[ [i] for i in res ] )
    print([i]+[i+1]for i in res)
    return keyboard
    
def MarkupCreate(tag, AD):
    res=[]
    lastwill=''
    if AD=='first_allow':
        AD='allow'
        res=res+[dict(text='올랜덤', callback_data='menupann♡'+AD+'♡All')]    
    elif AD=='allow': 
        lastwill='pass'  
    if AD != 'show':
        for i in range(len(tag)):
            res=res+[dict(text=tag[i], callback_data='menupann♡'+AD+'Tag♡'+tag[i])]
    else: res = res+[dict(text='메뉴판 전체 보기', callback_data='menupann♡showList')]
    if lastwill=='pass':
        res=res+[dict(text='제외태그 선택', callback_data='menupann♡denyTag')]
    if AD=='deny':
        res=res+[dict(text='메뉴를 골라줘!', callback_data='menupann♡Run')]
       
    markup = InlineKeyboardMarkup(inline_keyboard=[ [i] for i in res])

    print(res)
    print(markup)
    return markup
    
    

    
def tags(chid):
    ## sql 쿼리 검색 ###
    return ['수유','미아','미삼','훠거','길음','무한','냉면','수영']
    
def Pick(chid,allow,deny):
    if allow==None: pass
    if deny==None:pass
    ###SQL쿼리###
    allows = ['엄마손 기사식당','구겁실 국밥집','명륜진사갈비','일품향 훠거']
    denys = ['엄마손 기사식당','명인만두']
    res = random.choice(list(set(allows)-set(denys)))
    
    return res
def Picklist(chid,allow,deny):
    ###SQL쿼리###
    if allow==None : print(allow)
    if deny==None : print(deny)
    allows = ['엄마손 기사식당','구겁실 국밥집','명륜진사갈비','일품향 훠거']
    denys = ['엄마손 기사식당','명인만두']
    res = list(set(allows)-set(denys))
    print(res)
    e=''
    for i in range(len(res)):
        e=e+str(i+1)+'. '+res[i]+'\n'
    print(e)
    return e    

def addMenu(chid, chat):
    menu = chat.replace('/메뉴추가 ','')
    menu = chat.replace('/메뉴추가','')
    return 'okay'

def addTag(chid, chat):
    tag = chat.replace('/태그추가 ','')
    tag = chat.replace('/태그추가','')
    return 'okay'
    