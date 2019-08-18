# -*- coding: utf-8 -*-
import urllib.request

message_with_inline_keyboard = None

if __name__ == '__main__':
    print('이 모듈을 직접 실행하셨군요.')

async def smarthome(bot, letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']

    base='https://maker.ifttt.com/trigger/'
    tale='/with/key/duGL1OLFeBQQmcQz20_m_y'

    if '불' in chat:
        dv = 'home_bulb01'
        dt = '스탠드 '
    else: return 'pass'

    if '켜' in chat:
        sw='on'
        st='켜집니다...'
    elif '꺼' in chat:
        sw='off'
        st='꺼집니다...'
    else:
        sw='tgg'
        st='토글 합니다!'
    url = base+dv+'_'+sw+tale
    urllib.request.urlopen(url)
    await bot.sendMessage(chid, dt+st)
    return'okay!'