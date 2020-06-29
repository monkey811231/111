import pandas as pd
import numpy as np
import os


'''
建立資料夾 增加每個CSV的Session欄位 並合併成一個CSV
'''
# dir = 'nine_in_one'
# if not os.path.exists('./save/nine_in_one'):
#     os.mkdir('./save/nine_in_one')
#     print(f'已建立{dir}資料夾!')
# else:
#     print(f'{dir}資料夾已存在!')
#
# #新增session欄位 (只需修改2009~2008年度)
# for session in range(2009,2019):
#     df = pd.read_csv(f'./save/batter_data_{session}.csv',encoding='utf-8',index_col=False)
#     df['session'] = session+1    #增加session欄位 因為是要拿前一年的資料寫入 所以session要加1
#     df.to_csv(f'./save/nine_in_one/for_{session+1}.csv',encoding='utf-8',index=False)
#
#
# #將./save/nine_in_one 資料夾下的所有csv合併
# Folder_Path = f'C:/Users/monke/PycharmProjects/MLB/save/nine_in_one'     #######使用絕對路徑啊!!!!
# SaveFile_Path = f'C:/Users/monke/PycharmProjects/MLB/'
# SaveFile_Name = 'batter_9years.csv'
#
# #修改當前工作目錄
# os.chdir(Folder_Path)
# #將目錄下的csv標題製成一個list
# file_list = os.listdir()
# #讀取第一個檔案並寫包含表頭
# df_concat = pd.read_csv(f'{Folder_Path}/{file_list[0]}')
# #將讀取後的第一個檔案 寫入合併後的檔案儲存
# df_concat.to_csv(f'{SaveFile_Path}/{SaveFile_Name}',encoding='utf-8',index=False)
#
# #重複將csv檔案(除了第一個file_list[0])存合併進檔案儲存
# for i in range(1,len(file_list)):
#     df = pd.read_csv(f'{Folder_Path}/{file_list[i]}')
#     df.to_csv(f'{SaveFile_Path}/{SaveFile_Name}',encoding='utf_8',index=False,mode='a')    #切記mode='a' 不然會覆蓋掉全面

'''
讀mlb_game 切片date取year 刪除date已取出的year取代
'''
mlb_game = pd.read_csv('./for_last_test/mlb_game_v1.csv',encoding='utf-8',index_col=False)
#切片date 刪除date 新增Session
sessions = mlb_game.loc[:,'date']
session_list = []
for session in sessions :
    year = session.split('-')[0]
    session_list += [year]

mlb_game = mlb_game.drop('date', axis = 1) #刪除data欄位
mlb_game.insert(1,'session',np.array(session_list)) #新增session欄位
mlb_game.to_csv('merge.csv',index=0)
# print(mlb_game.columns.values)

'''
處理batter_9years(batter_data九年分的CSV合併後的CSV) 
'''
batter_9years = pd.read_csv('batter_9years.csv',encoding='utf-8',index_col=False)
#換型態
batter_9years['session']=batter_9years['session'].astype(str)
batter_9years['player_id']=batter_9years['player_id'].astype(str)
batter_9years['woba']=batter_9years['woba'].astype(str)

batter_9years = batter_9years.loc[:,['session','player_id','woba']] #只取batter_9years需要的欄位 為了merge
# batter_9years = batter_9years['session'] #取單個值可以直接Dataframe[column]



for batter_location in mlb_game.columns.values[6:24]: #此FOR迴圈是為了 依序對18個棒次做merge

    mlb_game = pd.read_csv('merge.csv') #開啟我們整理好的檔案(left merge 的left) 每個迴圈都要開 如果不每個loop做此步驟 此loop裡的每次都會去開新的

    #將型別轉換(為了跟要merge的對象型別一致)
    mlb_game['session'] = mlb_game['session'].astype(str)
    mlb_game[f'{batter_location}'] = mlb_game[f'{batter_location}'].astype(str)

    merge_data = pd.merge(mlb_game,batter_9years,left_on=['session','{0}'.format(batter_location)],right_on=['session','player_id'],how='left').drop('player_id',axis=1)
    merge_data.rename(columns = {'woba':f'{batter_location}_woba'} , inplace=True)
    merge_data.to_csv('merge.csv',index=0,na_rep='NA')
