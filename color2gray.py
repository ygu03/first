import cv2

img = cv2.imread('11.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #灰度图
#cv2.imshow('a',gray) 测试灰度图

ret,thresh  = cv2.threshold(gray,100,255,cv2.THRESH_BINARY) # 将图片进行二值化（130,255）之间的点均变为255（背景）
cv2.imshow('b',thresh) #测试二值图
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('12.jpg',thresh)