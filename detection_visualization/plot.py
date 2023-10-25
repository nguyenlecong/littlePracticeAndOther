import random

import cv2

def parse_label(path):
    file = open(path, 'r')
    lines = [line.strip() for line in file.readlines()]
    return lines

def plot_one_box(x, im, label=None):
    tl = round(0.003 * max(im.shape[0:2]))  # line thickness
    color = [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(im, c1, c2, color, thickness=tl)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl/3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(im, c1, c2, color, -1)  # filled
        cv2.putText(im, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

def run():
    class_map = {6: 'vehicle', 7: 'person'}

    img = cv2.imread('image.png')

    detections = parse_label('label.txt')
    for det in detections:
        x, y, w, h, cls_id = [int(i) for i in det.split(', ')]
        plot_one_box([x, y, x+w, y+h], img, label=class_map[cls_id])

    cv2.imwrite('output.png', img)

if __name__ == '__main__':
    run()