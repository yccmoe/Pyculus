#-*- coding:utf-8 -*-

import sys
import io
import asyncio
import random
from telepot import glance, message_identifier
import telepot.aio

from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
from telepot.aio.delegate import per_chat_id, per_callback_query_origin, create_open, pave_event_space, include_callback_query_chat_id

import re
import time
import datetime

from lib_ import key_
from lib_ import magic, menupann, core, board, remote, weather, jjs, ytube

brain=''
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class Unbuffered(object):
   def __init__(self, stream):
     self.stream = stream
   def write(self, data):
     self.stream.write(data)
     self.stream.flush()
   def writelines(self, datas):
     self.stream.writelines(datas)
     self.stream.flush()
   def __getattr__(self, attr):
     return getattr(self.stream, attr)

class Global(object):
    Timeout= None

class Emperor(telepot.aio.helper.ChatHandler, Global):
    def __init__(self, *args, **kwargs):
        super(Emperor, self).__init__(*args,**kwargs)






    async def on_chat_message(self, msg):
        content_type, chat_type, chid = glance(msg)
        chat, name = msg['text'], msg['from']['first_name']
        letter={'name':'', 'chid':'', 'type':'', 'chat':''}
        if content_type != 'text': return
        elif content_type == 'text':
            letter['name'] = name
            letter['chid'] = chid
            letter['type'] = content_type
            letter['chat'] = chat
        print(chat)
        A = re.compile('^[0-9]+분 타이머$')
        B = re.compile('^/pull +[0-9]+$')
        if chat == '/ㅎㅇ': await self.sender.sendMessage(name+'님 '+magic.ping())
        if chat == '/채팅방': await self.sender.sendMessage(chid)
        if chat == '/주사위':await core.dice(bot, letter)
        if chat.find('!') == 0 : await ytube.down(bot,letter)
        if chat =='/15': await self.sender.sendMessage(await core.fif_gui(), reply_markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='불만 있어요?', callback_data='fif_gui')],]))
        ##if chat.count('ㅋ')>5: await self.sender.sendMessage(core.funnybell(bot,letter))
        if chat.find('=') == 0 : await self.sender.sendMessage(await core.celc(chat, UAkey), parse_mode='HTML')
        if chat.find('>') == 0 or chat.find('»') == 0  : await self.sender.sendMessage(await core.papago(chat, naver))
        if chat.find('$') == 0 :
            a,b=await board.bbs(letter,bbskey)
            await self.sender.sendMessage(a,reply_markup=b)
        ## $, >, =, /주사위, /15, 고독한공부방이라던가,,,,,,
        if chat == '####뭐먹지?' or chat == '####모먹지?':
            Global.Timeout= None
            sent = await self.sender.sendMessage('배가 고픈 분위기군요..', reply_markup=menupann.start())
            await self.edittext(sent, 5, '배가 고픈 분위기군요..')
            return 'okay'
        if A.match(chat):
            minn, keyboard = await core.hglassStart(chat)
            await self.sender.sendMessage(minn, reply_markup=keyboard)
        if chid == ph or chid == mew:
            if chat == 'ㅎㅇ' : await self.sender.sendMessage(remote.greeting(),reply_markup=remote.butten())
        if chid == mew and chat == '불' :
            await self.sender.sendMessage(remote.greeting(),reply_markup=remote.privhomebttn())
        if chat.count('춥나?')==1 or chat.count('덥나?')==1:
            await weather.wttr(bot,letter)
        if chat.find('/누구 ')==0:
            await jjs.wow(bot,letter)    

    async def edittext(self, sent, s, letter):
        self._keyboard_msg_ident = message_identifier(sent)
        self.txtedit = telepot.aio.helper.Editor(self.bot, self._keyboard_msg_ident)
        await asyncio.sleep(s)
        if Global.Timeout == None:
            print(Global.Timeout)
            await self.txtedit.editMessageText(letter)
        else:
            return 'okay'

