import pymysql
import pathlib
import csv
import pandas as pd
from sqlalchemy import create_engine
#在python打sql指令套件 pip install mysql-connector-python
import mysql.connector
from MLB_date import date_search
import os  #確認檔案存在與否


# #使用csv reader 以list輸出csv [DictReader]則是以字典型態輸出
# with open('./scv_to_sql/game20100609.csv','r',encoding='utf-8',newline='') as s:
#     rows = csv.reader(s)
#     for row in rows :
#         print(row)
#
#
# #使用pandas pd.read.csv
# with open('./scv_to_sql/game20100609.csv','r',encoding='utf-8') as s:
#     rows = pd.read_csv(s)
#     print(rows)

'''
用mysql.connector 建立sqltable   最後記得commit()
'''
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

#
#
#
# for date in date_search() :
#     df = pd.read_csv(f'game{date}.csv',encoding='utf-8-sig')
#     header = list(df.columns)  #取欄位名稱
#     content_list = df.values
#     # print(header)
#
#     #依照CSV檔表頭設定
#     # header_str = ''
#     # for i in header:
#     #     header_str += '{},'.format(i)   #同 f'{i},'
#     # # print(header_str)
#     # header_str = header_str.strip(',')  #去除字尾,
#     # print(type(header_str))
#     # print(header_str)
#
#     #手動設定
#     header_str = '''date,time,matchup,1top,1bot,2top,2bot,3top,3bot,4top,4bot,5top,5bot,away_total,home_total,Umpires,Venue,away_pitcher, home_pitcher,
#                     away_1,away_2,away_3,away_4,away_5,away_6,away_7,away_8,away_9,
#                     home_1,home_2,home_3,home_4,home_5,home_6,home_7,home_8,home_9'''
#     print(header_str)
#
#     for j in range(df.shape[0]):
#         rows_list = []
#         for k in range(df.shape[1]):
#             rows_list.append(df.iat[j , k])
#
#         # print(rows_list)
#
#         insert_rows = ''
#         for row in rows_list :
#             if row == None:
#                 insert_rows += f'{row}'
#             elif type(row) == str :
#                 insert_rows += f'"{row}",'
#             else:
#                 row = str(row)
#                 insert_rows += f'{row},'
#
#         # print(insert_rows)
#         insert_rows = insert_rows.strip(',')
#         # print(insert_rows)
#
#
#         sql_insert = 'INSERT INTO mlb_test ({}) VALUES ({})'.format(header_str,insert_rows)
#         # print(sql_insert)
#         try:
#             cursor.execute(sql_insert)
#             print('寫入成功:{}'.format(sql_insert))
#         except:
#             print('寫入失敗')
#
#     # cursor.execute('DROP TABLE mlb_test')#一樣用db.commit()執行 並結束
#
#     MLBdb.commit()






''' CREATE TABLE'''
cursor.execute("""CREATE TABLE MLB_game (sid INT(10) AUTO_INCREMENT PRIMARY KEY, date DATE NOT NULL , time TIME NOT NULL ,matchup VARCHAR(25) NOT NULL , 1top INT(10) NOT NULL,
               1bot INT(10) NOT NULL , 2top INT(10) NOT NULL , 2bot INT(10) NOT NULL , 3top INT(10) NOT NULL , 3bot INT(10) NOT NULL ,
               4top INT(10) NOT NULL , 4bot INT(10) NOT NULL , 5top INT(10) NOT NULL , 5bot INT(10) NOT NULL , away_total INT(10) NOT NULL ,
               home_total INT(10) NOT NULL , Umpires VARCHAR(45) NOT NULL , Venue VARCHAR(45) NOT NULL , away_pitcher VARCHAR(45) NOT NULL , home_pitcher VARCHAR(45) NOT NULL ,
               away_1 VARCHAR(45) NOT NULL , away_2 VARCHAR(45) NOT NULL , away_3 VARCHAR(45) NOT NULL , away_4 VARCHAR(45) NOT NULL , away_5 VARCHAR(45) NOT NULL , 
               away_6 VARCHAR(45) NOT NULL , away_7 VARCHAR(45) NOT NULL , away_8 VARCHAR(45) NOT NULL , away_9 VARCHAR(45) NOT NULL , home_1 VARCHAR(45) NOT NULL , 
               home_2 VARCHAR(45) NOT NULL , home_3 VARCHAR(45) NOT NULL ,home_4 VARCHAR(45) NOT NULL , home_5 VARCHAR(45) NOT NULL , home_6 VARCHAR(45) NOT NULL , 
               home_7 VARCHAR(45) NOT NULL , home_8 VARCHAR(45) NOT NULL , home_9 VARCHAR(45) NOT NULL
                )""")





# #create table
# cursor.execute("CREATE TABLE users (name VARCHAR(255), age INTEGER(99), user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
# #insert資料進資料庫
# sqlStuff = "INSERT INTO users (name, age) VALUES (%s,%s)"
# records = [("Steve", 24),
#            ("Max", 25),
#            ("Chang" ,26),]
# cursor.executemany(sqlStuff, records)
# MLBdb.commit()
#
#
# cursor.execute('CREATE TABLE MLBtest (date NOT NULL)')



'''
用pandas將dateframe insert進mysql
'''
# engine = create_engine('mysql+pymysql://root:root@localhost:3306/db01')
# df = pd.read_csv('./scv_to_sql/game20100609.csv', sep=',',encoding='utf-8')
# 將新建的DataFrame儲存為MySQL中的數據表，不儲存index列
# df.to_sql('mpg', engine, index= False)
# print("Write to MySQL successfully!")




# #寫入hostname 帳號 密碼  資料庫名稱
# db = pymysql.connect('localhost','root','root','db_01')
# #建立cursor物件
# cursor = db.cursor()
#
# #cursor.execute('SQL語法')
# cursor.execute('SELECT VERSION()')
#
# data =cursor.fetchone()
# print(data)