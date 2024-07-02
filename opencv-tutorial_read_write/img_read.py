import cv2

img_file_path = './example_img1.jpg'
img = cv2.imread(img_file_path)                     # image reading

if img is not None:                                 # checking if the image is successfully loaded
    cv2.imshow('IMG', img)                          # showing the image
    cv2.waitKey()                                   # waiting for a key press event
    cv2.destroyAllWindows()                         # closing all windows at once
else:
    print('No image file.')                         # printing error message if image is not loaded
