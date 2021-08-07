
import cv2
path = r'coffee_mug_img.jpg'
img = cv2.imread(path, 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()