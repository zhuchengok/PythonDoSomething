import cv2
#reel_img=cv2.imread(r'E:\GitHub\PythonDoSomething\\opencv_count_reel\reel01.jpg',cv2.IMREAD_GRAYSCALE)
reel_img=cv2.imread(r'E:\GitHub\PythonDoSomething\opencv_count_reel\reel01.jpg')
#reel_img = cv2.resize(reel_img,(600,600),interpolation=cv2.INTER_AREA)
reel_img_gray = cv2.cvtColor(reel_img, cv2.COLOR_BGR2GRAY)
ret,binary_reel_img=cv2.threshold(reel_img_gray,175,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(binary_reel_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    # 输出为三个参数  
img_after=cv2.drawContours(reel_img,contours,-1,(0,0,255),1)
cv2.imshow("img_after", img_after)  
cv2.imwrite(r'E:\GitHub\PythonDoSomething\opencv_count_reel\reel01_after.jpg',img_after)
cv2.waitKey(0) 
print (len(contours))



#将图片保存到指定位置



