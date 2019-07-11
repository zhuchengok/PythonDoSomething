
# coding:utf-8 
import os
#遍历文件夹
rootDir='E:\\GitHub\\'   
def iter_files(rootDir):
    #遍历根目录
	for root,dirs,files in os.walk(rootDir):
		for file in files:
			file_name = os.path.join(root,file)
			print(file_name)

iter_files(rootDir)