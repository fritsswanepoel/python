#Convert an image (.jpg) to pencil sketch
import cv2
import sys

img_location = sys.argv[1] #Folder and file name
blur_value = int(sys.argv[2]) #Blur to apply

img = cv2.imread(img_location)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255 - gray_image

blurred_img = cv2.GaussianBlur(inverted_gray_image, (blur_value,blur_value), 0)
inverted_blurred_img = 255 - blurred_img

pencil_sketch_img = cv2.divide(gray_image, inverted_blurred_img, scale = 256.0)

cv2.imwrite(img_location.split('.')[0]+'_pencil.'+img_location.split('.')[1], pencil_sketch_img)




