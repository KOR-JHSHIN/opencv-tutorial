import cv2

img_file_path = './example_img1.jpg'
save_img_file_path = './gray_example_img1.jpg'

img = cv2.imread(img_file_path, cv2.IMREAD_GRAYSCALE) # image reading in grayscale

if img is not None:                                  # checking if the image is successfully loaded
    cv2.imshow('IMG', img)                           # showing the image
    cv2.imwrite(save_img_file_path, img)             # saving the image
    print("image saved successfully.")               # printing message indicating the image was saved
    cv2.waitKey()                                    # waiting for a key press event
    cv2.destroyAllWindows()                          # closing all windows
else:
    print("no image file.")                          # printing error message if image is not loaded
