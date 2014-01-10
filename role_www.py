# -*- coding: utf-8 -*-
from fabric.api import run, sudo

def cron_edit():
    sudo('echo "MAILTO=[user address]" > /var/spool/cron/root')
    sudo('echo "00 03 * * * nice -n 18 /bin/sh /[contents path]/sample1.sh" >> /var/spool/cron/root')
    sudo('echo "*/10 * * * * /bin/sh /[contents path]/sample2.sh" >> /var/spool/cron/root')

def httpd_start():
    sudo("/etc/init.d/httpd start")

def httpd_stop():
    sudo("/etc/init.d/httpd stop")

def httpd_status():
    run("/etc/init.d/httpd status")

def role_www():
    cron_edit()
    httpd_start()
#    httpd_stop()
#    httpd_status()

