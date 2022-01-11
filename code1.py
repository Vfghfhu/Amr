import sys
num=sys.argv[1]
'''
import requests,json

url = "https://proxy-orbit1.p.rapidapi.com/v1/"

querystring = {"protocols":"socks4"}

headers = {
    'x-rapidapi-key': "d8cd7b7d63msh6be235971b16bffp1676ecjsn0d1fd4d453e3",
    'x-rapidapi-host': "proxy-orbit1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

response = json.loads(response.text)
proxy = response['curl']

if 'https' in str(proxy):
	exit('try again')
if 'http' in str(proxy):
	exit('try again')

'''
nm=len(open("proxy.txt","r").readlines())
file = open("proxy.txt","r")
import random  
Content = file.read()
proxy=Content.split("\n")[random.randint(0,nm)]

import requests
from requests.structures import CaseInsensitiveDict
uid=open('u.txt',"r").read()
url = "https://mab.etisalat.com.eg:11003/Saytar/rest/quickAccess/sendVerCodeQuickAccessV2?sendVerCodeQuickAccessRequest=%3CsendVerCodeQuickAccessRequest%3E%3Cudid%3E"+uid+"%3C%2Fudid%3E%3Cdial%3E"+num+"%3C%2Fdial%3E%3C%2FsendVerCodeQuickAccessRequest%3E"

headers = CaseInsensitiveDict()
headers["applicationVersion"] = "2"
headers["Content-Type"] = "text/xml;charset=UTF-8"
headers["applicationName"] = "MAB"
headers["Accept"] = "text/xml"
headers["applicationPassword"] = "ZFZyqUpqeO9TMhXg4R/9qs0Igwg="
headers["APP-BuildNumber"] = "468"
headers["APP-Version"] = "22.7.1"
headers["OS-Type"] = "Android"
headers["OS-Version"] = "9"
headers["APP-STORE"] = "GOOGLE"
headers["Is-Corporate"] = "false"
headers["Host"] = "mab.etisalat.com.eg:11003"
headers["Connection"] = "Keep-Alive"
headers["Accept-Encoding"] = "gzip"
headers["User-Agent"] = "okhttp/3.12.8"
headers["ADRUM_1"] = "isMobile:true"
headers["ADRUM"] = "isAjax:true"


amr=requests.get(url, headers=headers,proxies={"http": proxy, "https": proxy},timeout=5).elapsed.total_seconds()
if amr <= 4:
        open("proxy.txt","+a").write(proxy+'''
''')
print("Done send")


