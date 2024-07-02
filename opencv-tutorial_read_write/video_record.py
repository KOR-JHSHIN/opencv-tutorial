import cv2

cap = cv2.VideoCapture(0)                           # creating video capture object

if cap.isOpened():                                  # checking capture object initialization
    file_path = './recording_test.avi'              # specifying the video file path and name
    fps = 25.0                                      # frames per second
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')        # video codec setting
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # frame width
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# frame height
    size = (width, height)                          # frame size

    out = cv2.VideoWriter(file_path, fourcc, fps, size) # creating video writer object

    while True:                                    
        ret, frame = cap.read()                     # reading frame from the camera

        if not ret:
            print('cannot read frame from the camera.')
            break

        cv2.imshow('camera-recording', frame)       # displaying the frame
        out.write(frame)                            # writing frame to the video file

        # stopping recording by pressing 'q' key
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'): # 'q' key press to stop recording
            break

    out.release()                                   # releasing the video writer object
else:
    print("cannot open the camera.")                # capture object initialization failed

cap.release()                                       # releasing the camera
cv2.destroyAllWindows()                             # closing all OpenCV windows
