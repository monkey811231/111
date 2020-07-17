import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import csv


def game_url(date):  # 判斷當天比賽
    date = date.split('-')
    year = int(date[0])-1
    month = date[1]
    day = int(date[2])
    print(f'取 {year}-{month}-{day} URL')

    url = 'https://www.baseball-reference.com/boxes/?year={}&month={}&day={}'.format(year, month, day)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    #代理伺服器 沒用到 騙人用
    # proxies = {
    #     'http':'206.189.184.46:80',
    #     'https':'52.191.103.11:3128'
    # }
    while True :
        try:
            req = requests.get(url,headers=headers)
            soup = BeautifulSoup(req.text, 'html.parser')

            try:
                soup.select('div[id="content"] h3')[0].text == "No Games Were or Have Yet Been Played on This Date"
                return None
            except:
                options = Options()
                # 禁止瀏覽器彈窗
                prefs = {
                    'profile.default_content_setting_values':
                        {
                            'notifications': 2
                        }
                }
                # 不開啟視窗畫面
                option = webdriver.ChromeOptions()
                options.add_argument('--headless')
                options.add_argument('blink-settings=imagesEnabled=false')
                options.add_argument("--disable-javascript")  # 禁用JavaScript
                options.add_argument('--disable-gpu')  # google say加上這個屬性來規避bug
                options.add_argument('--no-sandbox')  # 以最高權限運行
                options.add_argument('--disable-dev-shm-usage')

        # 開啟瀏覽器(brower)
                driver = webdriver.Chrome("./chromedriver.exe", options=options)

                driver.get(url)

                allday_game = driver.find_elements_by_link_text('Final')


                url_list = []
                for game_url in allday_game:
                        url_list += [game_url.get_attribute('href')]

                # 關閉瀏覽器
                driver.quit()
                print('取得URL')
                return url_list
            break
        except EnvironmentError as e:
            print(f'{e} , \nwait 10secs retry')
            time.sleep(10)
            pass


