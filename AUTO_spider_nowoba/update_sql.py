import pandas as pd
import sqlalchemy


def update_sql(date):
    host = '1.tcp.jp.ngrok.io:23879'
    port = 23879
    user = 'yulin'
    password = 'clubgogo'
    db = 'MoneyBallDatabase'

    #日期切片處理
    # date = date.split('-')
    # year = int(date[0])-1
    # month = date[1]
    # day = int(date[2])
    # date1 = f'./to_ID/{year}{month}{day}_ID.csv'
    # print(date1)
    date1 = date

    engine = sqlalchemy.create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s") % (user, password, host, db))

    try:
        df = pd.read_csv(date1,sep=',')
        print(df)


        df.to_sql(name='AUTO_web_crawler',if_exists='append',con=engine,)
        '''
        fail的意思如果表存在，啥也不做

        replace的意思，如果表存在，刪了表，再建立一個新表，把數據插入
        
        append的意思，如果表存在，把數據插入，如果表不存在創建一個表！！
        '''
        print("Write to MySQL successfully!")

    except Exception as e:
        print("載入失敗")
        print(e)


if __name__ == '__main__':
    update_sql()