from numba import jit
import numpy as np


def numba_color2gray(img):
    cp_img = numba_helper(np.copy(img))
    """ returns an grayscaled version of the provided numpy array
    :param img: an image as a 3d numpy array
    :return: grayscaled version of the image
    """
    return cp_img.astype("uint8")


@jit
def numba_helper(image_array):
    for i in range(len(image_array)):
        for j in range(len(image_array[i])):
            col = image_array[i][j]
            color_sum = col[0] * 0.21 + col[1] * 0.72 + col[2] * 0.07
            col[0] = col[1] = col[2] = color_sum
    return image_array
