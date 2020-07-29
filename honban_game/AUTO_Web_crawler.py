from honban_game import web_crawler
import pytz
import datetime
import csv
import time

def AUTO_crawler(US_ET_date,US_ET_time,US_ET_time_split):
    #check the ET
    # while 1 :
    #     #建立美東日期時間
    #     US_ET = pytz.timezone('US/Eastern')
    #     US_ET_datetime = str(datetime.datetime.now(US_ET)).split(' ')
    #     # print(US_ET_datetime)
    #     US_ET_date = US_ET_datetime[0]
    #     US_ET_time = US_ET_datetime[1].split('.')[0]
    #     US_ET_time_split = US_ET_time.split(':')[0:2]
    #     print(US_ET_date, US_ET_time)
    #     # print(US_ET_time.split(':')[0:2])
    print(US_ET_date,US_ET_time,US_ET_time_split)

    game_date = open('date.txt', 'r', encoding='utf-8-sig').read()
    #check換日
    if  game_date != US_ET_date: #如果換日 會去爬取明天有幾場賽事 並將比賽時間用字典記下
        #確定日期與原本不一樣之後 再判斷時間 如果是00:00則更新 date
        if US_ET_time_split == ['00','00']:  #預設更新時間為美東00:00 若過時間在此調整
            print(US_ET_time_split)
            print(f'{game_date} change to {US_ET_date}')
            open('date.txt', 'w', encoding='utf-8-sig').write(US_ET_date)
            game_date = US_ET_date
            print(f'{game_date} changed!!')
            return_dic = web_crawler.GAME_DATE(game_date)[0]
            # return_len = web_crawler.GAME_DATE(game_date)[1] #いらないもん
            # print(type(return_dic),return_dic)
            # print(type(return_len),return_len)
            open('game_time.txt','w',encoding='utf-8-sig').write(str(return_dic))

            column_list = ['date', 'time', 'matchup', '1top', '1bot', '2top', '2bot', '3top', '3bot', '4top', '4bot',
                           '5top', '5bot',
                           'away_total', 'home_total', 'Umpires', 'Venue',
                           'away_pitcher', 'home_pitcher',
                           'v_1', 'v_2', 'v_3', 'v_4', 'v_5', 'v_6', 'v_7', 'v_8', 'v_9',
                           'h_1', 'h_2', 'h_3', 'h_4', 'h_5', 'h_6', 'h_7', 'h_8', 'h_9']
            with open('./game/game{}.csv'.format(US_ET_date), 'w', newline='', encoding='utf-8-sig') as f:
                MLB_clumn = csv.writer(f)
                MLB_clumn.writerow(column_list)

    #檢查是否到爬取時間 並且更新字典(date_time)
    elif game_date == US_ET_date:
        #更新字典 處理突然暫訂時間 與 突然出現的延賽
        return_dic = web_crawler.GAME_DATE(game_date)[0]
        open('game_time.txt', 'w', encoding='utf-8-sig').write(str(return_dic))

        gametime_dic = eval(open('game_time.txt','r',encoding='utf-8-sig').read())
        print(type(gametime_dic),gametime_dic)
        for i in gametime_dic:
            time_key = gametime_dic[i].split(':')[0:2]  #如果字典時間  =  現在美東時間  則會取出那時間對應的index套進spider去做處理
            # print(time_key, US_ET_time_split)
            if time_key == US_ET_time_split:
                print(' Time is UP!! ')
                web_crawler.spider(i, US_ET_date, US_ET_time)
    else:
        print('ERROR')

    # 無聊製作
    # for a in range(1,5):
    #     b='...'
    #     print(f'{b*a}')
    #     time.sleep(25)
    #     print('\n')

    time.sleep(60)




if __name__ == '__main__':
    # AUTO_crawler()
    # spider(0,'2020-07-07')
    while 1 :
        #建立美東日期時間
        US_ET = pytz.timezone('US/Eastern')
        US_ET_datetime = str(datetime.datetime.now(US_ET)).split(' ')
        # print(US_ET_datetime)
        US_ET_date = US_ET_datetime[0]
        US_ET_time = US_ET_datetime[1].split('.')[0]
        US_ET_time_split = US_ET_time.split(':')[0:2]
        print(US_ET_date, US_ET_time)
        # print(US_ET_time.split(':')[0:2])
        AUTO_crawler(US_ET_date,US_ET_time,US_ET_time_split)   #參數範例 2020-07-29     01:56:44       ['01', '56']<<用於Check換日時間 與 對照比賽爬蟲時間
