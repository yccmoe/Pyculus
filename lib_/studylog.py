import datetime
import random
import urllib.request
import sys
import io
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

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

def greeting():
    his=('안녕하새요!','안녕하세요!','반갑습니다!','오늘도 멋져요!','무엇을 도와드릴까요?','부르셨나요?')
    return random.choice(his)
def butten(letter):
    name = letter['name']

    if name == '준모':
        res=[
        [{'text':'국어', 'callback_data': 'studylog♡국어'},{'text':'영어', 'callback_data': 'studylog♡영어'},{'text':'국사', 'callback_data': 'studylog♡국사'}],
        [{'text':'회계', 'callback_data': 'studylog♡회계'},{'text':'세법', 'callback_data': 'remote♡세법'}],
        [{'text':'코딩', 'callback_data': 'studylog♡코딩'},{'text':'핫산', 'callback_data': 'studylog♡핫산'},{'text':'운동', 'callback_data': 'studylog♡운동'},{'text':'휴식', 'callback_data': 'studylog♡휴식'}],
    ]
    elif name == '승화':
        res=[
        [{'text':'국어', 'callback_data': 'studylog♡국어'},{'text':'영어', 'callback_data': 'studylog♡영어'},{'text':'국사', 'callback_data': 'studylog♡국사'}],
        [{'text':'행정법', 'callback_data': 'studylog♡행법'},{'text':'행정학', 'callback_data': 'remote♡행학'}],
        [{'text':'운동', 'callback_data': 'studylog♡운동'},{'text':'게임', 'callback_data': 'studylog♡게임'},{'text':'휴식', 'callback_data': 'studylog♡휴식'}],
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=res)
    return keyboard
    