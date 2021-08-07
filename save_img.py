import cv2

# read image
img = cv2.imread('coffee_mug_img.jpg')
# save image
status = cv2.imwrite('coffee_mug_img.jpg',img)
print("Image written to file-system : ", status)