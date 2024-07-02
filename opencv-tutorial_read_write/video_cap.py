import cv2

video_file_path = './example_video.mp4'

cap = cv2.VideoCapture(video_file_path)            # creating video capture object
if cap.isOpened():                                 # checking capture object initialization 
    while True:                                    
        ret, frame = cap.read()                    # reading next frame
        if ret:
            cv2.imshow('Video', frame)             # displaying on screen          
            if cv2.waitKey(25) == ord('q'):        # breaking the loop and saving cap_photo if any key is pressed
                cv2.imwrite('./video_cap.jpg', frame)
                print('captured image saved')  
                break
        else:
            print('no frame.')
            break
else:
    print("can't open video." )                    # capture object initialization failed
cap.release()                                      # releasing capture resources
cv2.destroyAllWindows()
