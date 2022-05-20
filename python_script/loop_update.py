#!/usr/bin/env python3
# coding: utf-8
import time
import importlib
import download_sub


while 1:
    download_sub.update()
    print("waiting...")
    loop_timeout = download_sub.loop_timeout
    time.sleep(loop_timeout)
    importlib.reload(download_sub)
