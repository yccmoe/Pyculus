#누겁실?
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import telepot


async def ngs(bot, letter, phgs):
    name, chid, ning = letter['name'], letter['chid'], letter['ning']
    id, pw, urlA, urlC = phgs['id'], phgs['pw'], phgs['url']['A'], phgs['url']['C']
    driver_path = 'c:/Users/yccmo/dev/Pyculus/lib_/chromedriver.exe'
    send = await bot.sendMessage(chid, '똑똑똑...')
    msg_idf = telepot.message_identifier(send)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    driver.implicitly_wait(3)
    driver.get(urlA)
    driver.find_element_by_name('username').send_keys(id)
    driver.find_element_by_name('passwd').send_keys(pw)
    driver.find_element_by_xpath('//*[@id="submit_bt"]').click()

    await bot.editMessageText(msg_idf, '두근두근...')

    driver.get(urlC)

    await bot.editMessageText(msg_idf, '거의 다 됐어요!')
    html = driver.page_source
    soup = bs(html, 'html.parser')
    soup = str(soup)
    mac_list = []

    if '94:FE:22:B7:57:91' in soup: mac_list.append('얌 핸드폰')
    if 'F8:E6:1A:64:65:7D' in soup: mac_list.append('얌 핸드폰')
    if 'B4:F7:A1:E4:90:9D' in soup: mac_list.append('승 핸드폰')
    if '94:8B:C1:E5:65:82' in soup: mac_list.append('야 핸드폰')
    if '44:00:10:AD:83:9C' in soup: mac_list.append('꽉 핸드폰')
    if '94:8B:C1:3E:FA:5E' in soup: mac_list.append('새 핸드폰')
    if 'F8-E6-1A-FF-65-91' in soup: mac_list.append('빠 핸드폰')

    if '74:D4:35:5D:DD:89' in soup: mac_list.append('메인컴퓨터')
    if '6C:AD:F8:DA:00:F7' in soup: mac_list.append('크롬캐스트')
    if 'B8:27:EB:FA:B6:A7' in soup: mac_list.append('레트로파이')
    if 'A4:34:D9:3A:E8:DC' in soup: mac_list.append('노트북')
    if 'C8:63:F1:36:A2:31' in soup: mac_list.append('야 Ps4')
    if '5C:52:1E:5D:38:3F' in soup: mac_list.append('닌텐도 스위치')
    if '60:C5:47:22:E9:9D' in soup: mac_list.append('미니맥')
    if 'C8-28-32-2C-0C-9B' in soup: mac_list.append('미박스S')
    #print(soup)
    print(mac_list)  # this should print "Google"
    await bot.editMessageText(msg_idf, '과연.....!')
    driver.quit()

    try:
        res=''
        for i in range(len(mac_list)):
            res=res+mac_list[i]+'\n'
    except:
        res = '찬바람만이...'
    finally:
        await bot.editMessageText(msg_idf, res)
    return 'okay'