#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import os
import time


headers = {
    'User-Agent	' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0', 
}

def get_html(url, Referer_url=None):
    '''get_html(url),download and return html'''
    if Referer_url:
        headers['Referer'] = Referer_url
    req = requests.get(url, headers=headers)
    # req.encoding = 'gb2312'
    return req.text

def get_html_from_phantomjs(url):
    start_time = time.time()
    shell = 'phantomjs code.js {}'.format(url)
    print 'run shell cmd:{}'.format(shell)
    html = os.popen(shell).read()
    end_time = time.time()
    spend = end_time - start_time
    print 'loading time: {}s'.format(spend)

    return html
