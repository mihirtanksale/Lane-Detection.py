import cv2
import numpy as np
def find_white(image):
    #White color mask
    lower =np.uint8([200,200,200])
    upper =np.uint8([255, 255, 255])
    white_mask=cv2.inRange(image,lower,upper)
    return white_mask

def find_yellow(image):
    #yellow color mask
    lower=np.uint8([10,110,110])
    upper=np.uint8([40,255,255])
    yellow_mask=cv2.inRange(image,lower,upper)
    return yellow_mask

img=cv2.imread("road1.png")
cv2.imshow("Original",img)
imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",imghsv)

wh_mask=find_white(img)
yl_mask=find_yellow(imghsv)

mask_final=cv2.bitwise_or(wh_mask,yl_mask)
masked_final=cv2.bitwise_and(img,img,mask=mask_final)
cv2.imshow("Yellow Mask",yl_mask)
cv2.imshow("White Mask",wh_mask)
cv2.imshow("Final Mask",mask_final)
cv2.imshow("Final Image",masked_final)
cv2.waitKey()
cv2.destroyAllWindows()
