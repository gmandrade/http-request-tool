# HTTP Request Tool

**NOTE** Requires python3.6 and lib requests version 2.18.4

Simple script for testing HTTP requests

```
$ ./main.py -h
usage: main.py [-h] -u URL [-m METHOD] [-t TIMEOUT] [-n NUMBER]
               [-sh SHOW_HEADER]

HTTP Request Tool

optional arguments:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
                        Method request. Example: GET or HEAD Default: GET
  -t TIMEOUT, --timeout TIMEOUT
                        Define a timeout Example: 10 Default: 20
  -n NUMBER, --number NUMBER
                        Requests number Example: 10 Default: 1
  -sh SHOW_HEADER, --show-header SHOW_HEADER
                        Return header Example: True Default: False

required arguments:
  -u URL, --url URL     Url for request. Example: http://google.com
```

## Send 5 requests to a same URL with 10s timeout (requestTime is in seconds)
```
$ ./main.py -u http://facebook.com -n 5 -t 10
sys=http-request-tool log=INFO status=200 url=http://facebook.com requestTime=0.424029
sys=http-request-tool log=INFO status=200 url=http://facebook.com requestTime=0.429841
sys=http-request-tool log=INFO status=200 url=http://facebook.com requestTime=0.343457
sys=http-request-tool log=INFO status=200 url=http://facebook.com requestTime=0.430575
sys=http-request-tool log=INFO status=200 url=http://facebook.com requestTime=0.439477
```
or
```
$ ./main.py -u http://github.com --number 5 --timeout 10
sys=http-request-tool log=INFO status=200 url=http://github.com requestTime=0.922388
sys=http-request-tool log=INFO status=200 url=http://github.com requestTime=0.9215
sys=http-request-tool log=INFO status=200 url=http://github.com requestTime=0.921469
sys=http-request-tool log=INFO status=200 url=http://github.com requestTime=0.920861
sys=http-request-tool log=INFO status=200 url=http://github.com requestTime=0.921263
```

## Send a request with HEAD method
```
$ ./main.py -u http://instagram.com -m HEAD
sys=http-request-tool log=INFO status=301 url=http://instagram.com requestTime=0.482837
```
or
```
$ ./main.py -u http://yahoo.com --method HEAD
sys=http-request-tool log=INFO status=301 url=http://yahoo.com requestTime=0.482571
```

## Show header from request
```
$ ./main.py -u http://bbc.com -sh True
sys=http-request-tool log=INFO status=200 url=http://bbc.com requestTime=0.090202 header={'Server': 'Apache', 'X-Cache-Action': 'HIT', 'X-Cache-Age': '3', 'Content-Type': 'text/html', 'Content-Encoding': 'gzip', 'Expires': 'Sat, 20 Oct 2018 04:42:03 GMT', 'Content-Language': 'en', 'Etag': '"d641e3b5c7cc11eac18c48310d7dc8a8"', 'X-PAL-Host': 'pal836.back.live.lbh.local:80', 'Content-Length': '37029', 'Accept-Ranges': 'bytes', 'Date': 'Sat, 20 Oct 2018 05:00:41 GMT', 'Via': '1.1 varnish', 'Age': '5', 'Connection': 'keep-alive', 'X-LB-NoCache': 'true', 'X-Fastly-Cache-Status': 'HIT-CLUSTER', 'Set-Cookie': 'BBC-UID=9191fedbebbc3207e64dbb22eb6c5ef123fa2d821693783d807cceed6aadaad30python-requests%2F2.18.4; expires=Wed, 19 Oct 2022 05:00:41 GMT; path=/; domain=.bbc.com', 'Cache-Control': 'private, max-age=60', 'X-Served-By': 'cache-gru17122-GRU', 'X-Cache': 'HIT', 'X-Cache-Hits': '1, 1', 'X-Timer': 'S1540011642.969681,VS0,VE1', 'Vary': 'Accept-Encoding'}
```
or
```
$ ./main.py -u http://hackernews.com --show-header True
sys=http-request-tool log=INFO status=200 url=http://hackernews.com requestTime=0.865824 header={'Date': 'Sat, 20 Oct 2018 05:01:10 GMT', 'Server': 'Apache/2.4.35', 'Last-Modified': 'Thu, 08 Feb 2007 23:26:02 GMT', 'ETag': '"20d9-428ff5dc7f680"', 'Accept-Ranges': 'bytes', 'Content-Length': '8409', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Content-Type': 'text/html'}
```

## You can run as a docker command
```
$ docker build -t http-request-tool .
```

```
$ docker run -it http-request-tool -u http://google.com -n 5
sys=http-request-tool log=INFO status=200 url=http://google.com requestTime=0.290938
sys=http-request-tool log=INFO status=200 url=http://google.com requestTime=0.094965
sys=http-request-tool log=INFO status=200 url=http://google.com requestTime=0.085773
sys=http-request-tool log=INFO status=200 url=http://google.com requestTime=0.139594
sys=http-request-tool log=INFO status=200 url=http://google.com requestTime=0.133311
```