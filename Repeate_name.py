import mysql.connector

# def main():


# def exception_handing(player_name):
#利用idreference
MLBdb = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'moneyballdatabase'
    )

cursor = MLBdb.cursor()

sql_command = 'SELECT * FROM id_reference '
cursor.execute(sql_command)
show = cursor.fetchall()
# print(show)

#製作球員:ID的dict
id_dic = {i[1]:i[0] for i in show }
print(id_dic)

sql_for_name = 'SELECT mlb_name FROM id_copy'
cursor.execute(sql_for_name)
aa = cursor.fetchall()

for i in aa :
    i = i[0]
    id_reference_value = id_dic[i]
    print(i,id_reference_value)  #名字.id
    if i=='Francisco Rodriguez':
        sql_for_match = 'select '
        cursor.execute()
        '2011LAA' or '2010LAA'


    elif i=='Chris Young' or i=='Chris Smith' \
        or i=='Luis Jimenez' or i=='Miguel Gonzalez' or i=='Javy Guerra' \
        or i=='Luis Perdomo' or i=='David Carpenter' or i=='Matt Reynolds' \
        or i=='Will Smith' or i=='Jose Ramirez' or i=='Austin Adams' \
        or i=='Daniel Robertson' or i=='Matt Duffy' :
        print('■■■■■■■重複名稱■■■■■■■')
        pass
    else:
        try:
            sql_unlock = 'SET SQL_SAFE_UPDATES=0'
            sql_update = f'UPDATE id_copy SET mlb_name={id_reference_value} WHERE mlb_name="{i}"'
            sql_lock = 'SET SQL_SAFE_UPDATES=1'
            cursor.execute(sql_unlock)
            cursor.execute(sql_update)
            cursor.execute(sql_lock)
            MLBdb.commit()
            print(sql_update)
        except:
            print(f'{i}已修改')

cursor.close()





