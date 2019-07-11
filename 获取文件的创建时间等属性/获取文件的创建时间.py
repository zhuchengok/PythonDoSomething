#endcoding: utf-8

# 获取文件的时间属性-创建时间，修改时间和访问时间
# 用到的知识
#   os.getcwd() 方法用于返回当前工作目录
#   os.path.getatime(file) 输出文件访问时间
#   os.path.getctime(file) 输出文件的创建时间
#   os.path.getmtime(file) 输出文件最近修改时间


import time 
import os

def fileTime(file):
    return [
        time.ctime(os.path.getatime(file)),#访问时间
        time.ctime(os.path.getmtime(file)),#修改时间
        time.ctime(os.path.getctime(file))#创建时间
    ]

times = fileTime(os.getcwd())
print(times)
print(type(times))
