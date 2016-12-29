#Author:zzk
print ("hello world!")

name = input("please input your name:")
age = input("please input your age:")

info = '''
----- info of {_name} ------
name:{_name}
age:{_age}
'''.format(_name=name,
           _age=age)

print (info)

