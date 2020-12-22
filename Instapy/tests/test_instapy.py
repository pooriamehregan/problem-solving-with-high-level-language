import random
import numpy as np

from bin.python_files.python_color2gray import python_color2gray
from bin.numpy_files.numpy_color2gray import numpy_color2gray
from bin.numba_files.numba_color2gray import numba_color2gray
from bin.python_files.python_color2sepia import python_color2sepia
from bin.numpy_files.numpy_color2sepia import numpy_color2sepia
from bin.numba_files.numba_color2sepia import numba_color2sepia
from bin.filters import sepia

random_array = np.random.randint(0, 256, (400, 600, 3), dtype="uint8")


def test_grayscale_image():
    # i don't check function grayscale_image here,
    # because grayscale_image uses numpy implementation and I check numpy here.

    img = python_color2gray(np.copy(random_array))
    equal_rgb(img)

    img = numpy_color2gray(np.copy(random_array))
    equal_rgb(img)

    img = numba_color2gray(np.copy(random_array))
    equal_rgb(img)


# helper function to test_grayscale
def equal_rgb(img):
    assert img.shape == random_array.shape
    # check 3 different random columns,
    # to see if R,G and B in that column have the same value.
    for i in range(3):
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        assert img[y, x, 0] == img[y, x, 1] == img[y, x, 2]


def test_sepia_image():
    # i don't check function sepia_image here,
    # because sepia_image uses numpy implementation and I check numpy here.

    img = python_color2sepia(np.copy(random_array))
    helper_sepia(img)

    img = numpy_color2sepia(np.copy(random_array))
    helper_sepia(img)

    img = numba_color2sepia(np.copy(random_array))
    helper_sepia(img)


# helper function to test_sepia_image
def helper_sepia(img):
    x = random.randint(0, 600)
    y = random.randint(0, 400)

    sep_arr = img[y, x]  # rgb values from a random column of sepia array

    r, g, b = random_array[y, x]  # rgb values from a random column of random array
    tr = int(sepia[0][0] * r + sepia[0][1] * g + sepia[0][2] * b)
    tg = int(sepia[1][0] * r + sepia[1][1] * g + sepia[1][2] * b)
    tb = int(sepia[2][0] * r + sepia[2][1] * g + sepia[2][2] * b)
    if tr > 255: tr = 255
    if tg > 255: tg = 255
    if tb > 255: tb = 255
    check_arr = np.array([tb, tg, tr]).astype("uint8")

    assert np.array_equal(sep_arr, check_arr)
