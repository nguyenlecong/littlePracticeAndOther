import cv2
import numpy as np

from .config import FINAL_LINE_COLOR, WORKING_LINE_COLOR


class PolygonDrawer(object):
    def __init__(self):
        self.points = []
        self.done = False
        self.current = (0, 0)

    def on_mouse(self, event, x, y, buttons, user_param):
        if self.done:
            return

        if event == cv2.EVENT_MOUSEMOVE:
            self.current = (x, y)
        elif event == cv2.EVENT_LBUTTONDOWN:
            self.points.append((x, y))

    def run(self, window_name, frame, mode='RECT'):
        cv2.setMouseCallback(window_name, self.on_mouse)

        while (not self.done):
            canvas = frame.copy()

            if mode == 'POLYGON':
                if len(self.points) > 0:
                    cv2.polylines(canvas, np.array([self.points]), False, FINAL_LINE_COLOR, 2, cv2.LINE_AA)
                    cv2.line(canvas, self.points[-1], self.current, WORKING_LINE_COLOR, 2, cv2.LINE_AA)
                
                cv2.imshow(window_name, canvas)
                if cv2.waitKey(1) == 27 and len(self.points) > 2:  # ESC
                    self.done = True
            
            elif mode == 'RECT':
                if len(self.points) == 1:
                    cv2.rectangle(canvas, self.points[0], self.current, WORKING_LINE_COLOR, 2, cv2.LINE_AA)
                if len(self.points) == 2:
                    self.done = True

                cv2.imshow(window_name, canvas)
                cv2.waitKey(1)

        return self.points
