from bs4 import BeautifulSoup   #从BeautifulSoup4(bs4)库里导入BeautifulSoup模块
from urllib import request  #从urllib库里导入request模块
import re   #导入正则表达式模块re模块
import time     #导入time模块
 
url = "https://www.zhihu.com/question/64252714"
html = request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
 
 
links = soup.find_all('img', 'origin_image zh-lightbox-thumb', src = re.compile(r'jpg$'))
print(links)
 
path = r'D:\软件测试\软件测试教案\wallpaper'      #保存到某个文件夹下
for link in links:
    print(link.attrs['src'])
    request.urlretrieve(link.attrs['src'], path + '\%s.jpg' % time.time())