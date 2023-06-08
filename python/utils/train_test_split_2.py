import os
import glob
import shutil
import numpy as np
from random import shuffle


src = '/hdd/nguyenlc/ai4shop/fire_detection/dataset/raw/images/'
dst = '/hdd/nguyenlc/ai4shop/fire_detection/dataset/fire_dataset/'


def copy(a, b):
    shutil.copyfile(a, b)


def get_img_path():
    paths = []
    for image in sorted(os.listdir(src)):
        image_path = src + image
        # label_path = image_path.replace('images', 'labels').replace('jpg', 'txt')
        
        paths.append(image_path)

    return paths


def split(ratio_1=0.7, ratio_2=0.2):
    ratio_2 += ratio_1

    train = []
    val = []
    test = []

    # Get image paths list
    paths = get_img_path()
    
    # Split paths to 100 elements parts (due to frame from video)
    dist = 100
    path_num = len(paths) // dist

    parts = np.array_split(paths, path_num)
    for part in parts:
        for _ in range(10):  # shuffle multiple times
            shuffle(part)

        sub_train, sub_val, sub_test = np.split(part, [int(len(part)*ratio_1), int(len(part)*ratio_2)])

        train.extend(sub_train)
        val.extend(sub_val)
        test.extend(sub_test)

    # Check integrity
    print(len(train)/len(paths))
    print(len(val)/len(paths))
    print(len(test)/len(paths))

    print(len(train)+len(val)+len(test)-len(paths))
    print(any(i in val for i in train))
    print(any(i in test for i in val))
    print(any(i in test for i in train))

    return train, val, test

def get_label_path(img_path):
    return [path.replace('images', 'labels').replace('jpg', 'txt')\
            for path in img_path]

def move(imgs_src, labels_src, mode):
    for img_src, label_src in zip(imgs_src, labels_src):
        image_name = img_src.split('/')[-1]
        img_dst = dst + f'{mode}/images/' + image_name
        copy(img_src, img_dst)

        if os.path.isfile(label_src):
            label_dst = img_dst.replace('images', 'labels').replace('jpg', 'txt')

            copy(label_src, label_dst)

def remove():
    all_files = []
    for sub_folder, _, _ in os.walk(dst):
        for file in os.scandir(sub_folder):
            if file.is_file():
                all_files.append(file.path)
    
    for file in all_files:
        os.remove(file)
    
def main():
    # Remove all files first
    remove()

    # Split train, val, test
    img_train, img_val, img_test = split()

    label_train = get_label_path(img_train)
    label_val = get_label_path(img_val)
    label_test = get_label_path(img_test)

    move(img_train, label_train, 'train')
    move(img_val, label_val, 'val')
    move(img_test, label_test, 'test')


if __name__ == '__main__':
    main()
