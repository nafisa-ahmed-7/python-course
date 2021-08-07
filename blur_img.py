import cv2

img = cv2.imread('coffee_mug_img.jpg')
blurImg = cv2.blur(img, (10, 10))
cv2.imshow('blurred image', blurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()