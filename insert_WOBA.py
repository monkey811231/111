import pandas as pd
import numpy as np

mlb_game = pd.read_csv('for_last_test/mlb_game_v1.csv',encoding='utf-8',index_col=False)
y2009 = pd.read_csv('./game_test/batter_data_2009.csv', index_col=False)
y2010 = pd.read_csv('./game_test/batter_data_2010.csv', index_col=False)
y2011 = pd.read_csv('./game_test/batter_data_2011.csv', index_col=False)
y2012 = pd.read_csv('./game_test/batter_data_2012.csv', index_col=False)
y2013 = pd.read_csv('./game_test/batter_data_2013.csv', index_col=False)
y2014 = pd.read_csv('./game_test/batter_data_2014.csv', index_col=False)
y2015 = pd.read_csv('./game_test/batter_data_2015.csv', index_col=False)
y2016 = pd.read_csv('./game_test/batter_data_2016.csv', index_col=False)
y2017 = pd.read_csv('./game_test/batter_data_2017.csv', index_col=False)
y2018 = pd.read_csv('./game_test/batter_data_2018.csv', index_col=False)


#取出matchup 欄位所有值 切片後存成lis
matchups = mlb_game.loc[:,'matchup']
#matchups = mlb_game.values.to_list()
away_team = []
home_team = []
for matchup in matchups :
    awayteam = matchup.split('@')[0]
    hometeam = matchup.split('@')[1]
    away_team += [awayteam]
    home_team += [hometeam]
a = np.array(away_team)

#刪增column
mlb_game = mlb_game.drop('matchup', axis = 1) #刪掉matchup
mlb_game.insert(2,'away_team',np.array(away_team))
mlb_game.insert(3,'home_team',np.array(home_team))
for num in range(1,10):
    mlb_game[f'away_{num}_wobs'] = mlb_game[f'away_{num}']
for num in range(1,10):
    mlb_game[f'home_{num}_wobs'] = mlb_game[f'home_{num}']
