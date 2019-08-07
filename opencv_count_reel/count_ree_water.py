import cv2
import numpy as np
reel_img=cv2.imread(r'E:\GitHub\PythonDoSomething\opencv_count_reel\reel01.jpg')
reel_img_gray = cv2.cvtColor(reel_img, cv2.COLOR_BGR2GRAY)
ret,binary_reel_img=cv2.threshold(reel_img_gray,175,255,cv2.THRESH_BINARY)

fg=cv2.erode(binary_reel_img,None,iterations=2)
bgt=cv2.dilate(binary_reel_img,None,iterations=3)

ret,bg=cv2.threshold(bgt,1,128,1)

marker=cv2.add(fg,bg)


marker32=np.int32(marker)

cv2.watershed(reel_img,marker32)
m=cv2.convertScaleAbs(marker32)


ret,binary_reel_img = cv2.threshold(m,175,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
res = cv2.bitwise_and(reel_img,reel_img,mask = binary_reel_img)


cv2.imshow("img_after_water", res)  
cv2.imwrite(r'E:\GitHub\PythonDoSomething\opencv_count_reel\water_after.jpg',res)
cv2.waitKey(0) 




#将图片保存到指定位置



