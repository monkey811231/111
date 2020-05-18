from MLB_date import date_search
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as options
import time
def mmm():
    s = date_search()
    for date in s:
        # print(date)
        year = date[:4]
        month = date[4:6]
        day = date[6:8]


        url = 'https://www.baseball-reference.com/boxes/?year={}&month={}&day={}'.format(year,month,day)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        req = requests.get(url , headers=headers)
        soup = BeautifulSoup(req.text,'html.parser')


        try:
            a = soup.select('div[id="content"] h3')[0].text
            a == 'No Games Were or Have Yet Been Played on This Date'
            print('{}沒比賽'.format(date))
            continue
        except:
            print('{}有比賽'.format(date))
            game_url = aaa(date)

        












def aaa(date):
    from MLB_date import date_search
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as options
    import time



    year = date[:4]
    month = date[4:6]
    day = date[6:8]

    options = options()
    # 禁止瀏覽器彈窗
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    # 不開啟視窗畫
    option = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # 開啟瀏覽器(brower)
    driver = webdriver.Chrome("./chromedriver.exe", options=options)

    url = 'https://www.baseball-reference.com/boxes/?month={1}&day={2}&year={0}'.format(year,month,day)
    driver.get(url)

    allday_game = driver.find_elements_by_link_text('Final')

    x = []
    for game_url in allday_game:
        x += [game_url.get_attribute('href')]
    print(x)
    return x
    time.sleep(3)



if __name__ == '__main__':
    mmm()




