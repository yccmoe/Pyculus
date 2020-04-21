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
import calendar
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import key_
import time

n=datetime.datetime.now()+datetime.timedelta(hours=9)
key=key_.kids('std')
bot = telepot.Bot(key_.kids('jv'))
wk=['월','화','수','목','금','토','일']
w=n.weekday()
lastday= calendar.monthrange(int(n.strftime('%Y')),int(n.strftime('%m')))[1]


def stamp(q):
    n=datetime.datetime.now()+datetime.timedelta(hours=9)
    if q=='d' or q=='day': return int(str(n.strftime('%Y'))+str(n.strftime('%m'))+str(n.strftime('%d')))
    if q=='w' or q=='week': return int(str(n.isocalendar()[0]) + str(n.isocalendar()[1]))
    if q=='m' or q=='month': return int(str(n.strftime('%Y'))+str(n.strftime('%m')))
    if q=='y' or q=='year': return int(str(n.strftime('%Y')))
    if q=='e' or q=='epoch': return n.timestamp()

def timecelc(val):
    if val >= 3600:
        res = str(round((val/3600),1)) +'탐!!'
    elif val >=300:
        res = str(round((val/60),0))+'분!'
    else :
        res = '5분 미만  부스러기'
    res = res.replace ('.0','')
    return res    
    
def graph(v,val):
    if v=='d': return '■'*int(round((val/1300),1))
    if v=='w': return '■'*int(round((val/12500),1))
    if v=='m': return '■'*int(round((val/54000),1))
    if v=='w': return '■'*int(round((val/600000),1))



def Report(req):
    if req=='DoNotRun': return
    memo={'d':('dstamp','님의 '+wk[w]+'요일!'),
          'w':('wstamp','님의 '+str(n.isocalendar()[1])+'번 째 주!') ,
          'm':('mstamp','님의 '+str(n.strftime('%m'))+'월!!!!!'),
          'y':('ystamp','님, '+str(n.strftime('%Y'))+'년 정말 노력했군요!')
          }
    conn = pymysql.connect(host=key['host'],user=key['user'],password=key['pass'],db=key['db'],charset='utf8')
    with conn.cursor() as cursor:
        sql="select chid from timee where "+memo[req][0]+"=%s GROUP BY chid ;"
        cursor.execute(sql,(stamp(req)))
        chats=cursor.fetchall()
        for chat in chats:
            sql="select name from timee where "+memo[req][0]+"=%s and chid=%s GROUP BY name ;"
            cursor.execute(sql,(stamp(req),chat[0]))
            names=cursor.fetchall()
            for name in names:
                sql="select cat,sum(dtime) from timee where "+memo[req][0]+"=%s and chid=%s and name=%s GROUP BY cat,chid,name ;"
                cursor.execute(sql,(stamp(req),chat[0],name[0]))
                res=cursor.fetchall()
                print(name[0])
                response=''
                for r in res:
                    response=response+r[0]+': '+graph(req,int(r[1]))+' '+timecelc(r[1])+'\n'
                print(response)
                bot.sendMessage(chat[0], '~ ~ '+name[0]+memo[req][1]+' ~ ~\n'+response)
                time.sleep(10)
    conn.close()
def doom():
    conn = pymysql.connect(host=key['host'],user=key['user'],password=key['pass'],db=key['db'],charset='utf8')
    with conn.cursor() as cursor:
        sql='update timee set etime =%s where etime=22;'
        cursor.execute(sql,stamp('e'))
        conn.commit()
        sql='update timee set dtime=etime-stime where dtime=22;'
        cursor.execute(sql)
        conn.commit()
        
    conn.close()    
def cal():    
    if int(n.strftime('%m'))==12 and int(n.strftime('%m'))==lastday:
        req='y'
    elif int(n.strftime('%m'))==lastday:
        req='m'
    elif w == 6 :
        req='w'
    else:
        req='DoNotRun'
    Report(req)
    if w <6:
        Report('d')
        
print(wk[w])
doom()
cal()