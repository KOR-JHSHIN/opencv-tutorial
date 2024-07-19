import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            gray_scale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Video', gray_scale_frame)
            key = cv2.waitKey(25)
            if key == ord('q'):
                break
        else:
            break
else:
    print("can't open video.")

cap.release()
cv2.destroyAllWindows()
