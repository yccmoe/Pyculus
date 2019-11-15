import datetime
import random
import telepot
import urllib.request
import sys
import io
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

## Mysql 
## _No, stime, etime, do, yy, mm, ww, dd


def sbj_dict(text):
    if text.count('국어')>=1 :return '국어'
    elif text.count('영어')>=1 :return '영어'
    elif text.count('국사')>=1 :return '국사'
    elif text.count('회계')>=1 :return '회계'
    elif text.count('세법')>=1 :return '세법'
    elif text.count('사회')>=1 :return '사회'
    elif text.count('과학')>=1 :return '과학'
    elif text.count('수학')>=1 :return '수학'
    elif text.count('행정학')>=1 :return '행학'
    elif text.count('행정법')>=1 :return '행법'
    elif text.count('행학')>=1 :return '행학'
    elif text.count('행법')>=1 :return '행법'
    elif text.count('코딩')>=1 :return '코딩'
    elif text.count('운동')>=1 :return '운동'
    elif text.count('수업')>=1 :return '수업'
    elif text.count('휴식')>=1 :return '휴식'
    elif text.count('핫산')>=1 :return '핫산'
    else:return '기타'
    
def stamp(q):
    n=datetime.datetime.now()+datetime.timedelta(hours=9)
    if q=='d' or q=='day': return int(str(n.strftime('%Y'))+str(n.strftime('%m'))+str(n.strftime('%d')))
    if q=='w' or q=='week': return int(str(n.isocalendar()[0]) + str(n.isocalendar()[1]))
    if q=='m' or q=='month': return int(str(n.strftime('%Y'))+str(n.strftime('%m')))
    if q=='y' or q=='year': return int(str(n.strftime('%Y')))
    if q=='e' or q=='epoch': return n.timestamp()
print(stamp('d'))
print(stamp('w'))
print(stamp('m'))
print(stamp('y'))
print(stamp('e'))

def subject(letter):
    s_list=('국어','영어','국사','회계','세법','행법','행학','핫산','코딩','게임','운동','휴식')
    t = letter['chat']
    t = t.replace('!','')
    if t in s_list: return t
    else: return 'no'

## if etime이 22인게 있으면....
## etime = 지금
## XX N탐!
## YY 기록시작!!
async def log(letter,key):
    s_list=('국어','영어','국사','회계','세법','행법','행학','핫산','코딩','게임','운동','휴식')
    conn = pymysql.connect(host=hst, user=usr, password=pss, db=dbb, charset='utf8' )
    t = letter['chat']
    t = t.replace('!','')
    if t in s_list: 
 

    else: return 'no'
    