def for_search(url):

    options = Options()
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    options.add_experimental_option('prefs', prefs)
    options.add_argument("--headless")
    options.add_argument("--disable-javascript")
    options.add_argument('--disable-gpu')  # google say加上這個屬性來規避bug
    options.add_argument('--no-sandbox') #以最高權限運行
    options.add_argument('--disable-dev-shm-usage')

    column_list = ['date', 'matchup', '1top', '1bot', '2top', '2bot', '3top', '3bot', '4top', '4bot', '5top', '5bot',
                   'away_total', 'home_total', 'Umpires', 'Venue', \
                   'away_pitcher', 'home_pitcher', \
                   'v_1', 'v_2', 'v_3', 'v_4', 'v_5', 'v_6', 'v_7', 'v_8', 'v_9', \
                   'h_1', 'h_2', 'h_3', 'h_4', 'h_5', 'h_6', 'h_7', 'h_8', 'h_9']

    # content = [] #裝爬到的數據塞進DataFrame

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    date = url.split('.shtml')[0][-9:-1]
    game_year = date[:4]
    game_month = date[4:6]
    game_day = date[6:]
    game_date = game_year + '-' + game_month + '-' + game_day
    # print(game_date)

    driver = webdriver.Chrome("./chromedriver.exe", options=options)
    # driver.implicitly_wait(10)     #開啟網頁等待10秒在開始動作
    html = driver.get(url)
    html_data = driver.page_source  # 取得網站原始碼
    soup = BeautifulSoup(html_data, 'html.parser')
    tables = pd.read_html(html_data)  # 取得table 此動作必須在selenium下處理 否則該table標籤爬不到
    # print(tables[-5],'\n',tables[-4])
    driver.quit()  # '完整'關閉背景的selenium相關程式

    '''=============='''
    '''  取得先發名單  '''
    '''=============='''
    v_player = tables[-5]
    h_player = tables[-4]
    a = v_player.loc[:, [1, 2]].values
    b = h_player.loc[:, [1, 2]].values

    # 取先發投手姓名
    v_pitcher = ''
    for i in a:
        if i[1] == 'P':
            v_pitcher += i[0]

    h_pitcher = ''
    for i in b:
        if i[1] == 'P':
            h_pitcher += i[0]
    # print(v_pitcher, h_pitcher)

    # 取先發打者姓名依棒次，國聯投手會加入打擊，所以國聯投手會出現兩次(投手/打者)
    v_hitter_1 = v_player.loc[:, [1]].values
    v_hitter = v_hitter_1[0:9]

    h_hitter_1 = h_player.loc[:, [1]].values
    h_hitter = h_hitter_1[0:9]

    '''=============='''
    '''  取對戰球隊   '''
    '''=============='''
    tm = soup.select('table[class="linescore nohover stats_table no_freeze"] tbody tr td a')[2::3]

    v_tm = tm[0].text
    h_tm = tm[1].text

    # 馬林魚2012改名 因此有兩個kay
    teamname_dict = {'Boston Red Sox': 'BOS', 'Toronto Blue Jays': 'TOR', 'Baltimore Orioles': 'BAL',
                     'Tampa Bay Rays': 'TB',
                     'New York Yankees': 'NYY', 'Chicago White Sox': 'CWS', 'Cleveland Indians': 'CLE',
                     'Detroit Tigers': 'DET',
                     'Kansas City Royals': 'KC', 'Minnesota Twins': 'MIN', 'Oakland Athletics': 'OAK',
                     'Los Angeles Angels of Anaheim': 'LAA','Los Angeles Angels' : 'LAA',
                     'Texas Rangers': 'TEX', 'Houston Astros': 'HOU', 'Seattle Mariners': 'SEA',
                     'Atlanta Braves': 'ATL', 'Philadelphia Phillies': 'PHI',
                     'Florida Marlins': 'MIA', 'Miami Marlins': 'MIA', 'New York Mets': 'NYM',
                     'Washington Nationals': 'WSH',
                     'Milwaukee Brewers': 'MIL', 'Pittsburgh Pirates': 'PIT', 'Cincinnati Reds': 'CIN',
                     'Chicago Cubs': 'CHC',
                     'St. Louis Cardinals': 'STL', 'San Diego Padres': 'SD', 'Arizona Diamondbacks': 'ARI',
                     'San Francisco Giants': 'SF', 'Colorado Rockies': 'COL',
                     'Los Angeles Dodgers': 'LAD'}
    matchup = teamname_dict[v_tm] + '@' + teamname_dict[h_tm]
    # print(matchup)

    '''==========='''
    '''  取主裁判  '''
    '''==========='''
    HP = soup.select('div[id="content"] div[class="section_wrapper"]')[2].select('div[class="section_content"] div')[
        0].text
    Umpires = HP.split(',')[0].split('- ')[1]
    # print(Umpires)

    '''========='''
    '''  取分數 '''
    '''========='''
    point = soup.select('table[class="linescore nohover stats_table no_freeze"] tbody tr')
    v_p = point[0].select('td')[2:7]
    h_p = point[1].select('td')[2:7]
    # print(v_p,h_p)

    v_total = 0  # 客隊五局總分
    v_p_list = []  # 客隊五局分數
    for i in v_p:
        if i.text == 'X' :
            continue
        j = int(i.text)
        v_total += j
        v_p_list += i.text

    h_total = 0  # 主隊伍局總分
    h_p_list = []  # 主隊五局分數
    for i in h_p:
        if i.text == 'X' : #如果為分數欄X則只加入list 加總部分continue掉
            h_p_list += i.text
            continue
        j = int(i.text)
        h_total += j
        h_p_list += i.text

    '''========='''
    '''  取球場  '''
    '''========='''
    # Venue_name = soup.select('div[class="scorebox_meta"] div')[3].text
    # venue = ' '.join(Venue_name.split(' ')[1:])
    Venue_name = soup.select('div[class="scorebox_meta"] div')
    for i in Venue_name:
        i = i.text
        # print(i)
        if i.split(' ')[0] == 'Venue:':
            venue = ' '.join(i.split(' ')[1:])
            # print(venue)
            break
        else:
            venue = 'venue_error'
            continue
    '''========='''
    '''  取時間  '''
    '''========='''
    game_timezz = soup.select('div[class="scorebox_meta"] div')[1].text
    if game_timezz.split(':')[0] == 'Start Time' :
        pass
    else:
        game_timezz = soup.select('div[class="scorebox_meta"] div')[2].text

    game_timez = game_timezz.split(' ')[2:4]
    try:
        if game_timez[1] == 'a.m.':
            aa = 'am'
        else:
            aa = 'pm'
        try :
            g_t1 = f'{game_timez[0]} {aa}'
            g_t2 = '%I:%M %p'
            g_t3 = time.strptime(g_t1, g_t2)
            game_time = f'{g_t3.tm_hour}:{g_t3.tm_min}'
            # print(game_time)
        except ValueError:
            print('time data does not match format "%I:%M %p"')
            game_time = 'time_error'
    except IndexError:
        print('list index out of range')
        game_time = 'time_error'





    content = [game_date, game_time ,matchup, v_p_list[0], h_p_list[0], v_p_list[1], h_p_list[1], v_p_list[2], h_p_list[2],
               v_p_list[3], h_p_list[3], v_p_list[4], h_p_list[4],
               v_total, h_total, Umpires, venue, v_pitcher, h_pitcher, v_hitter[0][0], v_hitter[1][0], v_hitter[2][0],
               v_hitter[3][0], v_hitter[4][0],
               v_hitter[5][0], v_hitter[6][0], v_hitter[7][0], v_hitter[8][0], h_hitter[0][0], h_hitter[1][0],
               h_hitter[2][0], h_hitter[3][0], h_hitter[4][0],
               h_hitter[5][0], h_hitter[6][0], h_hitter[7][0], h_hitter[8][0]]
    return content



