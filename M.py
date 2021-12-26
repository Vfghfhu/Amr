import sys
num=sys.argv[1]
code=sys.argv[2]
import requests,json
'''
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
url = "https://mab.etisalat.com.eg:11003/Saytar/rest/quickAccess/verifyCodeQuickAccess"

headers = CaseInsensitiveDict()
headers["applicationVersion"] = "2"
headers["applicationName"] = "MAB"
headers["Accept"] = "text/xml;charset=UTF-8"
headers["applicationPassword"] = "ZFZyqUpqeO9TMhXg4R/9qs0Igwg="
headers["APP-BuildNumber"] = "468"
headers["APP-Version"] = "22.7.1"
headers["OS-Type"] = "Android"
headers["OS-Version"] = "9"
headers["APP-STORE"] = "GOOGLE"
headers["Is-Corporate"] = "false"
headers["Content-Type"] = "text/xml;charset=UTF-8"
headers["Content-Length"] = "193"
headers["Host"] = "mab.etisalat.com.eg:11003"
headers["Connection"] = "Keep-Alive"
headers["Accept-Encoding"] = "gzip"
headers["User-Agent"] = "okhttp/3.12.8"
headers["ADRUM_1"] = "isMobile:true"
headers["ADRUM"] = "isAjax:true"

data = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><verifyCodeQuickAccessRequest><dial>"+num+"</dial><udid>"+uid+"</udid><verCode>"+code+"</verCode></verifyCodeQuickAccessRequest>"

ah=requests.post(url, headers=headers, data=data,proxies={"http": proxy, "https": proxy},timeout=5).text

password=ah.replace('<?xml version="1.0" encoding="UTF-8"?><verifyCodeQuickAccessResponse><status>true</status><pass>','').replace('</pass></verifyCodeQuickAccessResponse>','')

if 'pass' in ah :
	import requests
	from requests.structures import CaseInsensitiveDict
	url = "https://mab.etisalat.com.eg:11003/Saytar/rest/quickAccess/loginQuickAccessWithPlan"
	to=num+','+uid+':'+password
	import base64
	akk=base64.b64encode(to.encode('utf-8'))
	headers = CaseInsensitiveDict()
	headers["applicationVersion"] = "2"
	headers["applicationName"] = "MAB"
	headers["Accept"] = "text/xml;charset=UTF-8"
	headers["applicationPassword"] = "ZFZyqUpqeO9TMhXg4R/9qs0Igwg="
	headers["Authorization"] ="Basic "+akk.decode('utf-8')
	headers["APP-BuildNumber"] = "468"
	headers["APP-Version"] = "22.7.1"
	headers["OS-Type"] = "Android"
	headers["OS-Version"] = "9"
	headers["APP-STORE"] = "GOOGLE"
	headers["Is-Corporate"] = "false"
	headers["Content-Type"] = "text/xml;charset=UTF-8"
	headers["Content-Length"] = "269"
	headers["Host"] = "mab.etisalat.com.eg:11003"
	headers["Connection"] = "Keep-Alive"
	headers["Accept-Encoding"] = "gzip"
	headers["User-Agent"] = "okhttp/3.12.8"
	headers["ADRUM_1"] = "isMobile:true"
	headers["ADRUM"] = "isAjax:true"
	data = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginWlQuickAccessRequest><firstLoginAttempt>true</firstLoginAttempt><modelType>Redmi 8A</modelType><osVersion>9</osVersion><platform>Android</platform><wlUdid>"+uid+"</wlUdid></loginWlQuickAccessRequest>"
	ii=requests.post(url, headers=headers, data=data,proxies={"http": proxy, "https": proxy},timeout=5).headers['Set-Cookie'].split()[0]+' path=/; HttpOnly'
	#######
	import requests
	from requests.structures import CaseInsensitiveDict
	url = "https://mab.etisalat.com.eg:11003/Saytar/rest/servicemanagement/submitOrder"
	headers = CaseInsensitiveDict()
	headers["applicationVersion"] = "2"
	headers["applicationName"] = "MAB"
	headers["Accept"] = "text/xml"
	headers["applicationPassword"] = "ZFZyqUpqeO9TMhXg4R/9qs0Igwg="
	headers["Cookie"] = ii
	headers["APP-BuildNumber"] = "336"
	headers["APP-Version"] = "20.19.0"
	headers["OS-Type"] = "Android"
	headers["OS-Version"] = "8.1.0"
	headers["APP-STORE"] = "GOOGLE"
	headers["Is-Corporate"] = "false"
	headers["Content-Type"] = "text/xml; charset=UTF-8"
	headers["Content-Length"] = "253"
	headers["Host"] = "mab.etisalat.com.eg:11003"
	headers["Connection"] = "Keep-Alive"
	headers["Accept-Encoding"] = "gzip"
	headers["User-Agent"] = "okhttp/3.12.8"
	headers["ADRUM_1"] = "isMobile:true"
	headers["ADRUM"] = "isAjax:true"
	data = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>"+num+"</msisdn><operation>RENEW</operation><productName>REESE_BUNDLE_10</productName></submitOrderRequest>"
	amr=requests.post(url, headers=headers, data=data,proxies={"http": proxy, "https": proxy},timeout=5).text
	if '<errorCode>' in amr:
		print('bad luck')
	elif 'Forbidden' in amr:
		print('bad luck')
	else:
			print('Done add 8GB')
			
else:
	print('error code')
	

















