import cv2
import pdf2image
import numpy as np

pdf_path = ''

images = pdf2image.convert_from_path(pdf_path, dpi=500)

for i, image in enumerate(images):
    image.save(f'{i+1}.jpg', 'JPEG')
    # image = np.array(image)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # cv2.imwrite(f'{i+1}.jpg', image)
