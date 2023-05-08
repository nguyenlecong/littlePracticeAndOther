import cv2
import numpy as np
from skimage.transform import resize

# Create fake image (original image)
frame_height = 720
frame_width = 1280
image = np.ones((frame_height, frame_width, 3))
image = np.asarray(image, np.uint8)

cell_size = 40
n_cols = frame_width//cell_size
n_rows = frame_height//cell_size

heat_matrix = np.zeros((n_rows, n_cols))

def get_row_col(x, y):
    row = y//cell_size
    col = x//cell_size

    return row, col

# Draw grid on original image
color = (0, 0, 0)
thickness = 1
for i in range(n_rows):
        start_point = (0, (i + 1) * cell_size)
        end_point = (frame_height, (i + 1) * cell_size)
        color = color
        thickness = thickness
        image = cv2.line(image, start_point, end_point, color, thickness)

for i in range(n_cols):
    start_point = ((i + 1) * cell_size, 0)
    end_point = ((i + 1) * cell_size, frame_width)
    color = color
    thickness = thickness
    image = cv2.line(image, start_point, end_point, color, thickness)

# Create fake heat matrix
randomNums = np.random.normal(scale=3, size=100000)
randomInts = np.round(randomNums)
xrange = np.arange(start=min(randomInts), stop = max(randomInts) + 1)
yrange = np.arange(start=min(randomInts), stop = max(randomInts) + 1)
for x, y in zip(xrange, yrange):
    row = int(y)//cell_size
    col = int(x)//cell_size
    heat_matrix[row, col] += 1

heat_matrix = cv2.resize(heat_matrix, (frame_width, frame_height))
heat_matrix = heat_matrix / np.max(heat_matrix)
heat_matrix = np.uint8(heat_matrix*255)

heat_image = cv2.applyColorMap(heat_matrix, cv2.COLORMAP_JET)

# Combine heat image and original image
alpha = 0.2
image = cv2.addWeighted(heat_image, alpha, image, 1-alpha, 0)

cv2.imshow('', image)
cv2.waitKey()
cv2.destroyAllWindows()