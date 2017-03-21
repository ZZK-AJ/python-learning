#Author:zzk
#coding=utf-8
# import urllib.request
import urllib2
import re
import sys
import os
URL="http://www.csdn.net/"
# request = urllib2.Request(URL)            #use Request method to get content
response = urllib2.urlopen(URL)    #获取了网页的内容
content = response.read()
print content
with open('html.txt', 'a+') as f:        #to write content to  html.txt
  f.write(content)
m = re.search(r'\w+\s=\s"//\w+.*"',content)
# m = re.search(r'<(body)\s\w+.*</(body)',content)
print m.group(0)


#</script>
# import urllib.request
# response = urllib.request.urlopen("https://www.zhihu.com/")
# #response = response.decode('utf-8')
# content = response.read()
# content = content.decode('utf-8')
# print(content)
# with open('html.txt', 'w',encoding='utf-8') as f:        #to write content to  html.txt
#     f.write(content)


