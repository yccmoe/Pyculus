import sys
import asyncio
import random
import telepot
import telepot.aio

from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

import re

from lib_ import key_
from lib_ import b2ta
from lib_ import brain

message_with_inline_keyboard = None
brain = {}

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

        if letter['chat'] == 'ee' or letter['chat']=='i':
            global message_with_inline_keyboard
            global brain
            if letter['chat']=='ee':
                markup = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text='aaa', callback_data='aaa'),dict(text='bbb', callback_data='bbb')],
                    [dict(text='ccc', callback_data='ccc'),dict(text='ddd', callback_data='ddd')],
                ])
                letter['intent'] = 'ABC버튼누르기' 
                cat='normal'
                hash = hsh(letter)
                brain[hash] = {'cat':cat, 'data':'이제부터 버튼을 눌러볼게요...!\n'}
                print(brain)
                message_with_inline_keyboard = await bot.sendMessage(chat_id, '이제부터 버튼을 눌러볼게요...!',
                                                                     reply_markup=markup)
               
                print(brain)
            if letter['chat'] == 'i':
                markup = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text='Telegram URL', url='https://core.telegram.org/')],
                    [InlineKeyboardButton(text='Callback - show notification', callback_data='notification')],
                    [dict(text='Callback - show alert', callback_data='alert')],
                    [InlineKeyboardButton(text='Callback - edit message', callback_data='edit')],
                    [dict(text='Switch to using bot inline', switch_inline_query='initial query')],
                ])

                
                message_with_inline_keyboard = await bot.sendMessage(chat_id, 'Inline keyboard with various buttons',
                                                                     reply_markup=markup)                                                                 
        if letter['chat'] == 'h':
            markup = ReplyKeyboardRemove()
            await bot.sendMessage(chat_id, 'Hide custom keyboard', reply_markup=markup)
        if letter['chat'] == 'f':
            markup = ForceReply()
            await bot.sendMessage(chat_id, 'Force reply', reply_markup=markup)


        if letter['chat'] == '/ㅎㅇ':
            await bot.sendMessage(chat_id, 'Res...')
    return 'okay'


async def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Callback query:', query_id, from_id, data)
    print(msg)
    letter={'name':msg['from']['first_name'], 'chid':from_id, 'type':'callback', 'chat':''}
    global brain
    if data == 'notification':
        await bot.answerCallbackQuery(query_id, text='Notification at top of screen')
    elif data == 'alert':
        await bot.answerCallbackQuery(query_id, text='Alert!', show_alert=True)
    elif data == 'edit':
        global message_with_inline_keyboard

        if message_with_inline_keyboard:
            msg_idf = telepot.message_identifier(message_with_inline_keyboard)
            await bot.editMessageText(msg_idf, 'NEW MESSAGE HERE!!!!!')
        else:
            await bot.answerCallbackQuery(query_id, text='No previous message to edit')
    
    h = hsh(letter)+'ABC버튼누르기'
    if h in list(brain.keys()):
        print('ee')
        if data=='aaa':
            markup = InlineKeyboardMarkup(inline_keyboard=[
                        [dict(text='aaa', callback_data='aaa'),dict(text='bbb', callback_data='bbb')],
                        [dict(text='ccc', callback_data='ccc'),dict(text='ddd', callback_data='ddd')],
                    ])
            msg_idf = telepot.message_identifier(message_with_inline_keyboard)
            brain[h]['letter'] = 
            await bot.editMessageText(msg_idf, brain, reply_markup=markup)
        elif data=='bbb':
            markup = InlineKeyboardMarkup(inline_keyboard=[
                        [dict(text='aaa', callback_data='aaa'),dict(text='bbb', callback_data='bbb')],
                        [dict(text='ccc', callback_data='ccc'),dict(text='ddd', callback_data='ddd')],
                    ])
            msg_idf = telepot.message_identifier(message_with_inline_keyboard)
            await bot.editMessageText(msg_idf, brain, reply_markup=markup)        
        elif data=='ccc':
            markup = InlineKeyboardMarkup(inline_keyboard=[
                        [dict(text='aaa', callback_data='aaa'),dict(text='bbb', callback_data='bbb')],
                        [dict(text='ccc', callback_data='ccc'),dict(text='ddd', callback_data='ddd')],
                    ])
            msg_idf = telepot.message_identifier(message_with_inline_keyboard)
            await bot.editMessageText(msg_idf, brain, reply_markup=markup)
        elif data=='ddd':
            markup = InlineKeyboardMarkup(inline_keyboard=[
                        [dict(text='aaa', callback_data='aaa'),dict(text='bbb', callback_data='bbb')],
                        [dict(text='ccc', callback_data='ccc'),dict(text='ddd', callback_data='ddd')],
                    ])
            msg_idf = telepot.message_identifier(message_with_inline_keyboard)
            await bot.editMessageText(msg_idf, brain, reply_markup=markup)                

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

def message_thinking(chat):
    return 'okay'
    
def unq(old):
    new=[]
    for i in range(len(old)):
        new.append(frozenset(old[i].items()))
    new=list(set(new))
    old=[]
    for i in range(len(new)):
        old.append(dict(new[i]))
    return old

def hsh(letter):
    try:res = str(letter['chid'])+str(letter['name'])+str(letter['intent'])
    except:res=str(letter['chid'])+str(letter['name'])
    return res

TOKEN = key_.kids('beta')

bot = telepot.aio.Bot(TOKEN)


answerer = telepot.aio.helper.Answerer(bot)

loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot, {'chat': on_chat_message,
                                   'callback_query': on_callback_query,
                                   'inline_query': on_inline_query,
                                   'chosen_inline_result': on_chosen_inline_result}).run_forever())
print('<--- --- Listening ... --- --->')
loop.run_forever()

