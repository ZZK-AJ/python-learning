#Author:zzk
# -*- coding:utf-8 -*-
import re

regex = r'[.*?]'
r1 = re.compile(regex)
print re.findall(r1, "hello[hi]heldfsdsf[iwonder]lo")
# r1 = re.compile('([.*?])')
print re.findall(r1, "hello[hi]heldfsdsf[iwonder]lo")

print re.findall('[0-9]{2}', "fdskfj1323jfkdj")
print re.findall('([0-9][a-z])', "fdskfj1323jfkdj")
print re.findall('(?=www)', "afdsfwwwfkdjfsdfsdwww")
print re.findall('(?<=www)', "afdsfwwwfkdjfsdfsdwww")

