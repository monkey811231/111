from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as options
import time
import requests
from MLB_date import date_search

s = date_search()
for date in s:
    print(date)
    year = date[:4]
    month = date[4:6]
    day = date[6:8]


    url = 'https://www.baseball-reference.com/boxes/?year={}&month={}&day={}'.format(year,month,day)


    options = options()
    #禁止瀏覽器彈窗
    prefs = {
        'profile.default_content_setting_values' :
            {
            'notifications' : 2
             }
    }

    option = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument("--disable-javascript")  # 禁用JavaScript

    #開啟瀏覽器(brower)
    driver = webdriver.Chrome("./chromedriver.exe",options=options)



    url = 'https://www.baseball-reference.com/boxes/?month=04&day=05&year=2010'
    driver.get(url)

    allday_game = driver.find_elements_by_link_text('Final')


    x = []
    for game_url in allday_game:
        x += [game_url.get_attribute('href')]
    print(x)
    time.sleep(3)