class Slave(telepot.aio.helper.CallbackQueryOriginHandler, Global):
    def __init__(self, *args, **kwargs):
        super(Slave, self).__init__(*args, **kwargs)
        self._everyTag=None
        self._allowTag = None
        self._denyTag = None
        self._addTag = None

    async def on_callback_query(self, msg):

        query_id, from_id, query_data = glance(msg, flavor='callback_query')
        letter={'name':msg['from']['first_name'], 'chid':msg['message']['chat']['id'], 'type':'','orgn':msg['message']['text']}
        
        q = query_data.split('♡')
        if q[0] == 'menupann':
            Global.Timeout='working...'
            print(Global.Timeout)
            if q[1] == 'Exit': await self.editor.editMessageText('취소되었습니다.')
            if q[1] == 'allowTag':
                if self._everyTag == None:
                    self._everyTag=menupann.tags(query_id)
                    await self.editor.editMessageText('배가 고픈 분위기군요..\n포함될 태그를 알려주세요.\n'+str(self._allowTag), reply_markup=menupann.MarkupCreate(self._everyTag,'first_allow'))
                if len(q)==3:
                    if q[2] =='ALL': self._allowTag= None
                    else:
                        if self._allowTag==None:self._allowTag=[]
                        self._allowTag.append(q[2])
                        self._everyTag.remove(q[2])
                        await self.editor.editMessageText('배가 고픈 분위기군요..\n포함될 태그를 알려주세요.\n'+str(self._allowTag), reply_markup=menupann.MarkupCreate(self._everyTag,'allow'))
            if q[1] == 'denyTag':
                if len(q)==3:
                    if self._denyTag==None:self._denyTag=[]
                    self._denyTag.append(q[2])
                    self._everyTag.remove(q[2])
                await self.editor.editMessageText('배가 고픈 분위기군요..\n포함될 태그를 알려주세요.\n'+str(self._allowTag)+'\n제외될 태그를 알려주세요.\n'+str(self._denyTag), reply_markup=menupann.MarkupCreate(self._everyTag,'deny'))
            if q[1] == 'Run': await self.editor.editMessageText('오늘의 메뉴는 '+str(menupann.Pick(from_id,self._allowTag,self._denyTag))+'입니다!',reply_markup=menupann.MarkupCreate(self._everyTag,'show'))
            if q[1] == 'showList': await self.editor.editMessageText('나올 수 있었던곳들...\n'+menupann.Picklist(from_id,self._allowTag,self._denyTag))
        if q[0] == 'hglass':
            w, target= q[1], q[2]
            process=22
            await self.editor.editMessageText(str(q[1])+'분\n→시작합니다!')
            while float(process)>0:
                w, clock,process  = await core.hglass(target)
                await self.editor.editMessageText(str(q[1])+'분\n→'+clock)
            print(w)
            w, clock, process = await core.hglass(target)
            await self.editor.editMessageText(str(q[1])+'분\n→'+clock+' 땡!!')
        if q[0] == 'fif_gui': await self.editor.editMessageText(await core.fif_gui(), reply_markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='아직 불만 있어요?', callback_data='fif_gui')]]))
        if q[0] == 'bbs':
            if q[1] =='open':
                letter['chat']=q[2]
                a,b=await board.bbs(letter,bbskey)
                await self.editor.editMessageText(a, reply_markup =b )
        if q[0]=='remote':
            if q[1]=='dest': mk = remote.distAllbutten()
            elif q[1]=='destreal' or q[1]=='exit': mk=None
            else: mk = remote.butten()
            o=letter['orgn']
            o=o+'\n'+remote.press(letter['name'],q[1],iftttkey)
            await self.editor.editMessageText(o,reply_markup=mk)
        if q[0]=='premote':
            mk = remote.privhomebttn()
            o=letter['orgn']
            o=o+'\n'+remote.privhomedesc(letter['name'],q[1],iftttkey)
            await self.editor.editMessageText(o,reply_markup=mk)

        print(q)




UAkey = key_.kids('UAkey')
naver = key_.kids('naver')
phgs = key_.kids('phgs')
bbskey = key_.kids('bbs')
iftttkey=key_.kids('ifttt')

me=key_.adds ('me')
mew=key_.adds ('mew')
ph=key_.adds ('pharmacy')



bot = telepot.aio.DelegatorBot(key_.kids('jv'), [
    pave_event_space()(
            per_chat_id(), create_open, Emperor, timeout=3),
    pave_event_space()(
            per_callback_query_origin(), create_open, Slave, timeout=300),
    ])


sys.stdout=Unbuffered(sys.stdout)
loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot).run_forever())
print('<--- --- Listening ... --- --->')
loop.run_forever()

