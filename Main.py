import sys
import asyncio
import random
import telepot
import telepot.aio

from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

from lib_ import key_
from lib_ import core
from lib_ import cust
from lib_ import magic
from lib_ import board
import re

message_with_inline_keyboard = None


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

        A = re.compile('^[0-9]+분 타이머$')
        B = re.compile('^/pull +[0-9]+$')


        if letter['chid'] == mew:
            if letter['chat'].find('불')==0:
                await cust.smarthome(bot, letter)

            if letter['chat'] == 'c':
                markup = ReplyKeyboardMarkup(keyboard=[
                    ['Plain text', KeyboardButton(text='Text only')],
                    [dict(text='Phone', request_contact=True), KeyboardButton(text='Location', request_location=True)],
                ])
                await bot.sendMessage(chat_id, 'Custom keyboard with various buttons', reply_markup=markup)

            if letter['chat'] == 'ㅎㅇ':
                markup = ReplyKeyboardMarkup(keyboard=[
                    [dict(text='Callback - show alert', callback_data='alert')],
                    [dict(text='Phone', request_contact=True), KeyboardButton(text='Location', request_location=True)],
                ])
                await bot.sendMessage(chat_id, 'Custom keyboard with various buttons', reply_markup=markup)
            
            
            if letter['chat'] == 'i':
                markup = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text='Telegram URL', url='https://core.telegram.org/')],
                    [InlineKeyboardButton(text='Callback - show notification', callback_data='notification')],
                    [dict(text='Callback - show alert', callback_data='alert')],
                    [InlineKeyboardButton(text='Callback - edit message', callback_data='edit')],
                    [dict(text='Switch to using bot inline', switch_inline_query='initial query')],
                ])

                global message_with_inline_keyboard
                message_with_inline_keyboard = await bot.sendMessage(chat_id, 'Inline keyboard with various buttons',
                                                                     reply_markup=markup)
            if letter['chat'] == 'h':
                markup = ReplyKeyboardRemove()
                await bot.sendMessage(chat_id, 'Hide custom keyboard', reply_markup=markup)
            if letter['chat'] == 'f':
                markup = ForceReply()
                await bot.sendMessage(chat_id, 'Force reply', reply_markup=markup)


        if letter['chat'] == '/ㅎㅇ':
            await magic.ping(bot,letter, TOKEN)
        elif letter['chat'] == '/하이':
            await magic.ping_full(bot,letter, TOKEN)
        elif letter['chat'] == '/채팅방':
            await bot.sendMessage(chat_id, chat_id)
        elif letter['chat'] == '/주사위':
            await core.dice(bot, letter)
        elif letter['chat'] == '/15':
            await core.fif_gui(bot, letter)

        elif A.match(letter['chat']):
            await core.hglass(bot, letter)
        elif B.match(letter['chat']):
            await core.dbm_pull(bot, letter)
        elif letter['chat'] == '>>' or letter['chat']=='»':
            await core.papago_help(bot, letter, naver)
        elif letter['chat'].find('>>') ==0 or letter['chat'].find('»') ==0 :
            await core.papago(bot, letter, naver)
        elif letter['chat'].find('=') ==0 :
            await core.celc(bot, letter, UAkey)

        elif letter['chat'].count('쐐기') == 1 and letter['chat'].count('뭐') == 1:
            await core.keystone(bot, letter)


        elif letter['chat'].find('$') ==0 :
            await board.bbs(bot, letter, bbskey)
    return 'okay'


async def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Callback query:', query_id, from_id, data)

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

TOKEN = key_.kids('jv')

UAkey = key_.kids('UAkey')
naver = key_.kids('naver')
phgs = key_.kids('phgs')
bbskey = key_.kids('bbs')
bot = telepot.aio.Bot(TOKEN)

me=key_.adds ('me')
mew=key_.adds ('mew')
ph=key_.adds ('pharmacy')



answerer = telepot.aio.helper.Answerer(bot)

loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot, {'chat': on_chat_message,
                                   'callback_query': on_callback_query,
                                   'inline_query': on_inline_query,
                                   'chosen_inline_result': on_chosen_inline_result}).run_forever())
print('<--- --- Listening ... --- --->')
loop.run_forever()

