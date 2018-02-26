# coding=utf-8

import re
import requests


def get_ip():
    req = requests.get("http://ip.cn/", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }, timeout=8)
    value = re.findall("(\d+\.\d+\.\d+\.\d+)", req.content)
    if not value:
        return None
    return value[0]
