# -*- coding:utf-8 -*-
import http.client


class HttpClient:

    conn = None

    def New(self, host, timeout=3):
        self.conn = http.client.HTTPConnection(host, timeout=timeout)
        return self.conn
