# coding=utf-8
import os

ENV = os.environ

# 用来获取IP的平台
SOURCES = ENV.get("SOURCES", '["taobao", "ipip_net", "ip_cn"]')

# 刷新间隔，单位秒
UPDATE_INTERVAL = ENV["UPDATE_INTERVAL"]
# Access Key ID
ACCESS_KEY_ID = ENV["ACCESS_KEY_ID"]
# Access Key Secret
ACCESS_KEY_SECRET = ENV["ACCESS_KEY_SECRET"]
# 账号ID
ACCOUNT_ID = ENV["ACCOUNT_ID"]
# 一级域名
RC_DOMAIN = ENV["RC_DOMAIN"]
# 解析记录
RC_RR = ENV["RC_RR"]
# 记录类型
RC_TYPE = ENV["RC_TYPE"]
# 解析记录ID
RC_RECORD_ID = ENV["RC_RECORD_ID"]
# TTL，单位秒
RC_TTL = ENV["RC_TTL"]
