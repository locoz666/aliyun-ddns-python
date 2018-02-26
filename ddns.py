import time
import json
import logging
import requests
import traceback
from config import *
from log import init_log
from aliyunsdkcore import client
from importlib import import_module
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest, DescribeDomainRecordInfoRequest

init_log()


class DDNS(object):
    def __init__(self):
        self.client = client.AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET)

        self.get_old_ip_req = DescribeDomainRecordInfoRequest.DescribeDomainRecordInfoRequest()
        self.get_old_ip_req.set_RecordId(RC_RECORD_ID)
        self.get_old_ip_req.set_accept_format("json")

        self.set_new_ip_req = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
        self.set_new_ip_req.set_RR(RC_RR)
        self.set_new_ip_req.set_Type(RC_TYPE)
        self.set_new_ip_req.set_RecordId(RC_RECORD_ID)
        self.set_new_ip_req.set_TTL(RC_TTL)
        self.set_new_ip_req.set_accept_format("json")

    def get_now_ip(self):
        for source in json.loads(SOURCES):
            try:
                source_api = import_module("ex.{}".format(source))
                now_ip = source_api.get_ip()
                if now_ip:
                    logging.debug("{} get ip {}".format(source, now_ip))
                    return now_ip
            except requests.ConnectTimeout:
                logging.error("{} timeout".format(source))
            except:
                logging.debug("{} error {}".format(source, traceback.format_exc()))
                logging.error("{} error".format(source))

    def get_old_ip(self):
        result = self.client.do_action_with_exception(self.get_old_ip_req)
        js = json.loads(result)
        return str(js["Value"])

    def update_dns(self, new_ip):
        self.set_new_ip_req.set_Value(new_ip)
        self.client.do_action_with_exception(self.set_new_ip_req)
        logging.info("update {}".format(new_ip))

    def run(self):
        while True:
            try:
                old_ip = self.get_old_ip()
                now_ip = self.get_now_ip()
                if old_ip != now_ip:
                    self.update_dns(now_ip)
                time.sleep(float(UPDATE_INTERVAL))
            except:
                logging.error(traceback.format_exc())


if __name__ == '__main__':
    DDNS().run()
