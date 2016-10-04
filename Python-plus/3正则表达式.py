#coding=utf-8
import re  # 导入模块名

p = re.compile("^[0-9]")
# 生成要匹配的正则对象
# ^代表从开头匹配，[0-9]代表匹配0至9的任意一个数字
#  所以这里的意思是对传进来的字符串进行匹配，如果这个字符串的开头第一个字符是数字，就代表匹配上了

m = p.match('14534Abc')
# 按上面生成的正则对象 去匹配字符串， 如果能匹配成功，这个m就会有值
# 否则m为None<br><br>if m: #不为空代表匹配上了
print m
#<_sre.SRE_Match object at 0x00000000034EA648>

print(m.group())
# m.group()返回匹配上的结果，此处为1，因为匹配上的是1这个字符<br>else:<br>　　print("doesn't match.")<br>

# 正则表达式常用5种操作
# re.match(pattern, string)　　　　 # 从头匹配
# re.search(pattern, string)　　　　# 匹配整个字符串，直到找到一个匹配
a = re.search("[a-z]","saf")
print(a)

#re.split()      # 将匹配到的格式当做分割点对字符串分割成列表
m = re.split("[0-9]", "alex1rain2jack3helen rachel8")
print(m)
# ['alex', 'rain', 'jack', 'helen rachel', '']

#re.findall()　　　　　　　　　　# 找到所有要匹配的字符并返回列表格式
m = re.findall("[0-9]", "alex1rain2jack3helen rachel8")
print(m)
# 输出：['1', '2', '3', '8']

# re.sub(pattern, repl, string, count,flag) 　　　# 替换匹配到的字符
m=re.sub("[0-9]","|", "alex1rain2jack3helen rachel8",count=2 )
print(m)
# 输出：alex|rain|jack3helen rachel8　　

'---------实例-------------'

phone_str = "hey my name is alex, and my phone number is 13651054607, please call me if you are pretty!"
phone_str2 = "hey my name is alex, and my phone number is 18651054604, please call me if you are pretty!"
m = re.search("(1)([358]\d{9})", phone_str2)
if m:
    print(m.group())
# 18651054604

ip_addr = "inet 192.168.60.223 netmask 0xffffff00 broadcast 192.168.60.255"
m = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip_addr)
print(m.group())
# 192.168.60.223  先匹配到第一个

email = "alex.li@126.com   http://www.oldboyedu.com"
m = re.search(r"[0-9.a-z]{0,26}@[0-9.a-z]{0,20}.[0-9a-z]{0,8}", email)
print(m.group())
# alex.li@126.com



