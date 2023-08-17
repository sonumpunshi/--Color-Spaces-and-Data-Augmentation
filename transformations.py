import imageio
import numpy as np
from matplotlib.image import imread, imsave
import random
from numpy.lib import stride_tricks
from skimage import io, color
import skimage.exposure as exposure
import matplotlib.pyplot as plt
from skimage.transform import resize


# Resize using nearest neighbor interpolation
def resize_img(img, factor):

    width_calc = int(img.shape[0] * factor)
    height_calc = int(img.shape[1] * factor)
    resized_img = np.zeros([width_calc, height_calc, img.shape[2]])

    for i in range(width_calc):
        for j in range(height_calc):
            resized_img[i][j] = img[int(i / factor)][int(j / factor)]

    resized_name = "resized_" + str(factor) + '.png'
    imsave(resized_name, resized_img)

# Random crop of image -- only for jpeg
def random_crop(img, size):
    if size > min(img.shape[0], img.shape[1]):
        print("dimension input is bigger than the image. restart the program")
    else:
        a_in = img.shape[0] - size
        b_in = img.shape[1] - size

        x = random.randint(0, a_in)
        y = random.randint(0, b_in)

        x2 = int(x + size)
        y2 = int(y + size)

        img_crop = img[x:x2, y:y2]
        io.imsave('cropped.jpeg', img_crop)
        print("Image crop successful.")
        return img_crop


def extract_patches(img, n):
    height, width, channels = img.shape
    patch_size = int(np.floor(height / n))
    patches = []

    for i in range(0, height, patch_size):
        for j in range(0, width, patch_size):
            x_end = i + patch_size
            y_end = j + patch_size
            if x_end > height:
                x_end = height
            if y_end > width:
                y_end = width
            patch = img[i:x_end, j:y_end, :]
            patches.append(patch)

    return patches


def color_jitter(img, hue, saturation, value, ):
    h=random.uniform(0,hue)
    s=random.uniform(0,saturation)
    v=random.uniform(0,value)

    img_hsv = color.rgb2hsv(img)
    img_hsv[:, :, 0] += (h / 360)
    img_hsv[:, :, 1] += s
    img_hsv[:, :, 2] += v

    imageio.imsave('modified_image_hsv.png', img_hsv, format='png')

if __name__ == '__main__':
    # for random crop: acceptable input is only a jpeg file
    filename = input("Enter the name of the file that needs to be resized: ")
    img = imread(filename)
    img = img[..., :3]

    hue = float(input("Enter a value for hue: "))
    saturation = float(input("Enter a value for saturation: "))
    value = float(input("Enter a value for value modification: "))

    # Use this for color jitter
    if (hue < 0 or hue > 360) or (saturation < 0 or saturation > 1) or (value < 0 or value > 1):
        print("Warning. Values incorrect. Restart ...\n")
        raise SystemExit
    else:
        color_jitter(img, 60, 0.1, 0.5)

    # use this for random_crop
    factor = float(input("What is the factor/size? "))
    random_crop(img, factor)
    resize_img(img, factor)

    #extract_patch
    img = plt.imread('image1.jpeg')
    patches = extract_patches(img, n=3)

    for i, patch in enumerate(patches):
        plt.imsave(f'patch_{i}.png', patch)
    patches = extract_patches(img, n=3)

    for i, patch in enumerate(patches):
        plt.imsave(f'patch_{i}.png', patch)
