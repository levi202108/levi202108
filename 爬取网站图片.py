from bs4 import  BeautifulSoup
import re
import requests
import urllib
url="https://www.tupianzj.com/meinv/mm/xgswmn/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
res1=requests.get(url=url,headers=header)
patten=re.compile('img src="(.*?)"',re.S)
result=re.findall(patten,res1.text)
num=1
for i in result:
    # print("https:"+i)
    res=requests.get(url=i,headers=header)
    with open('img/%d.jpg'%num,'wb+') as f:
        f.write(res.content)
    num=num+1
