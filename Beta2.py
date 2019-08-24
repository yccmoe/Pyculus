import sys
import asyncio
import random
import telepot
import telepot.aio

from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
from telepot.aio.delegate import (
    per_chat_id, per_callback_query_origin, create_open, pave_event_space)
import re

from lib_ import key_
from lib_ import b2ta
from lib_ import magic
from lib_ import menupann



class Emperor(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Emperor, self).__init__(*args,**kwargs)
        
    async def on_chat_message(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print('Chat:', content_type, chat_type, chat_id)
        print(msg)
        letter={'name':'', 'chid':'', 'type':'', 'chat':''}
        if content_type != 'text':
            return
        elif content_type == 'text':
            letter['name'] = msg['from']['first_name']
            letter['chid'] = chat_id
            letter['type'] = 'text'
            letter['chat'] = msg['text']


            if letter['chat'].find('불')==0:
                await cust.smarthome(bot, letter)

            if letter['chat'] == 'c':
                markup = ReplyKeyboardMarkup(keyboard=[
                    ['Plain text', KeyboardButton(text='Text only')],
                    [dict(text='Phone', request_contact=True), KeyboardButton(text='Location', request_location=True)],
                ])
                await bot.sendMessage(chat_id, 'Custom keyboard with various buttons', reply_markup=markup)

            if letter['chat']=='ee':
                    await menupann.Start(bot, letter)
                    #barin[hash]=data
                    
            if letter['chat'] == 'h':
                markup = ReplyKeyboardRemove()
                await bot.sendMessage(chat_id, 'Hide custom keyboard', reply_markup=markup)
            if letter['chat'] == 'f':
                markup = ForceReply()
                await bot.sendMessage(chat_id, 'Force reply', reply_markup=markup)


            if letter['chat'] == '/ㅎㅇ':
                await self.sender.sendMessage(msg)
        self.close()

class Slave(telepot.aio.helper.CallbackQueryOriginHandler):
    def __init__(self, *args, **kwargs):
        super(Slave, self).__init__(*args, **kwargs)

    async def on_callback_query(msg):
        query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
        print('Callback query:', query_id, from_id, data)
        print(msg)
        letter={'name':msg['from']['first_name'], 'chid':from_id, 'type':'callback', 'chat':''}
        msg_idf = telepot.message_identifier(message_with_inline_keyboard)
        print(msg_idf)
        

        if data == 'notification':
            await bot.answerCallbackQuery(query_id, text='Notification at top of screen')
        elif data == 'alert':
            await bot.answerCallbackQuery(query_id, text='Alert!', show_alert=True)
        elif data == 'edit':
            if message_with_inline_keyboard:
                msg_idf = telepot.message_identifier(message_with_inline_keyboard)
                await bot.editMessageText(msg_idf, 'NEW MESSAGE HERE!!!!!')
            else:
                await bot.answerCallbackQuery(query_id, text='No previous message to edit')

        if data.find('menupann.')==0:
            if data in 'QuickAll' :
                message_with_inline_keyboard, hash, brain = await menupann.QuickAll(bot, letter,msg_idf)
            elif data in 'Allow' :
                message_with_inline_keyboard, hash, brain = await menupann.Go2Allow(bot, letter,msg_idf)
            elif data in 'Exit' :
                message_with_inline_keyboard, hash, brain = await menupann.Exit(bot, letter,msg_idf)
            
        

    def on_inline_query(msg):
        def compute():
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            print('Computing for: %s' % query_string)

            articles = [InlineQueryResultArticle(
                id='abcde', title='Telegram',
                input_message_content=InputTextMessageContent(message_text='Telegram is a messaging app')),
                dict(type='article',
                     id='fghij', title='Google', input_message_content=dict(message_text='Google is a search engine'))]

            photo1_url = 'https://core.telegram.org/file/811140934/1/tbDSLHSaijc/fdcc7b6d5fb3354adf'
            photo2_url = 'https://www.telegram.org/img/t_logo.png'
            photos = [InlineQueryResultPhoto(
                id='12345', photo_url=photo1_url, thumb_url=photo1_url),
                dict(type='photo',
                     id='67890', photo_url=photo2_url, thumb_url=photo2_url)]

            result_type = query_string[-1:].lower()

            if result_type == 'a':
                return articles
            elif result_type == 'p':
                return photos
            else:
                results = articles if random.randint(0, 1) else photos
                if result_type == 'b':
                    return dict(results=results, switch_pm_text='Back to Bot',
                                switch_pm_parameter='Optional_start_parameter')
                else:
                    return dict(results=results)

        answerer.answer(msg, compute)


    def on_chosen_inline_result(msg):
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        print('Chosen Inline Result:', result_id, from_id, query_string)

 

TOKEN = key_.kids('beta')

bot = telepot.aio.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, Emperor, timeout=3),
    pave_event_space()(
        per_callback_query_origin(), create_open, Slave, timeout=10),
])



loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot).run_forever())
print('<--- --- Listening ... --- --->')
loop.run_forever()

