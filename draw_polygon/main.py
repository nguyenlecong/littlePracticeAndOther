import cv2
import argparse
import numpy as np

from utils.polygon_drawer import PolygonDrawer

from utils.config import FINAL_LINE_COLOR


def run( path):
    pd = PolygonDrawer()
    
    cap = cv2.VideoCapture(path)
    window_name = path.split('/')[-1]

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f'{window_name}: FPS_{fps}, Frame Count_{frame_count}')

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(window_name, 0, 0)

    is_first_frame = True
    while(cap.isOpened()): 
        ret, frame = cap.read()
        if not ret:
            break
        
        if is_first_frame:
            points = pd.run(window_name, frame)            
            is_first_frame = False
        
        cv2.polylines(frame, np.array([points]), True, FINAL_LINE_COLOR, 2, cv2.LINE_AA)
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cap.release() 
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path = 'data/synthetic_data/trimmed/14.avi'
    run(path)