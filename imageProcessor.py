from PIL import Image


def convert_format(image_file):

    imge_format = 'GIF'.lower()
    try:
        image_file_new = '{}.{}'.format(image_file.split('.')[0], imge_format)
    except AttributeError:
        image_file_new = image_file

    im = Image.open(image_file)
    # print(im.format)
    im.save(image_file_new, format=imge_format)
    # im1 = Image.open(image_file_new)
    # print(im1.format)

    return image_file_new

    # The file format of the source file.
    # print(im.format)
    # The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
    # print(im.mode)
    # Image size, in pixels. The size is given as a 2-tuple (width, height).
    # print(im.size)


def resize_image(image_file):

    size = 238, 317   # size in pixels

    im = Image.open(image_file)
    new_image = im.resize(size)
    new_image.save(image_file)

    # print(im.size)  # Output: old size
    # print(new_image.size)  # Output: new size

    return image_file





