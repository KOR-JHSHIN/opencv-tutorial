import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)
            cv2.imshow('Video', blurred_frame)
            key = cv2.waitKey(25)
            if key == ord('q'):
                break
        else:
            break
else:
    print("can't open video.")

cap.release()
cv2.destroyAllWindows()
