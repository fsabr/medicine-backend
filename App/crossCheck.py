
import cv2 
def fun(img):
    image = img
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(image, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    marea=0

    mh = image.shape[0]
    mw = image.shape[1]

    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        area = w*h
        if(area > marea and area < mh*mw):
            marea = area
    
    fin = img

    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w*h == marea:
            idx+=1
            new_img=image[y:y+h,x:x+w]
            fin = cimwrite(str(idx) + '.png', new_img)
    # cv2.ims
    # 
    # how("im",image)
    # cv2.waitKey(0)
    return fin
