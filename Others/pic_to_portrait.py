import cv2

img_location = './'
filename = 'DSC_6173.JPG'

img = cv2.imread(img_location+filename)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_image = 255 - gray_image

blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0)

inverted_blurred_img = 255 - blurred_img

pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale = 256.0)

cv2.imwrite("portrait_said_2020.jpg",pencil_sketch_IMG)
#Show the original image
cv2.imshow('Original Image', img)
#Show the new image pencil sketch
cv2.imshow('Pencil Sketch', pencil_sketch_IMG)
#Display the window infinitely until any keypress
cv2.waitKey(0)

