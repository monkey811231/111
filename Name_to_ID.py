import mysql.connector
import pandas as pd

MLBdb = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'last_test'
    )
#
# MLBdb = mysql.connector.connect(
#     host = '1.tcp.jp.ngrok.io',
#     port = 23879,
#     user = 'yulin',
#     password = 'clubgogo',
#     database = 'MoneyBallDatabase'
# )musqldump

cursor = MLBdb.cursor()

#製作columns的list
column1 = 'describe mlb_game '
cursor.execute(column1)
column = pd.DataFrame(cursor.fetchall())
xx = column.loc[:,0]
columns_list = []
for i in xx :
    columns_list += [i]
print(len(columns_list))



'''
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                      　　　
#   WAY1 連接MySQL 用MySQL直接換ID　(缺名字不一樣的)　　
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
'''
# sql_command = 'SELECT * FROM ID_reference '
# cursor.execute(sql_command)
# show = cursor.fetchall()
# # print(show)
#
# #製作球員:ID的dict
# id_dic = {i[1]:i[0] for i in show }
# print(id_dic)
# # T_id_dic = {v: k for k, v in id_dic.items()}
# # print(T_id_dic) #(ID,NAME)
#
# '''
# 一個一個columns處理
# '''
# #製作for迴圈用的
# # columns_list = ['away_pitcher','home_pitcher','away_1','away_2','away_3','away_4','away_5','away_6','away_7','away_8','away_9','home_1','home_2','home_3','home_4','home_5','home_6','home_7','home_8','home_9']
# columns_list = ['away_pitcher','home_pitcher']
#
# # sql_for_name = f'SELECT * FROM ID_reference '  #
# # cursor.execute(sql_for_name)
# # name_list = cursor.fetchall() #列出('名字',)
# # print(name_list)
#
# sql_unlock = 'SET SQL_SAFE_UPDATES=0'
# cursor.execute(sql_unlock)
#
#
# lost_player = []
# # for id_name in id_dic :
# #     id = id_dic[id_name]
# for test_column in columns_list :
#     sql_for_name = f'SELECT {test_column} FROM test '  #
#     cursor.execute(sql_for_name)
#     name_list = cursor.fetchall()  # 列出('名字',)
#
#     for i in name_list:
#         name = i[0]
#
#         try:
#             id = id_dic[name] #試當id_dic[name]有ID時進來做處理
#             print('')
#
#             if name == 'Chris Young':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=432934 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (
#                 (YEAR(game_date)=2010)AND((matchup LIKE 'SD%' OR matchup LIKE '%SD')) OR
#                 ((YEAR(game_date)=2011 OR YEAR(game_date)=2012)AND((matchup LIKE 'NYM%')OR matchup LIKE '%NYM')) OR
#                 (YEAR(game_date)=2014 AND (matchup LIKE 'SEA%'OR matchup LIKE '%SEA')) OR
#                 ((YEAR(game_date)=2015 OR YEAR(game_date)=2016 OR YEAR(game_date)=2017) AND (matchup LIKE 'KC%'OR matchup LIKE '%KC'))
#                 )
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=455759 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Rich Thompson':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=430829 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (YEAR(game_date)=2012)AND(matchup LIKE 'TB%' OR matchup LIKE '%TB')
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=460366 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Angel Sanchez':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=447816 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (
#                 (YEAR(game_date)=2010 AND ((matchup LIKE 'BOS%' OR matchup LIKE '%BOS') OR (matchup LIKE 'HOU%' OR matchup LIKE '%HOU')))
#                 OR
#                 (YEAR(game_date)=2011 AND (matchup LIKE 'HOU%' OR matchup LIKE '%HOU'))
#                 OR
#                 (YEAR(game_date)=2013 AND (matchup LIKE 'CHW%' OR matchup LIKE '%CHW'))
#                 )
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=605795 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#                 #
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Chris Carpenter' :
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=112020 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 ((YEAR(game_date)=2010 OR YEAR(game_date)=2011 OR YEAR(game_date)=2012) AND (matchup LIKE 'STL%'OR matchup LIKE '%STL'))
#
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=452764 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Luis Castillo':
#                 print(f'處理{name}')
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=622419 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (
#                 (YEAR(game_date)=2017 OR YEAR(game_date)=2018 OR YEAR(game_date)=2019) AND (matchup LIKE 'CIN%'OR matchup LIKE '%CIN')
#                 )
#
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=112116 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Josh Fields':
#                 print(f'處理{name}')
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=451661 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (
#                 YEAR(game_date)=2010 AND (matchup LIKE 'KC%'OR matchup LIKE '%KC')
#                 )
#
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=425222 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Chris Smith':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=434672 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (
#                 ((YEAR(game_date)=2010)AND(matchup LIKE 'MIL%' OR matchup LIKE '%MIL')) OR
#                 ((YEAR(game_date)=2016 OR YEAR(game_date)=2017) AND (matchup LIKE 'OAK%' OR matchup LIKE '%OAK'))
#                 )
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=627262 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Kyle Waldrop':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=592835 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 ((YEAR(game_date)=2015) OR (YEAR(game_date)=2016)) AND (matchup LIKE 'CIN%' OR matchup LIKE '%CIN')
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=448252 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Chris Carter':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=452080 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (YEAR(game_date)=2010)AND(matchup LIKE 'NYM%' OR matchup LIKE '%NYM')
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=474892 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Luis Jimenez':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=455921 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (YEAR(game_date)=2012)AND(matchup LIKE 'SEA%' OR matchup LIKE '%SEA')
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=499864 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Miguel Gonzalez':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=456068 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (
#                 (((YEAR(game_date)=2012)OR(YEAR(game_date)=2013)OR(YEAR(game_date)=2014)OR(YEAR(game_date)=2015))AND(matchup LIKE 'BAL%' OR matchup LIKE '%BAL'))
#                 OR
#                 (((YEAR(game_date)=2016)OR(YEAR(game_date)=2017)OR(YEAR(game_date)=2018))AND(matchup LIKE 'CHW%' OR matchup LIKE '%CHW'))
#                 OR
#                 (YEAR(game_date)=2016 AND (matchup LIKE 'TEX%' OR matchup LIKE '%TEX') )
#                 )
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=544838 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Javy Guerra':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=642770 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 ((YEAR(game_date)=2018)OR(YEAR(game_date)=2019))AND(matchup LIKE 'SD%' OR matchup LIKE '%SD')
#
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=457915 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Josh Bell':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=605137 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 ((YEAR(game_date)=2016)OR(YEAR(game_date)=2017)OR(YEAR(game_date)=2018)OR(YEAR(game_date)=2019))AND(matchup LIKE 'PIT%' OR matchup LIKE '%PIT')
#
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=458679 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Matt Reynolds':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=608703 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (
#                 (((YEAR(game_date)=2016)OR(YEAR(game_date)=2017))AND(matchup LIKE 'NYM%' OR matchup LIKE '%NYM'))OR
#                 ((YEAR(game_date)=2018)AND(matchup LIKE 'WSH%' OR matchup LIKE '%WSH'))
#                 )
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=519186 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Will Smith':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=669257 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (YEAR(game_date)=2019)AND(matchup LIKE 'LAD%' OR matchup LIKE '%LAD')
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=519293 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Jose Ramirez':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=608070 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 ((YEAR(game_date)=2013)OR(YEAR(game_date)=2014)OR(YEAR(game_date)=2015)OR(YEAR(game_date)=2016)OR(YEAR(game_date)=2017)OR
#                 (YEAR(game_date)=2018)OR(YEAR(game_date)=2019))
#                 AND(matchup LIKE 'CLE%' OR matchup LIKE '%CLE')
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=542432 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Austin Adams':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=613534 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 (
#                 ((YEAR(game_date)=2017)OR(YEAR(game_date)=2018)OR(YEAR(game_date)=2019))
#                 AND(matchup LIKE 'WSH%' OR matchup LIKE '%WSH'))
#                 OR
#                 ((YEAR(game_date)=2019)AND(matchup LIKE 'SEA%' OR matchup LIKE '%SEA')
#                 )
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=542866 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#                 #
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Daniel Robertson':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=621002 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 ((YEAR(game_date)=2017)OR(YEAR(game_date)=2018)OR(YEAR(game_date)=2019))AND(matchup LIKE 'TB%' OR matchup LIKE '%TB')
#
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=543706 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             elif name == 'Matt Duffy':
#                 print(f'處理{name}')
#
#                 # unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(unlock)
#
#                 sql_command1 = f'''
#                 UPDATE test SET {test_column}=592274 WHERE
#                 {test_column} = '{name}'
#                 AND
#                 ((YEAR(game_date)=2015)OR(YEAR(game_date)=2016))AND(matchup LIKE 'HOU%' OR matchup LIKE '%HOU')
#
#                 '''
#                 cursor.execute(sql_command1)
#                 MLBdb.commit()
#
#                 sql_command2 = f'UPDATE test SET {test_column}=622110 WHERE {test_column}="{name}"'
#                 cursor.execute(sql_command2)
#                 MLBdb.commit()
#
#                 # lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(lock)
#
#             else:
#                 # sql_unlock = 'SET SQL_SAFE_UPDATES=0'
#                 # cursor.execute(sql_unlock)
#                 # print(f'UPDATE test SET {test_column}={id_dic[name]} WHERE {test_column}="{name}"')
#                 # pass
#                 sql_update =f'UPDATE test SET {test_column}={id_dic[name]} WHERE {test_column}="{name}"'
#                 cursor.execute(sql_update)
#                 print('OK')
#                 # sql_lock = 'SET SQL_SAFE_UPDATES=1'
#                 # cursor.execute(sql_lock)
#
#         except KeyError:
#             lost_player += [name]
#             print('xx')
#
#
# sql_lock = 'SET SQL_SAFE_UPDATES=1'
# cursor.execute(sql_lock)
# MLBdb.commit()  #儲存執行的動作
#
#
# print('查無ID影響場數:{}'.format(len(lost_player)))
# print(lost_player)
#
# lost_ID_dic = {}
# for i in lost_player:
#     if lost_player.count(i)>1:
#         lost_ID_dic[i] = lost_player.count(i)
# print('查無ID人數:{}'.format(len(lost_ID_dic)))
# print(lost_ID_dic)
#
#
# cursor.clos


'''
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                      　　　
#   WAY2 利用pandas載到本地端做處理　　　
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
'''
# 先將要處理的table用SQLDB讓python讀到
# 然後將格式轉乘dataframe再載到本地端
# (做一次即可註解掉)
# mlb_game = 'SELECT * FROM mlb_game'
# cursor.execute(mlb_game)
# df = pd.DataFrame(cursor.fetchall())
# df.to_csv('../game_test/raw_mlb_game.csv',encoding='utf8',index=False)
# MLBdb.close()

#用id_reference製作字典 (重名 以及 姓名錯誤者另外處理)
get_id_reference = 'select * FROM id_reference'
cursor.execute(get_id_reference)
name_id_dic = { id[1] : id[0]for id in cursor.fetchall()}  #製成字典後KEY重複的會變一個,不過重複名自之前已經抓出來做例外處理所以不會影響)



#讀取剛剛製作的CSV檔
mlb_game = pd.read_csv('../game_test/raw_mlb_game.csv',index_col=False)
    # df.iat[colume, row] 查詢
    # x=df.iat[colume, row] 換成x值


#取出重名判斷用欄位(年)(隊伍)
for j in range(mlb_game.shape[0]): #(每個row都讀一次)
    YMD = mlb_game.iat[j, 1]  #取年
    MATCHUP = mlb_game.iat[j,3].split('@')
    # print(MATCHUP[0],MATCHUP[1]) #取主客隊
    for i in range(4,24) :
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
            # print('Good')


        else:
            mlb_game.iat[j, i] = name_id_dic[name]
            # print('OK')
    #換時間格式
    mlb_game.iat[j, 2] = mlb_game.iat[j, 2][7:12]

mlb_game.columns = columns_list
mlb_game.to_csv('ttt2.csv',encoding='utf-8',index=False)


MLBdb.close()