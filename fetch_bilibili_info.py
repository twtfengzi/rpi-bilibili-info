# -*- coding:utf-8 -*-
import json

import config
from lib.httpclient import HttpClient


class FetchBilibiliInfo:

    bilibili_client = HttpClient().New(config.bilibili_host)

    def fetch_my_follower(self):
        self.bilibili_client.request("GET", "/x/relation/stat?vmid="+str(config.my_bilibili_uid)+"&jsonp=jsonp")
        resp = self.bilibili_client.getresponse().read().decode("utf-8")
        my_follow = json.loads(resp)
        return my_follow['data']


if __name__ == '__main__':
    print(FetchBilibiliInfo().fetch_my_follower())
