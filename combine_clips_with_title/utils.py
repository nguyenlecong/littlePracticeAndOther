def get_key(filename):
    key = filename.split('-')[0].split(' ')[1]
    return int(key)


def config():
    from moviepy.config import change_settings
    change_settings(
        {"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})
