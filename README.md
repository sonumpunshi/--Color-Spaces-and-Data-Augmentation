# -Color Spaces and Data Augmentation


Color Spaces and Data AugmentationColor Spaces and Data Augmentation
Developed functions in Python to convert images between the RGB and HSV color spaces using NumPy arrays.

Created an image transformation function to generate random square crops of a given size from an input image, ensuring the crop size is feasible based on the input image dimensions.

Implemented a patch extraction function to return non-overlapping patches from an input image, useful for preprocessing in machine learning applications.

Developed a resizing function to resize images using nearest neighbor interpolation, taking an input image and a scale factor as inputs.

Implemented a color jitter function to randomly perturb the HSV values of an input image by a user-defined amount, leveraging the color space conversion functions developed earlier.

Created an image pyramid function to generate resized copies of an input image in powers of 2, based on a user-defined pyramid height. The function saves the resized copies with appropriate filenames indicating the scale factor.
