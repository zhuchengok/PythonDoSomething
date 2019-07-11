from PIL import Image,ImageDraw,ImageFont
 
# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
# Window的字体目录是C:\Windows\Fonts
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 240)
 
# image: 图片  text：要添加的文本 font：字体
def add_text_to_image(image, text, font=font):
  rgba_image = image.convert('RGBA')
  text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
  image_draw = ImageDraw.Draw(text_overlay)
 
  text_size_x, text_size_y = image_draw.textsize(text, font=font)
  # 设置文本文字位置
  print(rgba_image)
  text_xy = (rgba_image.size[0] - text_size_x, rgba_image.size[1] - text_size_y)
  # 设置文本颜色和透明度
  image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 180))
 
  image_with_text = Image.alpha_composite(rgba_image, text_overlay)
 
  return image_with_text
 
im_before = Image.open("test.jpg")
im_before.show()
im_after = add_text_to_image(im_before, '2019/7/6',font)
im_after.show()
# im.save('im_after.jpg')