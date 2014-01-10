# -*- coding: utf-8 -*-
from fabric.api import run, sudo

def cron_edit():
    sudo('echo "MAILTO=xxx@xxx.co.jp" > /var/spool/cron/root')
    sudo('echo "00 03 * * * nice -n 18 /bin/sh /var/tmp//sample1.sh" >> /var/spool/cron/root')
    sudo('echo "*/10 * * * * /bin/sh /var/tmp/sample2.sh" >> /var/spool/cron/root')

def httpd_start():
    sudo("/etc/init.d/httpd start")

def httpd_stop():
    sudo("/etc/init.d/httpd stop")

def httpd_status():
    run("/etc/init.d/httpd status")

def web_task():
    cron_edit()
    httpd_start()
#    httpd_stop()
#    httpd_status()

