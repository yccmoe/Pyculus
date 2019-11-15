import random
import urllib.request
import sys
import io
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
code_list=(
        '!ms-e4C-wByMkmb?BU5J?Wd',
        '!=dc@rB%Ld&5=jTt7VSwx5g',
        '!S3h4Mx7cK_3n#L!_Lf*!ES',
        '!p5aTDW$cYC6?-9tEuGb@N3',
        '!m&RS7Q&_W7P-+-n%%=?yqP',
        '!jsq77eP^r#&!*G95&p+Pp$',
        '!EuF+Cg7Myqe^q%Zu&YuB2-',
        '!k?2W@qcCmjP35w6SPn+RZG',
        '!ECTa8?aa4@QXs3aQwmU85T',
        '!!&r&K63rzcD%V3%?5+YrUR',
        '!w?Q54?W*E^K=txUvg9Akcb',
        '!uRNeA7rsDQ8PK*zw*YLb!=',
        '!S*8hmV&48E9V3QQFdm+429',
        '!WQ&varL2VM@X8uzR^kmBMh',
        '!PX7z7q!TCS6EZ#jk*AHJZh',
        '!#a$P!^8m%L!*25BDGZ@+g6',
        '!*4cu5wjkpyp5un-KnNZVJy',
        '!LhhmA$mWcG8c7PNCv*-UsT',
        '!@&5%Y?Ck&q!&YTj!W=-2C!',
        '!D27agtfK&rE2*7YY_e-fcJ',
        '!QYnGtry$4zSMUn_@=k72-B',
        '!eeTAbvQfHN+Yzh5m6D&CGv'
        )
        
def greeting():
    hi=('안녕하새요!','안녕하세요!','반갑습니다!','오늘도 멋져요!','무엇을 도와드릴까요?','부르셨나요?')
    return random.choice(hi)

    
def butten():
    res=[
        [{'text':'왼쪽', 'callback_data': 'remote♡lb'},{'text':'모두켜기', 'callback_data': 'remote♡Allon'},{'text':'오른쪽', 'callback_data': 'remote♡rb'}],
        [{'text':'모든 불 끄기', 'callback_data': 'remote♡Alloff'}],
        [{'text':'바테이블', 'callback_data': 'remote♡bar'},{'text':'책상', 'callback_data': 'remote♡desk'}],
        [{'text':'! 모든것을 파괴하도록 하십시오.', 'callback_data': 'remote♡dest'}]
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=res)
    return keyboard

def press(name,q,key):
    url=[]
    if q=='lb':
        url.append('https://maker.ifttt.com/trigger/r_on/with/key/')
        m = name+'님이 왼쪽 불을 켭니다.'
    if q=='rb':
        url.append('https://maker.ifttt.com/trigger/l_on/with/key/')
        m = name+'님이 오른쪽 불을 켭니다.'
    if q=='Allon':
        url.append('https://maker.ifttt.com/trigger/r_on/with/key/')
        url.append('https://maker.ifttt.com/trigger/l_on/with/key/')
        m = name+'님이 모든 불을 켭니다.'
    if q=='Alloff':
        url.append('https://maker.ifttt.com/trigger/r_off/with/key/')
        url.append('https://maker.ifttt.com/trigger/l_off/with/key/')
        m = name+'님이 모든 불을 끕니다.'
    if q=='bar':
        url.append('https://maker.ifttt.com/trigger/3y_on/with/key/')
        m = name+'님이 바테이블을 켭니다.'
    if q=='desk':
        if name == "Parlando" : name = '성연'
        if name=='준모' or name=='원용': url.append('https://maker.ifttt.com/trigger/4ch1_on/with/key/')
        if name=='태양' or name=='성연': url.append('https://maker.ifttt.com/trigger/4ch2_on/with/key/')
        if name=='승화' or name=='태준': url.append('https://maker.ifttt.com/trigger/4ch3_on/with/key/')
        url.append('https://maker.ifttt.com/trigger/4ch4_on/with/key/')
        m = name+'님이 책상을 켭니다.'
    if q=='destreal':
        url.append('https://maker.ifttt.com/trigger/r_off/with/key/')
        url.append('https://maker.ifttt.com/trigger/l_off/with/key/')
        url.append('https://maker.ifttt.com/trigger/3y_off/with/key/')
        url.append('https://maker.ifttt.com/trigger/4ch_off/with/key/')
        m = '...'+exitr()
    if q=='dest':
        m = name+'님이 모든것을 파괴합니다...\n...'+exit()
    for i in range(len(url)):
        urllib.request.urlopen(url[i]+key)
    
    print(name)
    return m
def exit():
    bi=('정말 모든것을요?', '진짜로요?', '정말로요?', '확실한가요?')
    return random.choice(bi)
def exitr():
    bi=('안녕히...', '지브스는 행복했어요...','잘가요...')
    return random.choice(bi)
def distAllbutten():
    res=[
        [{'text':random.choice(code_list), 'callback_data': 'remote♡destreal'}],
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=res)
    return keyboard
    