#Functions & Calls

import requests,uuid,secrets
import requests
from time import sleep
import os
import sys as n
import time as mm
from time import sleep

#Code slow
count = 0
def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(2. / 200)
        
 #Code      
os.system("clear")
uid = uuid.uuid4()
RED     = '\033[31m'
GREEN   = '\033[32m'
BLACK   = '\033[30m'
WHITE   = '\033[37m'
MAGENTA = '\033[35m'
r = requests.Session()
Dev =	'This tool by tofe x'
cookie = secrets.token_hex(8)*2
slow("""\033[35m\t\t|¯/ /¯\ |\| |¯\   | |\| |¯  ¯|¯ /¯\ 
\t\t|¯/ |¯| | | |_/   | | |  ¯|  |  |¯| 
\t         ¯                       ¯          
\tTelegram : @AsofeQ             Instagram : zb._c \n =================================================================\n """)

import webbrowser
sleep(2)
webbrowser.open("https://t.me//py_iq")
slow("""\n\t\t\tLogin Your account\n""") 
username = input("\n\t\t\tEnter your user : ")
password = input('\n\t\t\tyour password :  ')
target = input('\033[37m\n\t\t\ttarget :  ')
sle = int(input('\n\t\t\tsleep (\033[31mPreferably 15 - 25\033[37m) : '))
def login():
    global username
    global password
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
    data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
    req_login = r.post(url,headers=headers,data=data)
    if ("userId") in req_login.text:
        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
        print("\n \033[32mLogin True \n ")
        print("\t\t List of reports\n")
        url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
        req_id = r.get(url_id).json()
        user_id = str(req_id['logging_page_id'])
        idd = user_id.split('_')[1]
        done = 1
        while True:
            url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
            datas = {'source_name':'','reason_id':1,'frx_context':''} #spam
            report = r.post(url_report,data=datas)
            print('\033[31m \t\tdone spam {}'.format(done))
            sleep(sle)
            done += 1
    else:
        print('\033[31mlogin false')
        exit()

login()

