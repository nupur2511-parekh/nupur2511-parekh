import cv2
path= "C:/Users/HP/Pictures/Tiger 2.jpg"
img = cv2.imread(path)
width ,height = 350,350
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)
imgCropped= img[300:540, 430:480]
imCropResize = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
cv2.imshow("tiger",img)
cv2.imshow("tiger cropped",imgCropped)
cv2.imshow("tiger cropped",imgCropped)
cv2.waitKey(0)    
