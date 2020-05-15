from MLB_date import date_search
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pprint
from time import sleep
from random import randint

s = date_search()
for date in s:

    url = 'https://www.sportsbookreview.com/betting-odds/mlb-baseball/pointspread/1st-half/?date={}'.format(date)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    req = requests.get(url, headers = headers)
    soup = BeautifulSoup(req.text,'html.parser')

    game_year = url[-8:-4]
    game_month = url[-4:-2]
    game_day = url[-2:]
    game_date = game_year + '-' + game_month + '-' + game_day
    print(game_date)

    '''
    計算當天場次 決定for迴圈次數
    '''
    # teamname = soup.select('div[class="_1eZfC"] div[class="_1FVbw"] div[class="_2563p"]')
    # print(teamname)
    # print(len(teamname)

    gametatle = soup.select('div[class="_2563p"]')
    # print(len(gametatle))  #當天比賽場數

    '''
    當日無法賽則略過
    '''
    # for game_session in range(len(teamname)) : #用len()設定場次
    #     num = game_session
    try :
        teamname0 = soup.select('div[class="_1eZfC"]')[0]#加上index開始爬
    except IndexError:
        print('\n【no game in today】\n')
        continue




    x = []
    for game_session in range(len(gametatle)) : #用len()設定場次
        num = game_session
        teamname1 = teamname0.select('div[class="_1FVbw"]')[num].select(' a div')[::3]  #[<div>STL</div>, <div>PIT</div>]
        x += teamname1

    '''
    列出球隊
    '''
    teamname_list = [z.text for z in x]
    v_team = teamname_list[::2]
    h_team = teamname_list[1::2]
    eee = len(v_team)
    t = v_team + h_team

    c = ''
    for i in range(len(v_team)):
        c += v_team[i] + '@' + h_team[i] + '/'
    team_name = c.split('/')[:-1]  #因為用/分割 最後會有多一個/ 所以要[:-1]去掉最後一個
    # print(team_name)


    #取出投手名稱

    z = []
    for game_session in range(len(gametatle)):  # 用len()設定場次
        num = game_session
        pitchername = teamname0.select('div[class="_1FVbw"]')[num].select('a[class="_3qi53"] div')[1::3] #('div[class="_34bLJ _3XJBX"] div')[:]
        z += pitchername
    '''
    將一天內所有出賽先發列出
    '''
    pitchername_list = [w.text for w in z]
    v_pitchername = pitchername_list[::2]
    h_pitchername = pitchername_list[1::2]
    # print(v_pitchername)  #['L. Severino (R)', 'J. Eickhoff (R)', 'C. Rea (R)', 'D. Sala
    # print(h_pitchername)  #['J. Zimmermann (R)', 'J. deGrom (R)', 'J. Lyles (R)', 'J. Da




    '''
    取分數
    '''
    top1 = []
    top2 = []
    top3 = []
    top4 = []
    top5 = []
    bot1 = []
    bot2 = []
    bot3 = []
    bot4 = []
    bot5 = []
    v_point_sum = []
    h_point_sum = []

    for game_session in range(len(gametatle)) : #用len()設定場次
        gamepoint = teamname0.select('div[class="_2563p"]')[game_session].select('div[class="_1Y3rN _308Yc"] div')
        vh_point = [zz.text for zz in gamepoint ][:10]
        v_point = vh_point[::2]  #客隊1-5局分數 ['0', '0', '0', '0', '0']
        h_point = vh_point[1::2] #主隊1-5局分數 ['1', '0', '0', '2', '0']

        top1 += [v_point[0]]
        top2 += [v_point[1]]
        top3 += [v_point[2]]
        top4 += [v_point[3]]
        top5 += [v_point[4]]
        bot1 += [h_point[0]]
        bot2 += [h_point[1]]
        bot3 += [h_point[2]]
        bot4 += [h_point[3]]
        bot5 += [h_point[4]]

        '''
        top1 += v_point[0]
        top2 += v_point[1]
        top3 += v_point[2]
        top4 += v_point[3]
        top5 += v_point[4]
        bot1 += h_point[0]
        bot2 += h_point[1]
        bot3 += h_point[2]
        bot4 += [h_point[3]]
        bot5 += h_point[4]
        因為原本h_point以字串insert進bot4 但單場得分兩位數 會被拆成兩個數字 因此將它改成lsit塞進去
        '''


        v_point_sum1 =0
        for i in v_point:
            v_point_sum1 += int(i)
        v_point_sum += [v_point_sum1]

        h_point_sum1 =0
        for i in h_point:
            h_point_sum1 += int(i)
        h_point_sum += [h_point_sum1]

        # print(v_point_sum) #客隊1-5局總分
        # print(h_point_sum) #主隊1-5局總分


    # # one_1 = []
    # # two_2 = []
    # # three_3 = []
    # # four_4 = []
    # # five_5 = []
    # v_point = []
    # h_point = []
    # for game_session in range(len(teamname)) : #用len()設定場次
    #     # print(game_session)
    #     try:
    #         visiting_team_point = teamname0.select('div[class="_2563p"]')[game_session].select('div[class="_1Y3rN _308Yc"] div')[0::2]   #先攻隊得分
    #         home_team_point = teamname0.select('div[class="_2563p"]')[game_session].select('div[class="_1Y3rN _308Yc"] div')[1::2]   #後功隊得分
    #         # print(visiting_team_point)
    #         # print(home_team_point)
    #
    #         # v1_point = [point.text for point in visiting_team_point]
    #         # h1_point = [point.text for point in home_team_point]
    #         # v_point +=
    #         # h_point += h1_point
    #
    #         # print(v_point)
    #         # print(h_point)
    #
    #         # #同一局上下整成list塞進game_content
    #         # one = [visiting_team_point_list[0] , home_team_point_list[0]]
    #         # # print(one)
    #         # one_1 += one
    #         # two = [visiting_team_point_list[1] , home_team_point_list[1]]
    #         # # print(two)
    #         # two_2 += two
    #         # three = [visiting_team_point_list[2] , home_team_point_list[2]]
    #         # # print(three)
    #         # three_3 += three
    #         # four = [visiting_team_point_list[3] , home_team_point_list[3]]
    #         # # print(four)
    #         # four_4 += four
    #         # five = [visiting_team_point_list[4] , home_team_point_list[4]]
    #         # # print(five)
    #         # five_5 += five
    #     except:
    #         print('XXXX')
    # print('///')
    # print(game_date)
    # print('///')
    # print(team_name)
    # print(v_pitchername)
    # print(h_pitchername)
    # print(1)
    # print(top1)
    # print(top2)
    # print(top3)
    # print(top4)
    # print(top5)
    # print(2)
    # print(bot1)
    # print(bot2)
    # print(bot3)
    # print(bot4)
    # print(bot5)
    # print(v_point_sum)
    # print(h_point_sum)
    # print('======')
    # print(len(game_date))
    # print(len(team_name))
    # print(len(v_pitchername))
    # print(len(h_pitchername))
    # print(len(top1))
    # print(len(bot1))
    # print(len(top2))
    # print(len(bot2))
    # print(len(top3))
    # print(len(bot3))
    # print(len(top4))
    # print(len(bot4))
    # print(len(top5))
    # print(len(bot5))
    # print(len(v_point_sum))
    # print(len(h_point_sum))
    # print(len(v_pitchername))
    # print(len(h_pitchername))



    game_content = {'date':game_date,
                    'teamname':team_name,
                    '1_top' :top1,
                    '1_bot' :bot1,
                    '2_top' :top2,
                    '2_bot' :bot2,
                    '3_top' :top3,
                    '3_bot' :bot3,
                    '4_top' :top4,
                    '4_bot' :bot4,
                    '5_top' :top5,
                    '5_bot' :bot5,
                    'visiting_total' :v_point_sum,
                    'home_total' :h_point_sum,
                    'visiting_pitcher': v_pitchername,
                    'home_pitcher': h_pitchername,
                  }


    # # try:
    game = pd.DataFrame(game_content)
    print(game)
    # # except ValueError:
    # #     game20160403 = pd.DataFrame({'一局':'none',
    # #                 '二局':'none',
    # #                 '三局':'none',
    # #                 '四局':'none',
    # #                 '五局':'none'},index=[0])  #解決延賽

    #將DATAFRAME輸出成csv
    game.to_csv('game_Folder/game{date}.csv'.format(date=date),encoding='utf_8_sig',index=False)
    #測試輸出
    # game20160403.to_csv('game{date}.csv'.format(date=date), encoding='utf_8_sig',index=False)
    # sleep(randint(3,5))
    print('\n\n|| done ||\n\n')
