'''
pip install mysql-connector-python
'''
import mysql.connector

#👇👇起手式👇👇
name1 = mysql.connector.connect(
    host='1.tcp.jp.ngrok.io',
    port=23879,
    user='yulin',
    password='clubgogo',
    database='MoneyBallDatabase'
)
cursor = name1.cursor()  #cursor變數可以自己改 但通常不改



#開始下SQL指令
sql_command = 'SELECT * FROM mlb_game WHERE away_pitcher="CC Sabathia" ' #輸入sql指令不用加;
cursor.execute(sql_command)  #執行sql指令
result = cursor.fetchall()   #如果下select 可以用cursor.fetchall()來輸出結果
print(result)

name1.commit() #如果有對資料庫做修改需要加 name1.commit()讓SQL儲存剛剛執行的動作(我創建table時沒打這行也可以建 不過保險起見我現在都會加)

cursor.close() #關掉與MySQL的連結