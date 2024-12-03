import cv2
import numpy as np

def process_video():
    video_path = "../data/snooker.mp4"
    capture = cv2.VideoCapture(video_path)

    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            break

        #frame to color
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #DEFINE COLOR RANGE TO TRACK BLUE BALL
        lblue = np.array([100,150,0])
        upblue=np.array([140,255,255])

        #mask for blue
        mask = cv2.inRange(hsv, lblue, upblue)

        #contour
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 100:  # Filter small contours
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        cv2.imshow('Snooker Ball Tracker', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_video()