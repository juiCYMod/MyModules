import sys
import time
import requests
import configparser

#順次機能追加予定

inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')

def stringer(string):
    mojisu = len(string)
    for i in range(mojisu):
        sys.stdout.write(string[i])
        sys.stdout.flush()
        time.sleep(0.025)

def line(message):
    url = "https://notify-api.line.me/api/notify"
    token = inifile.get('settings', 'token')
    headers = {"Authorization" : "Bearer "+ token}
    payload = {"message" :  message}
    try:
        r = requests.post(url ,headers = headers ,params=payload)
    except Exception as e:
        print(e) 

