#!/usr/bin/env python
# coding=utf-8
import urllib.request
import os
import ssl
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, AdaptiveETA, AbsoluteETA, AdaptiveTransferSpeed

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


class Downloader(object):
    count=0         # 定义类属性
    def __init__(self, toDir):
        self.toDir = toDir
        self.pbar = ProgressBar(widgets=[Percentage(), Bar()], max_value=100)

    def mkdir(self, path):
        path = path.strip()
        path = path.rstrip("\\")
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print(str(path) + " makes sucessfully !")
        # else:
            # print(str(path) + " already exists !")

    def schedule(self,a,b,c):
        '''''
         a:已经下载的数据块
         b:数据块的大小
         c:远程文件的大小
        '''
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        self.pbar.update(round(per,2))

    def donwnloading(self, url):
        Downloader.count += 1
        self.mkdir(self.toDir)
        fileName = url.split('/')[-1]
        local = os.path.join(self.toDir, fileName)
        local = local[:-1]
        if not os.path.exists(local):
            print(" donwnloading "+ str(Downloader.count) +" >> "+fileName)
            self.pbar.start()
            urllib.request.urlretrieve(url, local, self.schedule)
            self.pbar.finish()
        else:
            print(" donwnloaded "+ str(Downloader.count) +" >> "+fileName)

# URL = "https://data.ngdc.noaa.gov/instruments/remote-sensing/passive/spectrometers-radiometers/imaging/viirs/dnb_composites/v10//201711/vcmcfg/SVDNB_npp_20171101-20171130_00N060W_vcmcfg_v10_c201712040930.tgz"
# Downloader(r"/Users/yanmeng/Downloads").donwnload(URL)