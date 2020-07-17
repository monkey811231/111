import time
import datetime
import pytz
from AUTO_spider_nowoba import last_v1,Name_to_ID,insert_WOBA_merge,Notification_email,update_sql
import os


def main():

    while True :
        #取台灣時間
        TW_date_localtime = time.localtime() #time.struct_time(tm_year=2020, tm_mon=7, tm_mday=9, tm_hour=17, tm_min=10, tm_sec=48, tm_wday=3, tm_yday=191, tm_isdst=0)
        TW_date_raw = time.strftime('%Y-%m-%d', TW_date_localtime)

        #取用美東時區
        us = pytz.timezone('US/Eastern')
        # US_date_raw = datetime.datetime.strptime(str(a),'%Y-%m-%d %H:%M:%S').replace(tzinfo=us)
        US_datetime_raw = str(datetime.datetime.now(us)).split(' ') #取美東時間分片成 日期 跟 時間
        US_date_raw = US_datetime_raw[0]
        US_time_raw = US_datetime_raw[1].split(':')[0:2]
        print(US_time_raw)

        # print('TW-date:' + TW_date_raw)
        print('\n\n ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('US-date:' + US_date_raw)

        # US_date_raw = '2019-07-11'   #for test 07/09=ALLSTART, 07/10=nogame
        if US_time_raw == ['00', '00']:  #重製每日URL
            start = time.time()
            with open('karioku.text','w',encoding='utf-8-sig'):
                print('Reset URL(karioku.text) List')

            print('\n執行爬蟲')
            spider_py = last_v1.spider(US_date_raw)
            if spider_py == None:
                print('無比賽')
            elif spider_py == 'No new URL':
                print('無新增賽事資訊')
            else:
                print('\n執行ID轉換')
                change_to_id = Name_to_ID.name_to_id(spider_py)


                print('\n送資料庫')
                update_sql.update_sql(change_to_id)

                #寄送email通知
                # Notification_email.email(US_date_raw)

                finish = time.time()
                total = finish-start
                print(f'⛩⛩⛩⛩⛩⛩⛩　完成 共計花費{total:.3f} 秒 🍌🍏🍊🍓🍇🍉❅')






        else:
            start = time.time()

            print('\n執行爬蟲')
            spider_py = last_v1.spider(US_date_raw)
            if spider_py == None:
                print('無比賽')
            elif spider_py == 'No new URL':
                print('無新增賽事資訊')


            else:
                print('\n執行ID轉換')
                change_to_id = Name_to_ID.name_to_id(spider_py)

                print('\n送資料庫')
                update_sql.update_sql(change_to_id)

                # 寄送email通知
                # Notification_email.email(US_date_raw)

                finish = time.time()
                total = finish - start
                print(f'⛩⛩⛩⛩⛩⛩⛩　完成 共計花費{total:.3f} 秒 🍌🍏🍊🍓🍇🍉❅')

        time.sleep(60)

if __name__ == '__main__':
    main()