import cv2

cap = cv2.VideoCapture(0)
ret = True
while ret:
    ret, frame = cap.read()

    cv2.imshow('q', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
