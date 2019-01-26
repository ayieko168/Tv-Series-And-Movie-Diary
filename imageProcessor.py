from PIL import Image  # third party


def delete_file(file):

    print(file)


def convert_format(image_file):

    imge_format = 'GIF'.lower()  # GIF
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

def resize_image(image_file):

    size = 238, 317   # size in pixels

    im = Image.open(image_file)
    new_image = im.resize(size)
    new_image.save(image_file)

    # print(im.size)  # Output: old size
    # print(new_image.size)  # Output: new size

    return image_file





