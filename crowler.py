#!/usr/bin/env python
# coding=utf-8
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        print(r.apparent_encoding)
        r.encoding = r.apparent_encoding

        return r.text
    except:
        print("产生异常")
        return "产生异常"

if __name__ == "__main__":
    url = "https://www.ngdc.noaa.gov/eog/viirs/download_dnb_composites.html#NTL_2015"
    print(getHTMLText(url))