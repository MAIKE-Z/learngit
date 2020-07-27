# 网页下载器代码示例
import urllib

url = "http://www.baidu.com"

print("第一种方法: 直接访问url")
response1 = urllib.request.urlopen(url)
print(response1.getcode())  # 状态码
print(len(response1.read()))  # read读取utf-8编码的字节流数据

print("第二种方法: 设置请求头，访问Url")
request = urllib.request.Request(url)  # 请求地址
request.add_header("user-agent", "mozilla/5.0")  # 修改请求头
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

import http.cookiejar  # 不知道这是啥

print("第三种方法: 设置coockie，返回的cookie")
# 第三种方法的目的是为了获取浏览器的cookie内容
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(len(response3.read()))
print(cj)  # 查看cookie的内容