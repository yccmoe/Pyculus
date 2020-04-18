import asyncio
import telepot
import telepot.aio
import datetime
import re
import pymysql
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import random
import telepot
import urllib.request
import sys
import io
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


message_with_inline_keyboard = None


if __name__ == '__main__':
    print('이 모듈을 직접 실행하셨군요.')
    

def paser(text):
    if text.find('!')!=0:  
        return 'Error'
    text = text.replace('!','')
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
    elif text.count('시마이')>=1 :return 'END'
    elif text.count('끝')>=1 :return 'END'
    elif text.count('완')>=1 :return 'END'
    elif text.count('그만')>=1 :return 'END'
    elif text.count('접')>=1 :return 'END'
    else:return '기타'
    
def stamp(q):
    n=datetime.datetime.now()+datetime.timedelta(hours=9)
    if q=='d' or q=='day': return int(str(n.strftime('%Y'))+str(n.strftime('%m'))+str(n.strftime('%d')))
    if q=='w' or q=='week': return int(str(n.isocalendar()[0]) + str(n.isocalendar()[1]))
    if q=='m' or q=='month': return int(str(n.strftime('%Y'))+str(n.strftime('%m')))
    if q=='y' or q=='year': return int(str(n.strftime('%Y')))
    if q=='e' or q=='epoch': return n.timestamp()
    
#print(stamp('d'))
#print(stamp('w'))
#print(stamp('m'))
#print(stamp('y'))
#print(stamp('e'))

def subject(letter):
    s_list=('국어','영어','국사','회계','세법','행법','행학','핫산','코딩','게임','운동','휴식')
    t = letter['chat']
    if t.find('!')!=0:  
        return 'no'
    t = t.replace('!','')
    if t in s_list: return t
    else: return 'no'

## if etime이 22인게 있으면....
## etime = 지금
## XX N탐!
## YY 기록시작!!
def timecelc(val):
    if val >= 3600:
        res = str(round((val/3600),1)) +'탐'
    elif val >=300:
        res = str(round((val/60),0))+'분'
    else :
        res = '5분 미만  부스러기'
    res = res.replace ('.0','')
    return res
    
async def quest(letter, key):
    now = stamp(d)
    name, chid, chat = letter['name'],letter['chid'],letter['chat']
    memo = chat.replace('+','')
    hst, usr, pss, dbb  = key['host'], key['user'], key['pass'], key['db']
    conn = pymysql.connect(host=hst, user=usr, password=pss, db=dbb, charset='utf8' )
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO quest (day, chid, name, memo) VALUES (%s, %s, %s, %s)'
            cursor.execute(sql,(now, chid, name, memo))
            conn.commit()
        conn.close()
        return '일퀘 추가됨!'
    except:
        return '일퀘 추가 실패함!'

#async def timee(letter,key):
async def timee(letter,key):
    name, chid, chat = letter['name'],letter['chid'],letter['chat']
    hst, usr, pss, dbb  = key['host'], key['user'], key['pass'], key['db']
    conn = pymysql.connect(host=hst, user=usr, password=pss, db=dbb, charset='utf8' )
    
    print(paser(chat))
    if paser(chat)=='Error':
        print('not okay')
        return
    if paser(chat)=='END':
#        await bot.sendMessage(chid, '- - - some text - - -')
        return
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO timee (stime,etime,dtime,chid,name,cat,dstamp,wstamp,mstamp,ystamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql,(stamp(e),22,22,chid,name,paser(chat),stamp(d),stamp(w),stamp(m),stamp(y)))
            conn.commit()
        conn.close()
        await bot.sendMessage(chid, name+'의 '+paser(chat)+' 기록 시작!')
        return 'okay'
    except:
#        print('INSERT INTO timee (stime,etime,dtime,chid,name,cat,dstamp,wstamp,mstamp,ystamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
#        print(stamp('e'),'22','22','chid','name',paser(chat),stamp('d'),stamp('w'),stamp('m'),stamp('y'))
        return 'fail'
        
async def semaii(letter, key):
    name, chid, chat = letter['name'],letter['chid'],letter['chat']
    hst, usr, pss, dbb  = key['host'], key['user'], key['pass'], key['db']
    conn = pymysql.connect(host=hst, user=usr, password=pss, db=dbb, charset='utf8' )
    try:
        with conn.cursor() as cursor:
            sql='update timee set etime =%s where name=%s and chid=%s and etime=22;'
            cursor.execute(sql,(stamp(e),name,chid))
            conn.commit()
            sql='update timee set dtime=etime-stime where name=%s and chid=%s and dtime=22;'
            cursor.execute(sql,(name,chid))
            conn.commit()
            
            
        conn.close()
        
        return 'okay'
    except:
        return 'fail'
        
        
#timee('시마이')