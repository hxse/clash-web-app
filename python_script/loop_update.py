#!/usr/bin/env python3
# coding: utf-8
import time
import json
import importlib
#from download_sub import update
import download_sub

timeout=60*60*6 #秒
first=True
while 1:
    download_sub.update()
    print("waiting...")
    time.sleep(timeout)
    importlib.reload(download_sub)
