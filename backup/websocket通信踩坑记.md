什么是websocket？网上有很多的介绍，比如[这里][1]。
如果在电脑端配置websocket服务器，python直接pip现成的模块就行，然后简单配置一下就可以运行了。但是目前我需要这个服务器运行在单片机上，这下就没有现成的轮子使了。所以就有了这篇踩坑记。

1、在websocket握手前，需要先起一个http服务器，用来监听网络端是否有request过来。

```python
self._listen_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
self._listen_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
addr = socket.getaddrinfo("0.0.0.0", port)[0][4]
self._listen_s.bind(addr)
self._listen_s.listen(1)
self.cl, self.remote_addr = self._listen_s.accept()

```

2、当有request请求的时候，说明有客户端连上，并且给服务器发送了`问候`，比如下面这种。

```
GET /upload.html HTTP/1.1
Host: 192.168.0.18
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36
DNT: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6
```

所以，需要判断客户端是什么请求？ GET? POST? PUT? ...

```python
data = self.cl.recv(1024).decode()
if data and "Upgrade: websocket" in data.split("\r\n"): # 协议为websocket
    websocket_helper.server_handshake(self.cl)
elif data and "GET" == data.split(" ")[0]: # 协议为 HTTP GET
    self.htmlserver._serve_file(requested_file, self.cl)
elif data and ("PUT" == data.split(" ")[0] or "POST" == data.split(" ")[0]): # 协议为 HTTP PUT POST
    self.htmlserver._save_put_request(self.cl,content_length)
```

看到第一个if成立的情况下，我们直接发送握手信号，这个信号是客户端发送一段看不懂的东西，然后服务器端需要加上

```
258EAFA5-E914-47DA-95CA-C5AB0DC85B11
```

然后发送另外一段看不懂的东西给客户端（经过SHA1），这样握手就结束了，然后就可以开始愉快的websocket了。一个典型的Websocket握手请求如下：

客户端请求

```
GET / HTTP/1.1
Upgrade: websocket
Connection: Upgrade
Host: example.com
Origin: http://example.com
Sec-WebSocket-Key: sN9cRrP/n9NdMgdcy2VJFQ==
Sec-WebSocket-Version: 13
```

服务器回应

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: fFBooB7FAkLlXgRSz0BT3v4hq5s=
Sec-WebSocket-Location: ws://example.com/
```

当然这里面还有很多细节上的东西，都配置好后，就成了一个简单的HTTP+WEBSOCKET 运行在MCU上的小型服务器了。

  [1]: https://www.infoq.cn/article/deep-in-websocket-protocol

[comment]: # (##{"timestamp":1559263320}##)