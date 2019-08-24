
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import telepot
import time



async def start(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    letter['intent']='menupann.Start'
    cat='force'
    hash = hsh(letter,cat)
    data = ''
    keyboard=InlineKeyboardMarkup(inline_keyboard=[
    [{'text': '빠른 올랜덤', 'callback_data': 'menupann.QuickAll'}], 
    [{'text': '태그 선택', 'callback_data': 'menupann.Go2Allow'},{'text': '종료', 'callback_data': 'menupann.Exit'}]
    ])
    message_with_inline_keyboard = await bot.sendMessage(chid, '몬가 먹을게 애매한 분위기군요..', reply_markup=keyboard)
    return message_with_inline_keyboard, hash, data

####여기서부터 콜백으로만 작동####
async def QuickAll(bot, letter, msg_idf):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    letter['intent']='menupann.QuickAll'
    cat='force'
    AD='Allow'
    hash = hsh(letter,cat)
    #### 대충 올랜덤 돌려서 결과 나옴 ####
    message_with_inline_keyboard = await bot.editMessageText(mag_idf, '대충 올랜덤')
    return message_with_inline_keyboard, 'okay', 'okay'
    
    
async def Allow(bot, letter, msg_idf):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    letter['intent']='AddAllow'
    cat='force'
    AD='Allow'
    hash = hsh(letter,cat)
    message_with_inline_keyboard = await bot.editMessageText(mag_idf, '몬가 먹을게 애매한 분위기군요..\n포함할 태그를 추가합니다.', reply_markup=MarkupCreate(chid,AD))
    return message_with_inline_keyboard    

async def Exit(bot, letter, msg_idf):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    letter['intent']='exit'
    cat='force'
    AD='Allow'
    hash = hsh(letter,cat)
    message_with_inline_keyboard = await bot.editMessageText(mag_idf, '펑')
    return message_with_inline_keyboard    


####바퀴와 불꽃####
def tags(chid):
    ###대충 SQL 돌리는 내용###
    return ['a','b','c','d','EE']
    
def MarkupCreate(chid,AD):
    tag = tags(chid)
    res=[]
    res=res+[dict(text='올랜덤', callback_data=AD+'All')]
    
    for i in range(len(tag)):
        res=res+[dict(text=tag[i], callback_data=AD+tag[i])]
    markup = InlineKeyboardMarkup(inline_keyboard=[ [i] for i in res])
    print(res)
    print(markup)
    return markup
    
def hsh(letter,cat):
    if cat=='normal':
        res=str(letter['chid'])+letter['name']+letter['intent']
    else: res=str(letter['chid'])+letter['intent']
    return res
    
#MarkupCreate(288,'allow')

