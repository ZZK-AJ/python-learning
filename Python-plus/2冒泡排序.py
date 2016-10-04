#!_*_coding:utf-8_*_
#coding=utf-8

# data = [10, 4, 33, 21, 54, 3, 8, 11, 5, 22, 2, 1, 17, 13, 6]
data = [10, 4, 33, 21, 54, 3]

print("before sort:", data)

previous = data[0]
for j in range(len(data)):
    tmp = 0
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:   #只要前面一个大于后一个，就调换两个的值
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp
  #          print '---有改变---'
 #       print(data)

print("after sort:", data)

print '冒泡法就是通过不断的前后比较，把大的数放到后面'

