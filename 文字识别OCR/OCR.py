python3使用Pillow、tesseract-ocr与pytesseract模块的图片识别


1.安装Pillow

pip install Pillow

2.安装tesseract-ocr
github地址: https://github.com/tesseract-ocr/tesseract
windows:
The latest installer can be downloaded here: tesseract-ocr-setup-3.05.01.exe and tesseract-ocr-setup-4.00.00dev.exe (experimental). 
ubuntu:

sudo apt-get install tesseract-ocr
traineddata文件路径: /usr/share/tesseract-ocr/tessdata/

3.安装pytesseract

pip install pytesseract
如不能使用pip直接安装可取搜索模块文件直接安装

遇到问题及解决：
1.FileNotFoundError: [WinError 2] 系统找不到指定的文件
解决办法：

方法1[推荐]: 将tesseract.exe添加到环境变量PATH中，
例如: D:\Tesseract-OCR,默认路径为C:\Program Files (x86)\Tesseract-OCR
注意: 为了使环境变量生效，需要关闭cmd窗口或是关闭pycharm等ide重新启动
方法2: 修改pytesseract.py文件，指定tesseract.exe安装路径
# CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe‘
方法3:  在实际运行代码中指定
pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'

2.pytesseract.pytesseract.TesseractError: (1, 'Error opening data file \\Tesseract-OCR\\tessdata/eng.traineddata')
 解决方法:
方法1[推荐]: 
将tessdata目录的上级目录所在路径(默认为tesseract-ocr安装目录)添加至TESSDATA_PREFIX环境变量中
例如: C:\Program Files (x86)\Tesseract-OCR
Please make sure the TESSDATA_PREFIX environment variable is set to the parent directory of your "tessdata" directory.
 
方法2:  在.py文件配置中指定tessdata-dir
tessdata_dir_config = '--tessdata-dir "D:\\Tesseract-OCR\\tessdata"'
# tessdata_dir_config = '--tessdata-dir "'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pytesseract.image_to_string(image, config=tessdata_dir_config)
trainedata下载地址: the latest from github.com
示例： 


# -*-coding:utf-8-*-  

from PIL import Image  

import sys  

import os  

import pytesseract

from selenium import webdriver  

sys.path.append('C:\Python27\Lib\site-packages\pytesser')  

import pytesser  

url='http://192.168.24.189/system/code?0.6824490785056669'  

driver = webdriver.Firefox()  

driver.maximize_window()  #将浏览器最大化  

driver.get(url)  

imgelement = driver.find_element_by_id('codeImg')  #定位验证码  

location = imgelement.location  #获取验证码x,y轴坐标  

size=imgelement.size  #获取验证码的长宽  

rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标  

name="code.jpg"    

driver.find_element_by_id("codeImg").click()  

driver.save_screenshot(name)  #截取当前网页，该网页有我们需要的验证码  

aa=Image.open(name) #打开截图  

frame4=aa.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域  

frame4.save(name)  

im = Image.open(name)

#转化到灰度图

imgry = im.convert('L')

#保存图像

imgry.save('g'+name)

#二值化，采用阈值分割法，threshold为分割点

threshold = 140

table = []

for j in range(256):

    if j < threshold:

        table.append(0)

    else:

        table.append(1)

out = imgry.point(table, '1')

out.save('b'+name)

#识别

text = pytesseract.image_to_string(out)

#识别对吗

text = text.strip()

text = text.upper();

print (text)

text = pytesseract.image_to_string(Image.open('code.png'), lang="eng")

print(text)  
