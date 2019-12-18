#-*- coding:utf-8 -*-
import json
import requests
import datetime
import telepot
import asyncio
if __name__ == '__main__':
    print('이 모듈을 직접 실행하셨군요.')

async def wttr(bot,letter):
    name, chid, chat = letter['name'], letter['chid'], letter['chat']
    loc='서울'
    if name=='지웅':loc='천안'
    if '천안' in chat : loc='천안'
    if '서울' in chat : loc='서울'
    if '수원' in chat : loc='수원'
    if '금정' in chat : loc='금정역'
    if '안양' in chat : loc='안양역'
    params = (('lang', 'ko'),('format', 'j1'),)
    if '내일' in chat: 
        no=datetime.datetime.now()+datetime.timedelta(hours=35)
        n=no.strftime('%Y-%m-%d')
        displayn='내일 ('+no.strftime('%d')+'일)\n'
        r= requests.get('http://wttr.in/'+loc, params=params).json()
        vs = int(r['weather'][1]['hourly'][4]['tempC']) -int(r['weather'][0]['hourly'][4]['tempC'])
        if vs==0: say='오늘 낮이랑 같아요.'
        elif vs>0: say='오늘 낮보다 '+str(vs)+'° 높아요.'
        else: say='오늘 낮보다 '+str(vs)+'° 낮아요.'
        await bot.sendMessage(chid, loc+'아침: '+r['weather'][1]['hourly'][2]['tempC']+'°, '+r['weather'][1]['hourly'][2]['lang_ko'][0]['value']+'\n낮: '+r['weather'][1]['hourly'][4]['tempC']+'°, '+r['weather'][1]['hourly'][4]['lang_ko'][0]['value']+'\n밤: '+r['weather'][1]['hourly'][7]['tempC']+'°, '+r['weather'][1]['hourly'][7]['lang_ko'][0]['value']+'\n'+say)
        return 'okay'
    else:
        r= requests.get('http://wttr.in/'+loc, params=params).json()
        await bot.sendMessage(chid, loc+': '+str(r['current_condition'][0]['lang_ko'][0]['value']+', '+r['current_condition'][0]['temp_C']+'°'))
        return 'okay'