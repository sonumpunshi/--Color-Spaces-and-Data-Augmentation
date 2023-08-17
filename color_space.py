import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imread
from skimage import io, color
import imageio

def normalize_img(R,G,B):
    return R/255,G/255,B/255

def rgb_to_hsv(img,h,s,v):
    img_hsv = color.rgb2hsv(img)
    img_hsv[:, :, 0] += (h/360)
    img_hsv[:, :, 1] += s
    img_hsv[:, :, 2] += v

    imageio.imsave('modified_image_hsv.png', img_hsv, format = 'png')

# def rgb_to_hsv(img):
#     R=img[0]/255
#     G=img[1]/255
#     B=img[2]/255
#     print(R)
#     V = max(R,G,B)
#     C = V - min(R,G,B)
#
#     #Saturation:
#     if V == 0:
#         S = 0
#     else:
#         S = C/V
#
#     #Hue:
#     if C == 0:
#         H = 0
#     elif V == R:
#         H = (((G-B)/C) % 6) * 60
#     elif V == G:
#         H = (((B-R)/C) + 2) * 60
#     elif V == B:
#         H = (((R-G)/C) + 4) * 60
#
#     return H,S,V
#

def hsv_to_rgb(name):
    img_rgb = color.hsv2rgb(img)
    imageio.imsave('modified_image_rgb.png', img_rgb, format = 'png')

# def plot_rgb_to_hsv(name):
#     rgb_image = plt.imread(name)
#     hsv = rgb_to_hsv(rgb_image, 60, 0.5, 0.5)
#     plt.figure(figsize=(6, 12))
#     plt.title("HSV Image")
#     plt.imshow(hsv)
#     plt.axis('off')
#     plt.gcf().set_dpi(100)
#     plt.savefig('rgb_to_hsv_output.JPG')
#     plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = input('Please input name of the file: ')
    hue = float(input("Enter a value for hue: "))
    saturation = float(input("Enter a value for saturation: "))
    value = float(input("Enter a value for value modification: "))
    if (hue<0 or hue>360) or (saturation<0 or saturation>1) or (value<0 or value>1):
        print("Warning. Values incorrect. Restart ...\n")
        raise SystemExit
    else:
        img = io.imread(name)
        rgb_to_hsv(img, hue, saturation, value)
        hsv_to_rgb(name)
