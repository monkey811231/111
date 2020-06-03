from MLB_date import date_search
from pathlib import Path
import pandas as pd
import mysql.connector
import concurrent.futures

MLBdb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'MoneyBallDatabase'
)
# MLBdb = mysql.connector.connect(
#     host = '1.tcp.jp.ngrok.io',
#     port = 23879,
#     user = 'yulin',
#     password = 'clubgogo',
#     database = 'MoneyBallDatabase'
# )
cursor= MLBdb.cursor()


# def to_MySQL(date):
for date in date_search():
    date = date
    if Path(f'game_Folder/game{date}.csv').exists():
        print(f'insert{date}.csv')
        df = pd.read_csv(f'game_Folder/game{date}.csv', encoding='utf-8-sig')



        # 手動設定
        header_str = '''date,time,matchup,1top,1bot,2top,2bot,3top,3bot,4top,4bot,5top,5bot,away_total,home_total,Umpires,Venue,away_pitcher, home_pitcher,
                            away_1,away_2,away_3,away_4,away_5,away_6,away_7,away_8,away_9,
                            home_1,home_2,home_3,home_4,home_5,home_6,home_7,home_8,home_9'''
        # print(header_str)

        for j in range(df.shape[0]):
            rows_list = []
            for k in range(df.shape[1]):
                rows_list.append(df.iat[j, k])

            # print(rows_list)

            insert_rows = ''
            for row in rows_list:
                if row == None:
                    insert_rows += f'{row}'
                elif type(row) == str:
                    insert_rows += f'"{row}",'
                else:
                    row = str(row)
                    insert_rows += f'{row},'


            insert_rows = insert_rows.strip(',')
            # print(insert_rows)

            sql_insert = 'INSERT INTO MLB_game ({}) VALUES ({})'.format(header_str, insert_rows)
            print(sql_insert)
            try:
                cursor.execute(sql_insert)
                print('寫入成功:{}'.format(date))
            except:
                print('寫入失敗')

            MLBdb.commit()
    else:
        print(f'無{date}檔案')



# def get_list():
#     date_list = []
#     for i in date_search():
#         date_list += [i]
#
#     with concurrent.futures.ProcessPoolExecutor(max_workers=8) as inserttoSQL:
#         inserttoSQL.map(to_MySQL,date_list)
#
#     print(f'\n{date_list[0]}~{date_list[-1]}已傳MySQL')
#
# if __name__ == '__main__':
#     get_list()



