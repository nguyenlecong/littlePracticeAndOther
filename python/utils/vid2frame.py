import os
import cv2
import math

video_folder = 'fire_video'
frame_folder = 'fire_frame'

i = 0
for videoFile in os.scandir(video_folder):
    if videoFile.is_file:
        cap = cv2.VideoCapture(videoFile.path)
        
        frameRate = cap.get(5) #frame rate
        while(cap.isOpened()):
            frameId = cap.get(1) #current frame number
            
            ret, frame = cap.read()
            if (ret != True):
                break

            if (frameId % math.floor(frameRate) == 0):
                i += 1
                filename = frame_folder + f"/{str(i)}.jpg"
                
                cv2.imwrite(filename, frame)

        cap.release()

print(i)