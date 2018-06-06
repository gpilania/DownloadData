#!/usr/bin/env python
# coding=utf-8

import crowler
import download
from bs4 import BeautifulSoup

# 提取数据并将提取的数据写入文件中
def getURL():
    url = "https://www.ngdc.noaa.gov/eog/viirs/download_dnb_composites_iframe.html"
    html = crowler.getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    ass = soup.find_all(["a"])

    f = open('/Users/yanmeng/Downloads/url_night_light.txt', 'w')
    for a in ass:
        if 'VCMCFG' in a.string:
            # print(a["href"])
            f.write(a["href"]+"\n")
    f.close()

# 从文件中读取url连接并进行下载
def getData(year, file, toDir):
    urls = []
    file = open(file)
    line = file.readline()
    while line:
        if year in line:
            print(line)
            urls.append(line)
        line = file.readline()
    file.close()
    # 遍历urls下载
    for url in urls:
        print("——————————————————————————————————————————————")
        download.Downloader(toDir).donwnloading(url)

year = "npp_201311"
getData(year, '/Users/yanmeng/Downloads/url_night_light.txt', '/Users/yanmeng/Downloads/'+year)




