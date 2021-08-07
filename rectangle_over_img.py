import cv2


path = r'coffee_mug_img.jpg'
image = cv2.imread(path)
window_name = 'Image'
# represents the top left corner of rectangle
start_point = (100, 100)
# represents the bottom right corner of rectangle
end_point = (220, 220)
# rectangle color in BGR
color = (255, 0, 0)
# Line thickness
thickness = 2
# Using cv2.rectangle() method
image = cv2.rectangle(image, start_point, end_point, color, thickness)
# Displaying the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()