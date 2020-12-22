import numpy as np
from bin.filters import sepia


def numpy_color2sepia(img, filt=sepia):
    """ produces the seoia version of the given image
    :param img: image
    :param filt: the filter to apply to image, in this case sepia
    :return: sepia image as unsigned int array
    """
    image = np.copy(img.astype(float))
    new_image = np.copy(image)

    new_image[:, :, 0] = (image[:, :] * filt[2]).sum(axis=2)
    new_image[:, :, 1] = (image[:, :] * filt[1]).sum(axis=2)
    new_image[:, :, 2] = (image[:, :] * filt[0]).sum(axis=2)

    new_image[np.where(new_image > 255)] = 255

    return new_image.astype("uint8")
