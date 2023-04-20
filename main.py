import matplotlib.pyplot as plt
import datetime
import cv2


img = cv2.imread('./CJE_2023_Lecture_Test_ImageProcessing/Image_Processing/lena.jpg')
x,y,w,h = cv2.selectROI(img=img)
img = img[y:y+h, x:x+w]
now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
cv2.imwrite(f'./CJE_2023_Lecture_Test_ImageProcessing/output/{now}.jpg',img)