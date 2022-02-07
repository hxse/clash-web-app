# clash-web-app

* 下载安装 [winsw](https://github.com/winsw/winsw/releases) 并且添加到环境变量
* 下载安装 [subconverter](https://github.com/tindy2013/subconverter/releases/tag/v0.7.1) 配置好路径, 在配置文件里 convert填入api, ""留空则直接请求url不会转换
* 把`clash-web-app`添加到环境变量
* cd clash-web-app root path
* install `install winsw.bat`
* add to start up: `run winsw.bat`
* run switch clash: `rsc <key|name>`
* windows 重载配置文件 restful api

  * `curl -X PUT -H "Content-Type:application/json" -d "{\"path\":\"D:\\clash\\config.yaml\"}" http://127.0.0.1:9090/configs`

# 配置文件示例
```
{
    "origin": ".\\config\\<name>.yaml",
    "target": ".\\config\\current.yaml",
    "convert": "http://127.0.0.1:25500/sub?target=clash&url=",
    "timeout": 6,
    "last_time": "",
    "subscription": [
        {
            "name": "<name>.yaml",
            "url": "<your url>",
            "alias": "<your key>"
        },
        {
            "name": "<name>.yaml",
            "url": "<your url>",
            "alias": "<your key>"
        }
    ]
}
```