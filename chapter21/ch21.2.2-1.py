# coding=utf-8
# 代码文件：chapter21/ch21.2.2-1.py

"""获得静态数据"""
import urllib.request

# url = 'https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'
# 换成自己到路径
url = "file:///C:/Users/tony/Desktop/chapter21/nasdaq-Apple1.html"
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    print(htmlstr)
