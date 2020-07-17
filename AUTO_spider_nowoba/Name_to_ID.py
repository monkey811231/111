import mysql.connector
import pandas as pd
import time




def name_to_id(csv_path):
    start = time.time()

    MLBdb = mysql.connector.connect(
        host='1.tcp.jp.ngrok.io',
        port=23879,
        user='yulin',
        password='clubgogo',
        database='MoneyBallDatabase'
    )

    # MLBdb = mysql.connector.connect(
    #     host='127.0.0.1',
    #     port=3306,
    #     user='root',
    #     password='root',
    #     database='last_test'
    # )
    cursor = MLBdb.cursor()

    #用id_reference製作字典 (重名 以及 姓名錯誤者另外處理)
    get_id_reference = 'select * FROM ID_reference'
    cursor.execute(get_id_reference)
    name_id_dic = { id[1] : id[0]for id in cursor.fetchall()}  #製成字典後KEY重複的會變一個,不過重複名自之前已經抓出來做例外處理所以不會影響)


    #讀取CSV
    mlb_game = pd.read_csv(f'{csv_path}',index_col=False)


    #取出重名判斷用欄位(年)(隊伍)
    for j in range(mlb_game.shape[0]): #(每個row都讀一次)
        YMD = mlb_game.iat[j, 0].split('-')[0]  #取年
        MATCHUP = mlb_game.iat[j,2].split('@')
        # print(MATCHUP[0],MATCHUP[1]) #取主客隊
        for i in range(17,37) :
            chigau_name_dic = {'John Mayberry':460055,'Nori Aoki':493114,'Matthew Joyce':459964,'Ivan De Jesus':474443,'Luis Cruz':458501,
                               'Chin-lung Hu':464341,'Juan Perez':448722,'T.J. House':543334,'Tony Gwynn':448242,'Tony Pena':430963,'Josh Smith':595001,
                               'Matt den Dekker':544925,'Mike Brosseau':670712,'Jon Niese':477003,'Rick van den Hurk':462995,'Phil Ervin':640447,
                               'Charles Leesman':489056,'Mike Morse':434604,'Rickie Weeks':430001,'Mike Ryan':408050,'Nathan Adcock':502264,'Val Pascucci':407831,
                               'Steven Tolleson':476270,'Dae-ho Lee':493193,'Albert Almora':546991,'Sam Deduno':465679,'Dwight Smith Jr.':596105,'Jae-gyun Hwang':666561,
                               'Russ Mitchell':452199,'Daniel Muno':594940,'Rafael Lopez':607257,'Robbie Ross':543726,'Melvin Upton Jr.':425834,'Luis Rodriguez':425904
                               }
            name = mlb_game.iat[j,i]
            # print(name) #取人名

            if name == 'Chris Young':
                print(f'處理{name}')
                if (YMD==2010 and ('SD'in MATCHUP)) or \
                    ((YMD==2011 or YMD==2012) and ('NYM' in MATCHUP)) or \
                    (YMD==2014 and ('SEA'in MATCHUP)) or \
                    ((YMD==2015 or YMD==2016 or YMD==2017) and ('KC' in MATCHUP)):
                    mlb_game.iat[j, i] = 432934
                else:
                    mlb_game.iat[j, i] = 455759


            elif name == 'Rich Thompson':
                print(f'處理{name}')
                if (YMD==2012 and ('TB'in MATCHUP)) :
                    mlb_game.iat[j, i] = 430829
                else:
                    mlb_game.iat[j, i] = 460366


            elif name == 'Angel Sanchez':
                print(f'處理{name}')
                if (YMD == 2010 and (('BOS' in MATCHUP)or('HOU' in MATCHUP))) or \
                        ((YMD == 2011 ) and ('HOU' in MATCHUP)) or \
                        (YMD == 2012 and ('CHW' in MATCHUP)):
                    mlb_game.iat[j, i] = 447816
                else:
                    mlb_game.iat[j, i] = 605795


            elif name == 'Chris Carpenter' :
                print(f'處理{name}')
                if ((YMD == 2010 or YMD == 2011 or YMD == 2012) and ('STL' in MATCHUP)):
                    mlb_game.iat[j, i] = 112020
                else:
                    mlb_game.iat[j, i] = 452764


            elif name == 'Luis Castillo':
                print(f'處理{name}')
                if ((YMD == 2017 or YMD == 2018 or YMD == 2019) and ('CIN' in MATCHUP)):
                    mlb_game.iat[j, i] = 622419
                else:
                    mlb_game.iat[j, i] = 112116


            elif name == 'Josh Fields':
                print(f'處理{name}')
                if (YMD == 2010 and ('KC' in MATCHUP)):
                    mlb_game.iat[j, i] = 451661
                else:
                    mlb_game.iat[j, i] = 425222


            elif name == 'Chris Smith':
                print(f'處理{name}')
                if (YMD == 2010 and ('MIL' in MATCHUP)) or \
                    ((YMD==2016 or YMD==2017) and ('OAK' in MATCHUP)):
                    mlb_game.iat[j, i] = 434672
                else:
                    mlb_game.iat[j, i] = 627262


            elif name == 'Kyle Waldrop':
                print(f'處理{name}')
                if ((YMD==2015 or YMD==2016)and ('CIN' in MATCHUP)):
                    mlb_game.iat[j, i] = 592835
                else:
                    mlb_game.iat[j, i] = 448252


            elif name == 'Chris Carter':
                print(f'處理{name}')
                if (YMD == 2010 and ('NYM' in MATCHUP)):
                    mlb_game.iat[j, i] = 452080
                else:
                    mlb_game.iat[j, i] = 474892


            elif name == 'Luis Jimenez':
                print(f'處理{name}')
                if (YMD == 2012 and ('SEA' in MATCHUP)):
                    mlb_game.iat[j, i] = 455921
                else:
                    mlb_game.iat[j, i] = 499864


            elif name == 'Miguel Gonzalez':
                print(f'處理{name}')
                if ((YMD == 2012 or YMD==2013 or YMD==2014 or YMD==2015 )and ('BAL' in MATCHUP)) or \
                    ((YMD == 2016 or YMD==2017 or YMD==2018)and ('CHW' in MATCHUP)) or \
                    (YMD == 2017 and ('TEX' in MATCHUP)):
                    mlb_game.iat[j, i] = 456068
                else:
                    mlb_game.iat[j, i] = 544838


            elif name == 'Javy Guerra':
                print(f'處理{name}')
                if ((YMD == 2018 or YMD==2019) and ('SD' in MATCHUP)):
                    mlb_game.iat[j, i] =642770
                else:
                    mlb_game.iat[j, i] =457915


            elif name == 'Josh Bell':
                print(f'處理{name}')
                if ((YMD == 2016 or YMD == 2017 or YMD == 2018 or YMD == 2019) and ('PIT' in MATCHUP)):
                    mlb_game.iat[j, i] = 605137
                else:
                    mlb_game.iat[j, i] = 458679


            elif name == 'Matt Reynolds':
                print(f'處理{name}')
                if ((YMD == 2016 or YMD == 2017) and ('NYM' in MATCHUP)) or \
                    (YMD == 2018 and ('WSH' in MATCHUP)) :
                    mlb_game.iat[j, i] = 608703
                else:
                    mlb_game.iat[j, i] = 519186


            elif name == 'Will Smith':
                print(f'處理{name}')
                if (YMD == 2019 and ('LAD' in MATCHUP)):
                    mlb_game.iat[j, i] = 669257
                else:
                    mlb_game.iat[j, i] = 519293


            elif name == 'Jose Ramirez':
                print(f'處理{name}')
                if ((YMD == 2013 or YMD==2014 or YMD==2015 or YMD==2016 or YMD==2017 or YMD==2018 or YMD==2019) and ('CLE' in MATCHUP)):
                    mlb_game.iat[j, i] = 608070
                else:
                    mlb_game.iat[j, i] = 542432


            elif name == 'Austin Adams':
                print(f'處理{name}')
                if ((YMD == 2017 or YMD==2018 or YMD==2019) and ('WSH' in MATCHUP)):
                    mlb_game.iat[j, i] = 613534
                else:
                    mlb_game.iat[j, i] = 542866


            elif name == 'Daniel Robertson':
                print(f'處理{name}')
                if ((YMD == 2017 or YMD==2018 or YMD==2019) and ('TB' in MATCHUP)):
                    mlb_game.iat[j, i] = 621002
                else:
                    mlb_game.iat[j, i] = 543706


            elif name == 'Matt Duffy':
                print(f'處理{name}')
                if ((YMD == 2015 or YMD==2016) and ('HOU' in MATCHUP)):
                    mlb_game.iat[j, i] = 592274
                else:
                    mlb_game.iat[j, i] = 622110

            elif name in chigau_name_dic.keys():
                mlb_game.iat[j, i] = chigau_name_dic[name]


            else:
                mlb_game.iat[j, i] = name_id_dic[name]

        # #換時間格式
        # mlb_game.iat[j, 2] = mlb_game.iat[j, 2][7:12]


    mlb_game.to_csv(f'./to_ID/game{csv_path[11:19]}_ID.csv',encoding='utf-8',index=False)
    finish = time.time()
    total = round(finish - start,2)
    print(f'game{csv_path[11:19]}_ID.csv檔案製作完成')
    print(f'ID轉換完成,花費 {total:.2f} 秒\n')

    MLBdb.close()
    return  f'./to_ID/game{csv_path[11:19]}_ID.csv'




if __name__ == '__main__':
    name_to_id()