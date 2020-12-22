import numpy as np


def numpy_color2gray(img_array):
    """ Make a grayscale copy of the given image (numpy array)
    :param img_array: a numpy array representing the image
    :return: grayscaled copy
    """
    copy_array = np.array(img_array, dtype=float)
    copy_array[:, :, 0] *= 0.21
    copy_array[:, :, 1] *= 0.72
    copy_array[:, :, 2] *= 0.07
    sum_arr = (copy_array.sum(axis=2, keepdims=True))[:, :, 0]
    copy_array[:, :, 0] = sum_arr
    copy_array[:, :, 1] = sum_arr
    copy_array[:, :, 2] = sum_arr
    return copy_array.astype("uint8")
