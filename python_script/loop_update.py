#!/usr/bin/env python3
# coding: utf-8
import time
import json

while 1:
    from download_sub import update
    update()
    print("waiting...")
    time.sleep(10)
