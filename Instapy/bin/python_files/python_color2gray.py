import numpy as np


def python_color2gray(image_array):
    copy_image = np.array(image_array, dtype=float)
    """ returns an grayscaled version of the provided numpy array
    :param image_array: an image as a 3d numpy array
    :return: grayscaled version of the image
    """
    for i in range(len(copy_image)):
        for j in range(len(copy_image[i])):
            col = copy_image[i][j]
            color_sum = col[0] * 0.21 + col[1] * 0.72 + col[2] * 0.07
            col[0] = col[1] = col[2] = color_sum
    return copy_image.astype("uint8")
