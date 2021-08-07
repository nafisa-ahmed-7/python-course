import cv2

path = r'coffee_mug_img.jpg'
image = cv2.imread(path)
window_name = 'Image'
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
