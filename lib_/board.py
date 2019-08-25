import asyncio
import telepot
import telepot.aio
import datetime
import re
import pymysql
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

message_with_inline_keyboard = None

if __name__ == '__main__':
    print('이 모듈을 직접 실행하셨군요.')


#bot = telepot.aio.Bot('747837106:AAHXUZT5NMnkS5JWM5QbegwnyNiqYC285HA')
#letter = {'name':'준모', 'chid':'288115423', 'type':'text', 'chat':'$2 $열기$'}




help='''메모장 - 겸 Issue Tracker
$$ : 도움말
$ : 글 목록 보기
$ <--새 글--> : 새 글 작성
$1 <--새 댓글--> : 새 댓글 달기
$2 <--변경할 제목--> $수정$ : 제목 변경
$3 $닫기$ : 4번 글 닫기 (더이상 댓글 달 수 없음)
$4 $열기$ : 5번 글 다시 열기.
'''




async def template(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    await bot.sendMessage(chid, '- - - some text - - -')
    await asyncio.sleep(1)
    return 'okay'

def epoch():
    n=datetime.datetime.now()+datetime.timedelta(hours=9)
    return n.strftime('%s')

def ago(time):
    n=datetime.datetime.now()+datetime.timedelta(hours=9)-datetime.timedelta(seconds=time)
    e=int(n.strftime('%s'))
    if e < 100:
        return str(n.strftime('%s'))+' 초 전'
    elif e < 3600:
        return str(n.strftime('%M'))+' 분 전'
    elif e < 86400:
        return str(n.strftime('%H'))+' 시간 전'
    else:
        return str(n.strftime('%d'))+' 일 전'



async def bbs(letter, key):
    name, chid, chat = letter['name'],letter['chid'],letter['chat']
    hst, usr, pss, dbb  = key['host'], key['user'], key['pass'], key['db']
    re_help=re.compile('^\${2}$')
    re_show=re.compile('^\${1}$')
    re_rename=re.compile('^\${1}[0-9]+\s{1}.*\$수정\$$')
    re_close=re.compile('^\${1}[0-9]+\s{1}.*\$닫기\$$')
    re_open=re.compile('^\${1}.*\$열기\$$')
    re_comment=re.compile('^\${1}[0-9]+\s{1}.')
    re_read=re.compile('^\${1}[0-9]+$')
    re_new=re.compile('^\${1}\s.*$')

    conn = pymysql.connect(host=hst, user=usr, password=pss, db=dbb, charset='utf8' )
    markup=None
    if re_help.match(chat):
        return help,markup
    elif re_show.match(chat):
        print('show')
    
        with conn.cursor() as cursor:
            sql = 'select distinct title, status from bbs where chat_id='+str(chid)+ ';'
            cursor.execute(sql)
            rs = cursor.fetchall()
            res=[]
            for i in (range(len(rs))):
                if rs[i][1]=='c': tale='-닫힘'
                else:tale=''
                res=res+[dict(text='#'+str(i+1)+' '+rs[i][0]+tale,  callback_data='bbs♡open♡$'+str(i+1)+'♡'+str(chid))]
        conn.close()
        print(res)
        markup = InlineKeyboardMarkup(inline_keyboard=[ [i] for i in res])
        res = '글 목록.'
#    except:
 #           markup=None
  #          res='새 글을 작성해 보세요.'
        return res, markup
    elif re_rename.match(chat):
        print('rename')
        qs = re.findall('^\$[0-9]',chat)
        q=int(qs[0].replace('$',''))
        text = re.sub('^\$[0-9]\s{1}','',chat)
        text = text.replace('$수정$','')
        try:
            with conn.cursor() as cursor:
                sql = 'select distinct title from bbs where chat_id='+str(chid)+ ';'
                cursor.execute(sql)
                rs = cursor.fetchall()
                query = rs[q-1][0]
                sql = 'select title, status from bbs where chat_id="'+str(chid)+'" and title="'+query+'";'
                cursor.execute(sql)
                rs = cursor.fetchall()
                if rs[0][1]=='o':
                    print(rs)
                    old_title = rs[0][0]
                    print(old_title)
                    new_title = text
                    print(new_title)
                    sql = 'update bbs set title = %s where title =%s and chat_id=%s'
                    cursor.execute(sql,(new_title, old_title, chid))
                    sql = "INSERT INTO bbs (chat_id, user, title, text, time) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql,(chid, name, new_title, text+' - 수정', epoch()))
                    conn.commit()
                    return 'okay', markup
                else:
                    return '잠긴 글 입니다.\n$$:도움말 출력', markup
            conn.close()
        except:
            return '#'+str(q)+' 게시물이 없습니다.', markup
    elif re_close.match(chat):
        print('close')
        qs = re.findall('^\$[0-9]',chat)
        q=int(qs[0].replace('$',''))
        text = re.sub('^\$[0-9]\s{1}','',chat)
        text = text.replace('$닫기$','')
        try:
            with conn.cursor() as cursor:
                sql = 'select distinct title from bbs where chat_id='+str(chid)+ ';'
                cursor.execute(sql)
                rs = cursor.fetchall()
                query = rs[q-1][0]
                sql = 'select title, status from bbs where chat_id="'+str(chid)+'" and title="'+query+'";'
                cursor.execute(sql)
                rs = cursor.fetchall()
                if rs[0][1]=='o':
                    print(rs)
                    title = rs[0][0]
                    status = 'c'
                    sql = 'update bbs set status = %s where title =%s and chat_id=%s'
                    cursor.execute(sql,(status, title, chid))
                    sql = "INSERT INTO bbs (chat_id, user, title, text, time, status) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql,(chid, name, title, title+' - 닫음', epoch(), 'c'))
                    conn.commit()
                    return 'okay', markup
                else:
                    return '잠긴 글 입니다.\n$$:도움말 출력', markup
            conn.close()
        except:
            return '#'+str(q)+' 게시물이 없습니다.', markup
    elif re_open.match(chat):
        print('reopen')
        qs = re.findall('^\$[0-9]',chat)
        q=int(qs[0].replace('$',''))
        text = re.sub('^\$[0-9]\s{1}','',chat)
        text = text.replace('$열기$','')
        try:
            with conn.cursor() as cursor:
                sql = 'select distinct title from bbs where chat_id='+str(chid)+ ';'
                cursor.execute(sql)
                rs = cursor.fetchall()
                query = rs[q-1][0]
                sql = 'select title, status from bbs where chat_id="'+str(chid)+'" and title="'+query+'";'
                cursor.execute(sql)
                rs = cursor.fetchall()
                if rs[0][1]=='c':
                    print(rs)
                    title = rs[0][0]
                    status = 'o'
                    sql = 'update bbs set status = %s where title =%s and chat_id=%s'
                    cursor.execute(sql,(status, title, chid))
                    sql = "INSERT INTO bbs (chat_id, user, title, text, time) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql,(chid, name, title, title+' - 다시 열음', epoch()))
                    conn.commit()
                    return 'okay', markup
                else:
                    return '이미 열려 있습니다.\n$$:도움말 출력', markup
            conn.close()
        except:
            return '#'+str(q)+' 게시물이 없습니다.', markup
    elif re_comment.match(chat):
        print('comment')
        qs = re.findall('^\$[0-9]',chat)
        q=int(qs[0].replace('$',''))
        text = re.sub('^\$[0-9]\s{1}','',chat)
        try:
            with conn.cursor() as cursor:
                sql = 'select distinct title from bbs where chat_id='+str(chid)+ ';'
                cursor.execute(sql)
                rs = cursor.fetchall()
                query = rs[q-1][0]
                sql = 'select title, status from bbs where chat_id="'+str(chid)+'" and title="'+query+'";'
                cursor.execute(sql)
                rs = cursor.fetchall()
                if rs[0][1]=='o':
                    print(rs)
                    title = rs[0][0]
                    sql = "INSERT INTO bbs (chat_id, user, title, text, time) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql,(chid, name, title, text, epoch()))
                    conn.commit()
                    return 'okay', markup
                else:
                    return '잠긴 글 입니다.\n$$:도움말 출력', markup
            conn.close()
        except:
            return '#'+str(q)+' 게시물이 없습니다.', markup
    elif re_read.match(chat) or chat.find('CallbackOpen')==0:
        q = chat.replace('$','')
        q = q.replace('CallbackOpen','')
        q= int(q)
        try:
            print('read: '+str(q))
            with conn.cursor() as cursor:
                sql = 'select distinct title from bbs where chat_id='+str(chid)+ ';'
                cursor.execute(sql)
                rs = cursor.fetchall()
                query = rs[q-1][0]
                sql = 'select user, time, text from bbs where chat_id="'+str(chid)+'" and title="'+query+'";'
                cursor.execute(sql)
                rs = cursor.fetchall()
                res=''
                for i in (range(len(rs))):
                    if rs[i][1]=='c': tale='-닫힘'
                    else:tale=''
                    res=res+'#'+str(i+1)+' '+rs[i][2]+'\n'+ago(rs[i][1])+', '+rs[i][0]+'\n\n'
            conn.close()
            return res, markup
        except:
            return '#'+str(q)+' 게시물이 없습니다.', markup
    elif re_new.match(chat):
        print ('new: '+chat)
        with conn.cursor() as cursor:
            title = chat.replace('$ ','',1)
            text = title+' - 열림'
            sql = "INSERT INTO bbs (chat_id, user, title, text, time) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql,(chid, name, title, text, epoch()))
            conn.commit()
        conn.close()
        return title+': okay', markup
    else:
        return '$$ 로 도움말 보기', markup
    return 'okay!', markup







