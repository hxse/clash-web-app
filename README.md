# clash-web-app

* 下载安装 [winsw](https://github.com/winsw/winsw/releases) 并且添加到环境变量
* 把`clash-web-app`添加到环境变量
* cd clash-web-app root path
* install `install winsw.bat`
* add to start up: `run winsw.bat`
* run switch clash: `rsc <key|name>`
* windows 重载配置文件 restful api

  * `curl -X PUT -H "Content-Type:application/json" -d "{\"path\":\"D:\\clash\\config.yaml\"}" http://127.0.0.1:9090/configs`

