#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weibo import APIClient

APP_KEY = '待写入'
APP_SECRET = '待写入'                   # APP_KEY 和 APP_SECRET 通过创建应用获取
CALLBACK_URL = 'http://www.weibo.com'   # 和 OAuth2.0 授权设置网页一致

# 获取微博授权
def get_access_code():
    client = APIClient(app_key=APP_KEY,
                       app_secret=APP_SECRET,
                       redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    print url
    code = raw_input('拷贝以上链接输入浏览器填写 URL 获取 code [回车结束]: ')
    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in
    client.set_access_token(access_token, expires_in)
    return client

# 发送微博
def post_weibo(client):
    content = raw_input('输入你想要发送的微博内容：')
    ucontent = unicode(content, "UTF-8")
    client.statuses.update.post(status=ucontent)

if __name__ == '__main__':
     client = get_access_code()
     post_weibo(client)
