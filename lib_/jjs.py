# -*- coding:utf-8 -*-
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import sys
import io
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

q = '잠행'
q=quote(q)
url = 'https://worldofwarcraft.com/ko-kr/search/character?q='+q
print(url)
INFO=[]
lvls=[]
svrs=[]
aohs=[]
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
slave_lvl = soup.select('body > div.body > div > div.Pane.Pane--full.Pane--dirtDark > div.Pane-content > div > div.Pane-content > div > div.SortTable.SortTable--stretch > div.SortTable-body > a > div.SortTable-col.SortTable-data.text-nowrap.align-center')
slave_svr = soup.select('body > div.body > div > div.Pane.Pane--full.Pane--dirtDark > div.Pane-content > div > div.Pane-content > div > div.SortTable.SortTable--stretch > div.SortTable-body > a > div:nth-of-type(6)')
slave_aoh = soup.select('body > div.body > div > div.Pane.Pane--full.Pane--dirtDark > div.Pane-content > div > div.Pane-content > div > div.SortTable.SortTable--stretch > div.SortTable-body > a > div:nth-of-type(5)')
for lvl in slave_lvl:
    
for svr in slave_svr:
    print(svr.text)
    