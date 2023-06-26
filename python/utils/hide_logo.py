import cv2

img_1 = cv2.imread('images/21.jpg')

img_2 = cv2.imread('images/22.jpg')

logo = img_2[1750:1870, 990:1370]

img_1[1750:1870, 990:1370] = logo

cv2.imwrite('images/2.jpg', img_1)
