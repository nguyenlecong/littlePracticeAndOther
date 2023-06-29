import time


def use_pdf2image(pdf_path):
        import pdf2image

        pages = pdf2image.convert_from_path(pdf_path, dpi=600)

        for i, page in enumerate(pages):
            dst_filename = f'pdf2image_{i}.png'

            page.save(dst_filename, format='PNG')


# Faster
def use_pymupdf(pdf_path):
    import fitz

    pages = fitz.open(pdf_path)

    for page in pages:
        pix = page.get_pixmap()

        pix.save(f'pymupdf_{page.number}.png')


def main(func):
    pdf_path = '''
    
    start = time.time()

    func(pdf_path)

    end = time.time()
    
    process_time = str(round((end-start)*1000, 3)) + ' ms'
    print(process_time)


if __name__ == '__main__':
    main(use_pdf2image)
    main(use_pymupdf)
