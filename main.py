import cv2 
from cv2 import VideoWriter, VideoWriter_fourcc

camera = cv2.VideoCapture(1)
video = VideoWriter('output.avi', VideoWriter_fourcc(*'MJPG'), 10, (1280,720))

while camera.isOpened():
    _, frame = camera.read()
    video.write(frame)
    
    cv2.imshow('Footage', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()