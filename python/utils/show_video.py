import cv2
import argparse 
import time


ap = argparse.ArgumentParser()
ap.add_argument('-i', default='out.avi')
ap.add_argument('-d', default=0.01)
args = ap.parse_args()

vid_name = args.i.split('/')[-1]

cap = cv2.VideoCapture(args.i)
while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    cv2.namedWindow(vid_name, cv2.WINDOW_NORMAL)
    cv2.imshow(vid_name, frame)
    cv2.moveWindow(vid_name, 10, 10)
    
    time.sleep(float(args.d))
    
    k = cv2.waitKey(1)
    if k==ord('q'):
        break 
    if k==ord(' '):
        input()
        
cap.release()
cv2.destroyAllWindows()
