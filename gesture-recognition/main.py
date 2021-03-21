import cv2
import winsound
import numpy as np
import pyautogui

cam = cv2.VideoCapture(0)
yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])
prev_y = 0

while cam.isOpened():
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        area = cv2.contourArea(c)
        if area < 4000:
            continue
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if y < prev_y:
                pyautogui.press('space')
            else:
                pyautogui.press('page up')
            prev_y = y

        winsound.Beep(500, 500)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Gesture Recognition - Scroll Only', frame1)

cam.release()
cv2.destroyAllWindows()