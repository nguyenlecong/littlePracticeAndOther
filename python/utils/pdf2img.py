import os
import cv2
import fitz
import numpy as np
from tqdm import tqdm

filters = ['JPXDecode', 'CCITTFaxDecode', 'FlateDecode', 'JBIG2Decode']


def get_type_page(min_size, max_size):
    if 400 <= min_size <= 500 and 500 <= max_size <= 600:
        return "A5"
    if 500 < min_size <= 800 and 600 < max_size <= 900:
        return "A4"
    if 800 < min_size <= 1100 and 900 < max_size <= 1550:
        return "A3"
    if 1100 < min_size <= 1550 and 1550 < max_size <= 2200:
        return "A2"
    return "Unknown"


def pix2np(pix):
    im = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
        pix.h, pix.w, pix.n)
    if pix.n == 3:
        im = np.ascontiguousarray(im[..., [2, 1, 0]])  # rgb to bgr
    else:
        im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    return im


def page2np(page, scale=(6, 6)):
    image_matrix = fitz.Matrix(fitz.Identity)
    image_matrix.preScale(*scale)
    pix = page.getPixmap(alpha=False, matrix=image_matrix)
    im = pix2np(pix)
    return im


def doc2img(doc):
    images = []
    type_pages = []
    for i in range(len(doc)):
        current_page = doc.loadPage(i)
        page_width, page_height = current_page.rect.width, current_page.rect.height

        # Get type of page (A2, A3, A4)
        min_size = min(page_width, page_height)
        max_size = max(page_width, page_height)
        type_of_page = get_type_page(min_size, max_size)
        type_pages.append(type_of_page)

        to_scale = False
        if len(doc.getPageImageList(i)) == 1:
            img = doc.getPageImageList(i)[0]
            xref = img[0]

            item = list(img)
            item[-1] = 0
            image_rect = current_page.getImageBbox(item)

            width_image_rect = int(image_rect[2]-image_rect[0])
            height_image_rect = int(image_rect[3] - image_rect[1])

            if width_image_rect >= 0.5 * page_width and height_image_rect >= 0.5*page_height:
                if img[8] == "DCTDecode":
                    pix = fitz.Pixmap(doc, xref)
                    if pix.n - pix.alpha < 4:       # this is GRAY or RGB
                        im = pix2np(pix)
                    else:               # CMYK: convert to RGB first
                        pix1 = fitz.Pixmap(fitz.csRGB, pix)
                        im = pix2np(pix1)
                elif img[8] in filters:
                    pix = fitz.Pixmap(doc, xref)
                    im = pix2np(pix)
                else:
                    to_scale = True
            else:
                to_scale = True
        else:
            to_scale = True

        if to_scale:
            im = page2np(current_page)

        images.append(im)
    return images, type_pages


def pdf2image_fitz(pdf_obj):
    doc = fitz.open(pdf_obj)
    #if len(doc) == 1:
    #    images = ([], [])
    #else:
    images = doc2img(doc)
    doc.close()
    return images


class PdfExtractor():
    def __init__(self):
        pass

    def extract(self, pdf_path):
        pages, type_pages = pdf2image_fitz(pdf_path)
        return pages, type_pages


def resize_image_page(page_image, type_page):
    img_height, img_width = page_image.shape[:2]
    if type_page == "A4":
        resize_width = 1654
        resize_height = 2340
    elif type_page == "A3":
        resize_width = 2340
        resize_height = 3300
    elif type_page == "A2":
        resize_width = 3300
        resize_height = 4680
    else:
        # keep ratio
        dim_min = min(img_width, img_height)
        dim_max = max(img_width, img_height)
        resize_width = 1654
        resize_height = int(1654*dim_max/dim_min)

    if img_height > img_width:
        resize_dim = (resize_width, resize_height)
    else:
        resize_dim = (resize_height, resize_width)
    resize_image = cv2.resize(page_image, resize_dim,
                              interpolation=cv2.INTER_AREA)
    return resize_image


class Preprocessor():
    def __init__(self):
        self.pdf_extractor = PdfExtractor()

    def process(self, path, save_path):
        pdf_name = os.path.basename(path)
        prefix_img_name = pdf_name[:-4] + "_page"
        prefix_img_path = os.path.join(save_path, prefix_img_name)
        pages, type_pages = self.pdf_extractor.extract(path)

        ret_resized_pages = []

        for i, (page, type_page) in enumerate(zip(pages, type_pages)):
            resized_page = resize_image_page(page, type_page)
            cv2.imwrite(f'{prefix_img_path}_{i}.png', resized_page)
            ret_resized_pages.append(resized_page)


if __name__ == '__main__':
    processor = Preprocessor()
    pdf_folder = '/hdd/nguyenlc/dms/data/ARS/Mau08'
    #pdf_folder = '/hdd/nguyenlc/dms/data/ARS/Real Unlabeled Data'
    for pdf in tqdm(os.listdir(pdf_folder)):
        if 'pdf' in pdf:
            pdf_path = os.path.join(pdf_folder, pdf)
            processor.process(pdf_path, 'images')

            # break
