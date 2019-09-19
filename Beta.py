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
from lib_ import magic, menupann, core, board, remote, studylog

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

        if chat == '/ㅎㅇ': await self.sender.sendMessage(name+'@'+str(chid)+'님 '+magic.ping())
        if chat == 'ㅎㅇ' : 
            await self.sender.sendMessage(name+'님 '+studylog.greeting(),reply_markup=studylog.butten(letter))
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
        print(msg)
        
        letter={'name':msg['from']['first_name'], 'chid':msg['message']['chat']['id'], 'type':'', 'orgn':msg['message']['text']}
        
        q = query_data.split('♡')
        if q[0]=='remote':
            if q[1]=='dest': mk = remote.distAllbutten()
            elif q[1]=='destreal' or q[1]=='exit': mk=None
            else: mk = remote.butten()
            o=letter['orgn']
            o=o+'\n'+remote.press(letter['name'],q[1])
            await self.editor.editMessageText(o,reply_markup=mk)
        print(q)




UAkey = key_.kids('UAkey')
naver = key_.kids('naver')
phgs = key_.kids('phgs')
bbskey = key_.kids('bbs')


me=key_.adds ('me')
mew=key_.adds ('mew')
ph=key_.adds ('pharmacy')



bot = telepot.aio.DelegatorBot(key_.kids('beta'), [
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

