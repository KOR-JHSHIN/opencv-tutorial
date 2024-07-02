import cv2

video_file_path = './example_video.mp4'

cap = cv2.VideoCapture(video_file_path)            # creating video capture object

if cap.isOpened():                                 # checking capture object initialization
    # reading video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    print("Frame Width:", frame_width)
    print("Frame Height:", frame_height)
    print("Frames per Second:", fps)

    while True:                                    
        ret, frame = cap.read()                    # reading next frame
        if ret:
            cv2.imshow('Video', frame)             # displaying on screen
            key = cv2.waitKey(int(1000 / fps))     # applying delay according to fps
            if key == ord('q'):                    # break the loop if 'q' key is pressed
                break
        else:
            break                                  # exit the loop if frame reading fails

    cap.release()                                  # releasing capture resources
    cv2.destroyAllWindows()                        # closing all OpenCV windows
else:
    print("can't open video.")                     # capture object initialization failed
