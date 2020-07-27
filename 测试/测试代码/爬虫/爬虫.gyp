#coding=utf-8
from bs4 import BeautifulSoup
import requests
 
#使用requests抓取页面内容，并将响应赋值给page变量
html = requests.get('https://www.qiushibaike.com/text/')
 
#使用content属性获取页面的源页面
#使用BeautifulSoap解析，吧内容传递到BeautifulSoap类
soup = BeautifulSoup(html.content,'lxml')
#我是分隔符，下面就是select（）方法咯~ a.contentHerf > div > span 没有评论
links = soup.select('div > a >div >span')
#links = soup.find_all('div',class_='content')
 
#link的内容就是div，我们取它的span内容就是我们需要段子的内容
for link in links:
    print (link.get_text())
#    print (link.span.get_text())


