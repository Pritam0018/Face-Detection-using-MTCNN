import cv2
from mtcnn import MTCNN

cap = cv2.VideoCapture(0)
detector = MTCNN()

while True:

    ret,frame = cap.read()

    output = detector.detect_faces(frame)

    for single_output in output:
        x,y,width,height = single_output['box']
        cv2.rectangle(frame,pt1=(x-5,y),pt2=(x+width,y+height),color=(0,0,0),thickness=3)
        cv2.putText(frame, "FACE-DETECTED", (x-40,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('win',frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()