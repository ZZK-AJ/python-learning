#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import urllib2
URL="http://10.23.30.130/index.asp"    #the url you need to deal with
request = urllib2.Request(URL)            #use Request method to get content
response = urllib2.urlopen(request)
content = response.read()
with open('html.txt', 'w') as f:        #to write content to  html.txt
   f.write(content)

import difflib
import re
#to compare two txt to ndiff the difference
sum1 = 0
newfile = '/home/zzk/oksecpy/day5/html.txt'    #?????
oldfile = '/home/zzk/oksecpy/day5/html1.txt'
with open(oldfile,'r') as f1,open(newfile,'r') as f2:
#show the difference what plus in html today
	diff = difflib.ndiff(f1.readlines(),f2.readlines())                #use ndiff method return a 
	#sys.stdout.writelines(diff)
	for i in diff:
		#print i
		m1 = re.search('^\+ <a href=',i)
		#print m1
		if m1 is not None:
		    sum1 += 1
print '+ times: %s ' %sum1
#put + times into a txt , and append the new sum in it
with open ('sum.txt','a') as f3:
	f3.write('\n +times: %s' %sum1)




