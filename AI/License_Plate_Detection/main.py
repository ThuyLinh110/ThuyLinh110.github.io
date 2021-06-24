
import cv2
import numpy as np 

def Gray_img(img):
   return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
def find_contour(img): 
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=cv2.contourArea,reverse=True)
    return contours

def crop_Rectangle(img,contours):
    screenCnt = None
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.05 * peri, True)

        if len(approx) == 4 :
            screenCnt = approx
            x,y,w,h = cv2.boundingRect(c)

            break
    if screenCnt is None:
        detected = 0
        print ("No plate detected")
  
    else:
        detected = 1

    if detected == 1:
        out=img[ y:y+h, x:x+w]
        # cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 2)
        img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3)
    dim=(300,220)
    img1 = cv2.resize(out, dim, interpolation = cv2.INTER_AREA)
    return img1


def crop_Number(img,cnts):
    num = 0
    for c in cnts:
        area =cv2.contourArea(c)
        if area <= 3500 and area >= 900:
            x,y,w,h = cv2.boundingRect(c)
            ROI = img[y:y+h, x:x+w]
            img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            cv2.imshow('ROI_{}'.format(num), ROI)
            num += 1
        
  
img = cv2.imread('image6.jpg')


edged = cv2.Canny(Gray_img(img), 30, 200)

out =crop_Rectangle(img,find_contour(edged))      # crop rectangle
cv2.imshow('Origin', img)


thresh = cv2.threshold(Gray_img(out), 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

crop_Number(out,find_contour(thresh))
cv2.imshow('crop',out)


cv2.waitKey(0)






































































































































