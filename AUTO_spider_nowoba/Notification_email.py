import smtplib
from email.mime.text import MIMEText

def email(str):
    gmail_user = 'monkey811231@gmail.com'
    gmail_password = 'kvpblexhnheigesl' # google for python password

    msg = MIMEText('爬蟲已完成!!!!')
    msg['Subject'] = f'{str} is finish.'
    msg['From'] = gmail_user
    msg['To'] = gmail_user

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()

    print('Email sent!')
