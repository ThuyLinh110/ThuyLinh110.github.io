import numpy as np 
import cv2
def GrayChanel(image):
    B=np.array(image[:,:,0])
    G=np.array(image[:,:,1])
    R=np.array(image[:,:,2])
    img_gray = (R * 0.2989 + G * 0.5870 + B * 0.1140)
    return np.array(img_gray.astype(np.uint8))
def BlackWhite_Chanel(image):
    image=np.where(image>110,image,0)
    return np.where(image<110,image,255)
image=cv2.imread("image.PNG")
cv2.imshow("Gray",GrayChanel(image))
cv2.imshow("BlackWhite",BlackWhite_Chanel(GrayChanel(image)))
cv2.waitKey(10000)