def spider(date):
    url_return = game_url(date)


    start = time.time()
    date = date.split('-')
    year = int(date[0])-1
    month = date[1]
    day = int(date[2])
    new_date = f'{year}{month}{day}'


    if url_return == None:
        print(f'No Games Were or Have Yet Been Played on {url_return}')
        pass
    elif 'allstar-game' == str(url_return).split('.shtml')[0][-12:]:
        print('ALL-STAR')
        pass
    else:  # 如果有回傳LIST 利用URL呼叫內容爬蟲程式
        url_list = []
        for url in url_return:
            with open('karioku.text',encoding='utf-8-sig') as a :
                karioku_list = a.read().split(',')
                if url in karioku_list:
                    print(f'{url}已存在')
                else:
                    with open('karioku.text','a',encoding='utf-8-sig') as b:
                        b.write(f'{url},')
                    url_list += [url]


        if url_list != []:
            with concurrent.futures.ProcessPoolExecutor() as executor:
                content_return = executor.map(for_search, url_list)
                column_list = ['date', 'time' , 'matchup', '1top', '1bot', '2top', '2bot', '3top', '3bot', '4top', '4bot',
                               '5top', '5bot',
                               'away_total', 'home_total', 'Umpires', 'Venue',
                               'away_pitcher', 'home_pitcher',
                               'v_1', 'v_2', 'v_3', 'v_4', 'v_5', 'v_6', 'v_7', 'v_8', 'v_9',
                               'h_1', 'h_2', 'h_3', 'h_4', 'h_5', 'h_6', 'h_7', 'h_8', 'h_9']
                with open('./game/game{}.csv'.format(new_date), 'w', newline='', encoding='utf-8-sig') as f:
                    MLB_clumn = csv.writer(f)
                    MLB_clumn.writerow(column_list)

                for content_return_1 in content_return:
                    print(content_return_1)
                    with open('./game/game{}.csv'.format(new_date), 'a', newline='', encoding='utf-8-sig') as g:
                        MLB_row = csv.writer(g)
                        MLB_row.writerow(content_return_1)


                finish = time.time()
                print('game{}.csv檔案製作完成\n爬蟲完成,花費 {} 秒\n '.format(new_date,round(finish - start, 2)))
                return './game/game{}.csv'.format(new_date)
        else:
            print('無新增URL')
            return 'No new URL'


if __name__ == "__main__":
    spider("2019-07-11")