import cv2
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
'''

import cv2
import numpy as np
img = cv2.imread ("Burj Khalifa.jpg")
rows, cols = img.shape
print("rows",rows)
print("cols",cols)
# cut image
cut_image = img[426: 526, 250: 1280]
# ROI (region of interest)
cv2.rectangle(img, (385, 155), (851, 613), (0, 255, 0), 3)
roi = img[155: 613, 385: 1280]
cv2.imshow("cut image", cut_image)
cv2.imshow("Roi",roi)
cv2.imshow("image",img)
cv2.waitkey(0)

'''
'''
import cv2
import numpy as np
img = cv2.imread ("Burj Khalifa.jpg")
print(img.shape)
cv2.imshow("original",img)
cropped_image=img[80:280, 150:330]
cv2.imshow("cropped",cropped_image)
cv2.imwrite("cropped image.jpg",cropped_image)
cv2.waitkey(0)
cv2.destroyAllWindows()
'''
