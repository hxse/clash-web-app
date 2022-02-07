#!/usr/bin/env python3
# coding: utf-8
import time
import json
from download_sub import update

while 1:
    with open("config/config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
    update(config["origin"])
    print("waiting...")
    time.sleep(60 * 6)
