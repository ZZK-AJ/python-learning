# -*- coding: UTF-8 -*-
__author__ = 'zhongzhikun'

import urllib2

url = "http://www.baidu.com"

print 'first method'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print 'second method'
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print 'third method'
#cj = cookielib.CookieJar()
#openner = urllib2.urlopen(request)
#urllib2.install_opener(openner)
response3 = urllib2.urlopen(url)
print response3.getcode()
#print cj
print response3.read()
