import os
import random
from itertools import product  

from tqdm import tqdm
from PIL import Image

from augmentation import Augmentator


class StampMarker():
    def __init__(self, doc_folder, stamp_folder):
        self.multiples = 1
        self.augmentator = Augmentator(for_stamp=False)
        self.doc_stamp = self.get_data(doc_folder, stamp_folder)

    def get_data(self, doc_folder, stamp_folder):
        doc_paths = [os.path.join(doc_folder, f) for f in os.listdir(doc_folder)]
        stamp_paths = [os.path.join(stamp_folder, f) for f in os.listdir(stamp_folder)]
        doc_stamp = list(product(doc_paths, stamp_paths))
        
        print(f'* {len(doc_paths)} doc images, {len(stamp_paths)} stamp images')
        return doc_stamp

    @staticmethod
    def random_crop(doc, stamp):
        doc_w, doc_h = doc.size
        stamp_w, stamp_h = stamp.size
        
        x = random.randrange(0, doc_w-stamp_w, doc_w//10)
        y = random.randrange(0, doc_h-stamp_h, doc_h//10)
        doc = doc.crop((x, y, x+stamp_w, y+stamp_h))
        return doc
    
    def process(self, doc_path, stamp_path):
        output_basename = '_'.join([os.path.basename(doc_path)[:-4], os.path.basename(stamp_path)[:-4]])

        ori_doc = Image.open(doc_path)
        ori_stamp = Image.open(stamp_path).convert("RGBA")

        for i in range(1, self.multiples+1):
            output_name = f'{output_basename}_{i}'

            doc = ori_doc.copy()
            stamp = ori_stamp.copy()

            doc = self.random_crop(doc, stamp)

            # Doc augmentation
            doc = self.augmentator.run(doc)
            doc.save(f'dataset_2/test/labels/{output_name}.png')

            doc.paste(stamp, (0,0), stamp)
            doc.save(f'dataset_2/test/images/{output_name}.png')

    def run(self):
        num = 100
        print(f'* Generating {num} images...')
        for i in tqdm(range(num)):
            self.process(*self.doc_stamp[15000:][i])
            # break

if __name__ == '__main__':
    doc_folder = 'ori_doc'
    stamp_folder = 'aug_stamp'
    stamp_marker = StampMarker(doc_folder, stamp_folder)
    stamp_marker.run()

