import numpy as np
from bin.filters import sepia

def python_color2sepia(img, filt=sepia):
    """ produces the seoia version of the given image
    :param img: image
    :param filt: the filter to apply to image, in this case sepia
    :return: sepia image as unsigned int array
    """
    image = np.copy(img)
    for y in range(len(image)):
        for x in range(len(image[y])):
            r, g, b = image[y][x]

            tr = int(filt[0][0] * r + filt[0][1] * g + filt[0][2] * b)
            tg = int(filt[1][0] * r + filt[1][1] * g + filt[1][2] * b)
            tb = int(filt[2][0] * r + filt[2][1] * g + filt[2][2] * b)

            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            image[y, x] = tb, tg, tr

    return image.astype("uint8")
