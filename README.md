# About

Fabric Role Scripts

# How to

```bash
基本形
$ fab -H 127.0.0.1 -u admin -f role_www.py role_www

■注意
httpd status呼び出しの場合のみ、下記にて実行(戻り値が0以外の為)
$ fab -H 127.0.0.1 -u admin -f role_www.py role_www -w
```
