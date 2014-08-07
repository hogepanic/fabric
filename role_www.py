# -*- coding: utf-8 -*-
from fabric.api import run, sudo

env.roledefs = {
    'web': ['192.168.1.10', '192.168.1.11', '192.168.1.12'],
    'dns': ['192.168.1.100']
}


def cron_edit():
    sudo('echo "MAILTO=[user address]" > /var/spool/cron/root')
    sudo('echo "00 03 * * * nice -n 18 /bin/sh /[contents path]/sample1.sh" >> /var/spool/cron/root')
    sudo('echo "*/10 * * * * /bin/sh /[contents path]/sample2.sh" >> /var/spool/cron/root')

def httpd_start():
    sudo("/etc/init.d/httpd start")

def httpd_stop():
    sudo("/etc/init.d/httpd stop")

def chkconfig_httpd_off():
    sudo("/sbin/chkconfig httpd off")

def chkconfig_list():
    sudo("/sbin/chkconfig --list httpd")

def httpd_status():
    run("/etc/init.d/httpd status")

def web_task():
    cron_edit()
    httpd_start()
#    httpd_stop()
#    chkconfig_httpd_off()
#    chkconfig_list()
#    httpd_status()
