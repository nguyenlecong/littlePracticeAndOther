import os
import random
import shutil

import cv2
import numpy as np
import albumentations as A
from PIL import Image, ImageEnhance

class Augmentator:
    def __init__(self, for_stamp=True):
        self.for_stamp = for_stamp
        self.opacities = [0.4, 0.7, 1.0]

        if for_stamp:
            T = [
                # A.ChannelShuffle(p=0.1),
                A.MedianBlur(p=0.1),
                A.Sharpen(p=0.1),
                A.Affine(p=0.1),
                A.Flip(p=0.1),
                A.HorizontalFlip(p=0.1),
                A.OpticalDistortion(p=0.1),
                A.Perspective(p=0.1),
                A.RandomRotate90(p=0.1),
                A.VerticalFlip(p=0.1),
                ]
        else:
            T = [
                # A.Crop(x_min=50, y_min=100, x_max=500, y_max=556, p=1),  # for debugging
                A.Perspective(p=0.1),
                A.Blur(p=0.1),
                A.ColorJitter(p=0.1),
                # A.Equalize(p=0.1),
                A.HueSaturationValue(p=0.1),
                # A.MotionBlur(p=0.1),
                A.Posterize(p=0.1),
                A.RGBShift(p=0.1),
                A.RandomBrightnessContrast(p=0.1),
                # A.RandomRain(p=0.1),
                # A.RingingOvershoot(p=0.1),
                A.Sharpen(p=0.1),
                A.ToGray(p=0.1),
                A.ToSepia(p=0.1),
            ]
        
        self.transform = A.Compose(T)
    
    def random_opacity(self, img):
        opacity = random.choice(self.opacities)
        alpha = img.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        img.putalpha(alpha)
        return img

    def random_gray(self, img):
        p = random.random()
        if p >= 0.7:
            img = img.convert('LA')
        return img
    
    def run(self, im):
        im = np.array(im) 
        im = self.transform(image=im)['image']
        im = Image.fromarray(im, 'RGB')
        return im
    
    def __call__(self, inpath, outpath):
        for file in os.listdir(inpath):
            if 'CVDD' in file:
                multiple = 15
            else:
                multiple = 12

            filename = file.split('.')
            path = os.path.join(inpath, file)
            out_path = os.path.join(outpath, f'{filename[0]}_0_{filename[1]}')
            if self.for_stamp:
                shutil.copy(path, out_path)

            im = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            for i in range(multiple):
                img = im.copy()

                img = self.transform(image=im)['image']
                
                if self.for_stamp:
                    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
                    img = Image.fromarray(img, 'RGBA')
                    img = self.random_opacity(img)
                    img = self.random_gray(img)
                    img.thumbnail((256,256))
                else:
                    img = Image.fromarray(img, 'RGB')
                
                img.save(f'{outpath}/{filename[0]}_{i+1}.{filename[1]}')

                # break
            break

if __name__ == '__main__':
    # # For stamp
    # augmentator = Augmentator()
    # folder = 'ori_stamp'
    # out_folder = 'aug_stamp'
    # augmentator(folder, out_folder)

    # For doc, debugging
    augmentator = Augmentator(for_stamp=False)
    folder = 'ori_doc'
    out_folder = 'aug_doc'
    augmentator(folder, out_folder)
