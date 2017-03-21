#Author:zzk
# -*- coding:utf-8 -*-
__author__ = 'ZHONGZHIKUN408'
import urllib2
# import urllib
import cookielib

cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}

url ='http://www.csdn.net/'

req = urllib2.Request(url)
try:
    response = urllib2.urlopen(url)
    content = response.read()
    print(content)
except urllib2.URLError,e:
    if hasattr(e,"reason"):
        print "The reason:",e.reason
    elif hasattr(e,"code"):
        print "Error code:",e.code
        print "Return content:",e.read()

with open('html.txt','wb') as f:
    f.write(content)


