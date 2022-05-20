#!/usr/bin/env python3
# coding: utf-8
import grequests  # making sure grequests is the first imported module https://github.com/spyoungtech/grequests/issues/150
import requests
import fire
import json
import os
from pathlib import Path
import datetime

configPath = Path("./config/config.json")
if not configPath.is_file():
    raise "请创建配置文件或检查目录"
with open(configPath, "r", encoding="utf-8") as file:
    config = json.load(file)
    print(config)


def convert_timeout(time):
    timeout = 1
    if str(type(time)) == "<class 'str'>":
        for i in time.split("*"):
            if i.strip():
                timeout = timeout * int(i.strip())
    else:
        timeout = time
    return timeout


loop_timeout = convert_timeout(config["loop_timeout"])


def hard_link(origin, target):
    # 不要用软链接, 因为clash不支持快捷方式
    origin = Path(origin)
    target = Path(target)
    if not origin.is_file():
        raise "源文件不存在,请输入正确路径"
    if target.is_file():
        target.unlink()
    origin.link_to(target)


def set_meta(meta):
    def hook(r, *args, **kwargs):
        r.meta = meta
        return r

    return hook


def get_config():
    get_url = (
        lambda x: x["url"] if not config["convert"] else config["convert"] + x["url"]
    )
    get_meta = lambda x: {"name": x["name"]}
    reqArr = [
        grequests.get(
            get_url(subs), callback=set_meta(get_meta(subs)), timeout=config["timeout"]
        )
        for subs in config["subscription"]
    ]
    print("start requests length:", len(reqArr))
    resArr = grequests.imap(reqArr, size=10)
    for res in resArr:
        if res.status_code == 200:
            print("订阅返回成功", res.meta["name"], res.url)
            with open("config/" + res.meta["name"], "w", encoding="utf8") as f:
                f.write(res.text)
        else:
            print("订阅返回失败", res.meta["name"], res.url)

    print("end")


def reload_config(path, url="http://127.0.0.1:9090/configs"):
    requests.put(url, json={"path": path})


def get_alias(key):
    for i in config["subscription"]:
        if key == i["alias"]:
            return f'.\\config\\{i["name"]}'
    return key


def update(origin=config["origin"], update=True, reload=True):
    # origin: 指定配置文件
    # update: 下载更新订阅
    # reload: 重载配置文件
    origin = get_alias(origin)
    if update:
        get_config()
    hard_link(origin, config["target"])

    # 如果指定参数则更新配置文件里的默认参数
    if update:
        config["last_time"] = f"{datetime.datetime.now()}"
    if origin != config["origin"]:
        config["origin"] = origin
    if update or origin != config["origin"]:
        with open(configPath, "w", encoding="utf-8") as file:
            json.dump(config, file, ensure_ascii=False, indent=4)

    if reload:
        fullPath = Path(origin).resolve()
        reload_config(str(fullPath))
        print("reload:", fullPath)


if __name__ == "__main__":
    fire.Fire(update)
