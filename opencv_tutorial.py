import cv2.cv2 as cv2


img = cv2.imread("picture_1.png", cv2.IMREAD_COLOR)
cv2.imshow("pic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Load an image
#convert color image to gray scale (black n white)
#resize image to specific width and height
# blurring an image
#create border around image
# draw a rectangle box over the pic
#save the image