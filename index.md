# Linux 下通过命令行发送微博

## 安装 weibo python sdk

* 项目地址: [sinaweibopy](http://github.liaoxuefeng.com/sinaweibopy/)

```
pip install sinaweibopy
```

## 申请微博个人开发者

* [微博开放平台](http://open.weibo.com/apps)

申请之后创建应用获取 `App Key` 和 `App Secret`，填入代码中指定行即可

## 获取授权，发送微博

```
$ python post_weibo.py 
https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//www.weibo.com&response_type=code&client_id=2339560670
拷贝以上链接输入浏览器填写 URL 获取 code [回车结束]: 65be734e2b1e0ae75f9b19a8a5ff7386
输入你想要发送的微博内容："hello world！"
```

现在访问你的微博主页，就可以查看刚刚发送的内容了，赶快行动吧 ^_^