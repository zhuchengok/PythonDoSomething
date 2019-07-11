import os 
import time 
from math import ceil 
def secondsToStr(seconds):
	x = time.localtime(seconds)  # 时间元组    
	return time.strftime("%Y-%m-%d ", x)  # 时间元组转为字符串
	#return time.strftime("%Y-%m-%d ", x)  # 时间元组转为字符串 

fileInfo = os.stat('test.jpg') #获取文件属性信息
'''
st_mode=33206 #权限模式
st_ino=844424930150465 #inode 
numberst_dev=3795105997 #device
st_nlink=1 #number of hard links
st_uid=0  #所有用户的user id
st_gid=0 #所有用户的group id
st_size=64985 #文件的大小，以字节为单位
st_atime=1549040523  #文件最后访问时间
st_mtime=1549040524  #文件最后修改时间
st_ctime=1549036862  #文件创建时间
'''
print('文件大小:{}k'.format(ceil(fileInfo.st_size/1024)))
print('文件创建时间:{}'.format(secondsToStr(fileInfo.st_ctime)))
print('文件访问时间:{}'.format(secondsToStr(fileInfo.st_atime)))
print('文件修改时间:{}'.format(secondsToStr(fileInfo.st_mtime)))
