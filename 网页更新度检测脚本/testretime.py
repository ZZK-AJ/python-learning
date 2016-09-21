#! /usr/bin/env python
#coding=utf-8
# 以需要的时间间隔执行某个命令    
import time, os 
#inc = 60 * 60 * 24
def schdule(cmd, inc = 60):     #use schdule to execute 'cmd' every 'inc' second
    while True: 
        os.system(cmd); 
        time.sleep(inc) 

schdule('python count.py', 5)

'''
with the re_exe to count what plus in this time
zzk@py:~/oksecpy/day5$ python testretime.py 
+ times: 3 
+ times: 3 
+ times: 3 
+ times: 4 
+ times: 4 
+ times: 4 
+ times: 5 
'''