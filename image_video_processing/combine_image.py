import os
import cv2
from tqdm import tqdm
import numpy as np


def combine_4_images():
    path_raw = '/projects/new_obj_det_data/test/day/images/'

    path = '/projects/new_obj_det_data/test_folder/'
    path_old = path + 'test_old_day/'
    path_v4 = path + 'test_v4_day/'
    path_v5 = path + 'test_v5_day/'

    out_path = '/projects/new_obj_det_data/test_folder/combine_image_test_day/'

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 300)
    fontScale = 3
    fontColor = (255, 255, 255)
    thickness = 3
    lineType = 2

    for file in tqdm(os.listdir(path_old)):

        img1 = cv2.imread(path_raw+file)
        cv2.putText(img1, 'raw',
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

        img2 = cv2.imread(path_old+file)
        cv2.putText(img2, 'old',
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

        img3 = cv2.imread(path_v4+file)
        cv2.putText(img3, 'pretrained-v4',
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

        img4 = cv2.imread(path_v5+file)
        cv2.putText(img4, 'scratch-v5',
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

        image_row_1 = cv2.hconcat([img1, img2])
        image_row_2 = cv2.hconcat([img3, img4])
        combined_image = cv2.vconcat([image_row_1, image_row_2])

        cv2.imwrite(out_path+file, combined_image)

        # break


def combine_2_images():
    # path = '/projects/new_obj_det_data/test_folder/'
    # path_old = path + 'test_old_day/'
    # path_new = path + 'test_v5_day/'

    path_old = '/hdd/nguyenlc/hti-traffic/object_detection/yolov5/runs/detect/old_detection/'
    path_new = '/hdd/nguyenlc/hti-traffic/object_detection/yolov5/runs/detect/new_detection/'
    out_path = '/hdd/nguyenlc/hti-traffic/object_detection/yolov5/runs/detect/combine_image/'

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 300)
    fontScale = 3
    fontColor = (255, 255, 255)
    thickness = 3
    lineType = 2

    for file in tqdm(os.listdir(path_old)):

        img1 = cv2.imread(path_old+file)
        cv2.putText(img1, 'old',
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

        img2 = cv2.imread(path_new+file)
        cv2.putText(img2, 'new',
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

        combined_image = np.concatenate((img1, img2), axis=1)

        cv2.imwrite(out_path+file, combined_image)


if __name__ == '__main__':
    combine_2_images()
