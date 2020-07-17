import pandas as pd
import numpy as np
import time


def insert_woba(csv_path):
    start = time.time()
    '''
    讀mlb_game 切片date取year 刪除date已取出的year取代
    '''
    mlb_game = pd.read_csv(f'{csv_path}',encoding='utf-8',index_col=False)
    mlb_game.to_csv(f'./merge/merge{csv_path[12:20]}.csv',index=0)

    '''
    處理game{year}{month}{day}_ID.csv
    '''
    batter_year = pd.read_csv('./data/batter_data_2018.csv',encoding='utf-8',index_col=False)
    #換型態
    med = batter_year.loc[:,['woba']].median()[0]
    print(med)
    batter_year['player_id']=batter_year['player_id'].astype(str)
    x_3f = lambda x:'%.3f'%x
    batter_year['woba']=batter_year['woba'].map(x_3f).astype(str)

    batter_year = batter_year.loc[:,['player_id','woba']] #只取batter_9years需要的欄位 為了merge




    for batter_location in mlb_game.columns.values[19:37]: #此FOR迴圈是為了 依序對18個棒次做merge
        # print(batter_location)

        mlb_game = pd.read_csv(f'./merge/merge{csv_path[12:20]}.csv') #開啟我們整理好的檔案(left merge 的left) 每個迴圈都要開 如果不每個loop做此步驟 此loop裡的每次都會去開新的

        #將型別轉換(為了跟要merge的對象型別一致)
        mlb_game[f'{batter_location}'] = mlb_game[f'{batter_location}'].astype(str)

        merge_data = pd.merge(mlb_game,batter_year,left_on=[f'{batter_location}'],right_on=['player_id'],how='left').drop('player_id',axis=1)
        merge_data.rename(columns = {'woba':f'{batter_location}_woba'} , inplace=True)
        merge_data.to_csv(f'./merge/merge{csv_path[12:20]}.csv',index=False,na_rep=f'{med}')

    finish = time.time()
    total = finish - start
    print(f'./merge/merge{csv_path[12:20]}.csv檔案製作完成')
    print(f'merge完成,花費 {total:.2f} 秒\n')

if __name__ == "__main__":
    insert_woba()