'''
# a1_woba = []
# a2_woba = []
# a3_woba = []
# a4_woba = []
# a5_woba = []
# a6_woba = []
# a7_woba = []
# a8_woba = []
# a9_woba = []
# h1_woba = []
# h2_woba = []
# h3_woba = []
# h4_woba = []
# h5_woba = []
# h6_woba = []
# h7_woba = []
# h8_woba = []
# h9_woba = []
'''
# for i in range(100):
for i in range(mlb_game.shape[0]):
    # print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print(i,f"{i/(mlb_game.shape[0]*100):.3f}%")
    # print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    year = mlb_game.iat[i,1].split('-')[0]
    for batter in range(31,49):
        # print(mlb_game.iat[i, batter])

        if year == '2010':
            if mlb_game.iat[i, batter] not in [i for i in y2009['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2009['woba'].median()
            # id_list = [i for i in y2009['player_id'] ]
            # if mlb_game.iat[i, batter] in id_list:  #換WOBA
            #     for ii in range(y2009.shape[0]):
            #         if mlb_game.iat[i, batter] == y2009.iat[ii, 1]:
            #             if y2009.iat[ii, 9] == '0':
            #                 y2009.iat[ii, 9] = 'null'
            #             mlb_game.iloc[i, batter] = y2009.iat[ii, 9]
            #
            #         # if mlb_game.iloc[i, batter] == 0 :
            #         #     mlb_game.iloc[i , batter] = 'null'
            #             # mlb_game.iloc[i, batter] = y2009['woba'].median()  # 沒有WOBA的放中位數
            #
            # else:
            #     pass
            else:
                for ii in range(y2009.shape[0]):
                    if mlb_game.iat[i, batter] == y2009.iat[ii, 1] : #換WOBA
                        mlb_game.iloc[i, batter] = y2009.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0 :
                            mlb_game.iloc[i , batter] = 'null'
                    else:
                        pass

        if year == '2011':
            if mlb_game.iat[i, batter] not in [i for i in y2010['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2010['woba'].median()# 沒有WOBA的放中位數
            else:
                for ii in range(y2010.shape[0]):
                    if mlb_game.iat[i, batter] == y2010.iat[ii, 1] : #換WOBA
                        mlb_game.iloc[i, batter] = y2010.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0 :
                            mlb_game.iloc[i , batter] = 'null'
                    else:
                        pass

        if year == '2012':
            if mlb_game.iat[i, batter] not in [i for i in y2011['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2011['woba'].median()# 沒有WOBA的放中位數
            else:
                for ii in range(y2011.shape[0]):
                    if mlb_game.iat[i, batter] == y2011.iat[ii, 1] : #換WOBA
                        mlb_game.iloc[i, batter] = y2011.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0 :
                            mlb_game.iloc[i , batter] = 'null'
                    else:
                        pass

        if year == '2013':
            if mlb_game.iat[i, batter] not in [i for i in y2012['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2012['woba'].median()# 沒有WOBA的放中位數
            else:
                for ii in range(y2012.shape[0]):
                    if mlb_game.iat[i, batter] == y2012.iat[ii, 1] : #換WOBA
                        mlb_game.iloc[i, batter] = y2012.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0 :
                            mlb_game.iloc[i , batter] = 'null'
                    else:
                        pass

        if year == '2014':
            if mlb_game.iat[i, batter] not in [i for i in y2013['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2013['woba'].median()# 沒有WOBA的放中位數
            else:
                for ii in range(y2013.shape[0]):
                    if mlb_game.iat[i, batter] == y2013.iat[ii, 1] : #換WOBA
                        mlb_game.iloc[i, batter] = y2013.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0 :
                            mlb_game.iloc[i , batter] = 'null'
                    else:
                        pass
        if year == '2015':
            if mlb_game.iat[i, batter] not in [i for i in y2014['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2014['woba'].median()# 沒有WOBA的放中位數
            else:
                for ii in range(y2014.shape[0]):
                    if mlb_game.iat[i, batter] == y2014.iat[ii, 1] : #換WOBA
                        mlb_game.iloc[i, batter] = y2014.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0 :
                            mlb_game.iloc[i , batter] = 'null'
                    else:
                        pass

        if year == '2016':
            if mlb_game.iat[i, batter] not in [i for i in y2015['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2015['woba'].median()# 沒有WOBA的放中位數
            else:
                for ii in range(y2015.shape[0]):
                    if mlb_game.iat[i, batter] == y2015.iat[ii, 1] : #換WOBA
                        mlb_game.iloc[i, batter] = y2015.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0 :
                            mlb_game.iloc[i , batter] = 'null'
                    else:
                        pass

        if year == '2016':
            if mlb_game.iat[i, batter] not in [i for i in y2015['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2015['woba'].median()# 沒有WOBA的放中位數
            else:
                for ii in range(y2015.shape[0]):
                    if mlb_game.iat[i, batter] == y2015.iat[ii, 1] : #換WOBA
                        mlb_game.iloc[i, batter] = y2015.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0 :
                            mlb_game.iloc[i , batter] = 'null'
                    else:
                        pass

        if year == '2017':
            if mlb_game.iat[i, batter] not in [i for i in y2016['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2016['woba'].median()# 沒有WOBA的放中位數
            else:
                for ii in range(y2016.shape[0]):
                    if mlb_game.iat[i, batter] == y2016.iat[ii, 1] : #換WOBA
                        mlb_game.iloc[i, batter] = y2016.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0 :
                            mlb_game.iloc[i , batter] = 'null'
                    else:
                        pass

        if year == '2018':
            if mlb_game.iat[i, batter] not in [i for i in y2017['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2017['woba'].median()  # 沒有WOBA的放中位數
            else:
                for ii in range(y2017.shape[0]):
                    if mlb_game.iat[i, batter] == y2017.iat[ii, 1]:  # 換WOBA
                        mlb_game.iloc[i, batter] = y2017.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0:
                            mlb_game.iloc[i, batter] = 'null'
                    else:
                        pass
        if year == '2019':
            if mlb_game.iat[i, batter] not in [i for i in y2018['player_id']]:
                # print(mlb_game.iloc[i, batter])
                mlb_game.iloc[i, batter] = y2018['woba'].median()  # 沒有WOBA的放中位數
            else:
                for ii in range(y2018.shape[0]):
                    if mlb_game.iat[i, batter] == y2018.iat[ii, 1]:  # 換WOBA
                        mlb_game.iloc[i, batter] = y2018.iat[ii, 9]
                        if mlb_game.iat[i, batter] == 0:
                            mlb_game.iloc[i, batter] = 'null'
                    else:
                        pass

        # elif year == '2011':
        #     for ii in range(y2010.shape[0]):
        #         # print(mlb_game.iat[i, batter])
        #         if mlb_game.iat[i,batter] == y2010.iat[ii,1]:
        #             mlb_game.iat[i,batter] = y2010.iat[ii,9]
        #         else:
        #             mlb_game.iloc[i, batter] = -1
        # elif year == '2012':
        #     print(2012)
        #     for ii in range(y2011.shape[0]):
        #         if mlb_game.iat[i,batter] == y2011.iat[ii,1] :
        #             mlb_game.iat[i,batter] = y2011.iat[ii,9]
        #         else:
        #             mlb_game.iat[i, batter] = -1
        # elif year == '2013':
        #     print(2013)
        #     for ii in range(y2012.shape[0]):
        #         if mlb_game.iat[i,batter] == y2012.iat[ii,1] :
        #             mlb_game.iat[i,batter] = y2012.iat[ii,9]
        #         else:
        #             mlb_game.iat[i, batter] = -1
        # elif year == '2014':
        #     print(2014)
        #     for ii in range(y2013.shape[0]):
        #         if mlb_game.iat[i,batter] == y2013.iat[ii,1]:
        #             mlb_game.iat[i,batter] = y2013.iat[ii,9]
        #         else:
        #             mlb_game.iat[i, batter] = -1
        # elif year == '2015':
        #     print(2015)
        #     for ii in range(y2014.shape[0]):
        #         if mlb_game.iat[i,batter] == y2014.iat[ii,1]:
        #             mlb_game.iat[i,batter] = y2014.iat[ii,9]
        #         else:
        #             mlb_game.iat[i, batter] = -1
        # elif year == '2016':
        #     print(2016)
        #     for ii in range(y2015.shape[0]):
        #         if mlb_game.iat[i,batter] == y2015.iat[ii,1]:
        #             mlb_game.iat[i,batter] = y2015.iat[ii,9]
        #         else:
        #             mlb_game.iat[i, batter] = 0.23
        # elif year == '2017':
        #     print(2017)
        #     for ii in range(y2016.shape[0]):
        #         if mlb_game.iat[i,batter] == y2016.iat[ii,1]:
        #             mlb_game.iat[i,batter] = y2016.iat[ii,9]
        #         else:
        #             mlb_game.iat[i, batter] = -1
        # elif year == '2018':
        #     print(2018)
        #     for ii in range(y2017.shape[0]):
        #         if mlb_game.iat[i,batter] == y2017.iat[ii,1]:
        #             mlb_game.iat[i,batter] = y2017.iat[ii,9]
        #         else:
        #             mlb_game.iat[i, batter] = -1
        # elif year == '2019':
        #     print(2018)
        #     for ii in range(y2016.shape[0]):
        #         if mlb_game.iat[i,batter] == y2018.iat[ii,1]:
        #             mlb_game.iat[i,batter] = y2018.iat[ii,9]
        #         else:
        #             mlb_game.iat[i, batter] = -1
        # else:
        #     mlb_game.iat[i, batter] = -2






mlb_game.to_csv('test.csv',encoding='utf8',index=False)
