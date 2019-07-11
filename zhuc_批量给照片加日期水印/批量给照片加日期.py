# coding:utf-8 
#批量给照片加日期水印
import os 
import time
from PIL import Image,ImageDraw,ImageFont 

font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 240)

def secondsToStr(seconds):
	x = time.localtime(seconds)  # 时间元组    
	return time.strftime("%Y-%m-%d", x)  # 时间元组转为字符串
	#return time.strftime("%Y-%m-%d ", x)  # 时间元组转为字符串 

def add_time_topicture(image_name,text,seq,font=font):
	
	rgba_image = image_name.convert('RGBA')
	text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))#新建白色透明图层
	image_draw = ImageDraw.Draw(text_overlay)#创建绘画对象
	text_size_x, text_size_y = image_draw.textsize(text, font=font)
	# 设置文本文字位置
	text_xy = (rgba_image.size[0] - text_size_x, rgba_image.size[1] - text_size_y)
	# 设置文本颜色和透明度
	image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 180))

	image_with_text = Image.alpha_composite(rgba_image, text_overlay)#融合两张图片
	#image_with_text.show()
	image_with_text.save(text+'_'+str(seq)+'.bmp')
	return image_with_text


def main_process():

	#遍历文件夹
	BaseDir=r'E:\GitHub' #字符串前加r表示防止转义字符
	#rootDir='E:\\GitHub\\' 
	seq=0
	#遍历目录
	for root,dirs,files in os.walk(BaseDir):
		for file in files:
			if os.path.splitext(file)[1] == '.jpg':
				seq=seq+1
				file_name = os.path.join(root,file)
				fileInfo = os.stat(file_name)
				im_before = Image.open(file_name)
				add_time_topicture(im_before,secondsToStr(fileInfo.st_ctime),seq,font)

main_process()
	



