import cv2

video_file_path = './example_video.mp4'

cap = cv2.VideoCapture(video_file_path)            # creating video capture object
if cap.isOpened():                                 # checking capture object initialization 
    while True:                                    
        ret, frame = cap.read()                    # reading next frame
        if ret:
            cv2.imshow('Video', frame)             # displaying on screen            
            key = cv2.waitKey(25)                  # wait for 25ms (assuming 40fps)
            if key == ord('q'):                    # break the loop if 'q' key is pressed
                break
        else:
            break                                  # exit the loop if frame reading fails
else:
    print("can't open video.")                     # capture object initialization failed

cap.release()                                      # releasing capture resources
cv2.destroyAllWindows()                            # closing all OpenCV windows
