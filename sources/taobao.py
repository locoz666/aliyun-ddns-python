# coding=utf-8

import requests


def get_ip():
    req = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip=myip", timeout=1)
    value = req.json()["data"]["ip"]
    if not value:
        return None
    return value
