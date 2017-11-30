#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import os
import webbrowser
#网址
url = "http://www.baidu.com"
#请求
request = urllib.request.Request(url)
#爬取结果
response = urllib.request.urlopen(request)
#读取结果
data = response.read()
#设置解码方式
data = data.decode('utf-8')
#获取绝对路径
path = os.path.abspath('')
dirpath = os.path.join(path,'spider')
#创建文件
dir = os.mkdir(dirpath)
Txtpath = os.path.join(dirpath,'test3.html')
Txt =  open(Txtpath,'w',encoding='utf-8')
#写入数据
Txt.write(data)
# Txt.closed()



