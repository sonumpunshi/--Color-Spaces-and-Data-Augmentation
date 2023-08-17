import numpy as np
import skimage.io as io
from skimage import transform, exposure


def resize_img(img, scale_factor):
    resized_img = transform.resize(img, ((img.shape[0] // scale_factor, img.shape[1] // scale_factor)))
    return resized_img


def create_pyramid(img, height, file_name):
    scale_factor = 2
    count = 1
    while count < height:
        img = resize_img(img, scale_factor)
        filename = file_name + str(scale_factor) + "x.png"
        img = np.uint8(img * 255)
        io.imsave(filename, img)
        print("Pyramid file: ", filename)
        scale_factor *= 2
        count += 1


if __name__ == '__main__':
    name=input("Enter filename: ")
    img = io.imread(name)
    height = int(input("What is the height of the image pyramid? "))
    create_pyramid(img, height, name)
