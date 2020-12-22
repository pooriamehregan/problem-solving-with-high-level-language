# test_array.py
from scripts.Array import Array
import pytest

arr1 = Array((2,), 2, 3)
arr2 = Array((0,))
arr3 = Array((2,), -1, 2)
arr4 = Array((1,), -1)
arr5 = Array((1,), 1)
arr6 = Array((2,), 2, 2)
arr7 = Array((2,), True, False)
arr8 = Array((3,), 2, 3, 4)
arr9 = Array((2,), 4, 3)


def test_print():
    assert str(arr1) == "[2, 3]"
    assert str(arr2) == "[]"


def test_elementwise_add():
    assert str(arr1 + arr3) == "[1, 5]"
    assert str(arr2 + arr2) == "[]"


def test_elementwise_sub():
    assert str(arr1 - arr3) == "[3, 1]"
    assert str(arr2 - arr4) == "[]"


def test_elementwise_mul():
    assert str(arr1 * arr3) == "[-2, 6]"
    assert str(arr1 * arr5) == "[2, 3]"
    assert str(arr1 * 2) == "[4, 6]"


def test_equal():
    assert (arr1 == arr1) == True
    assert (arr1 == arr6) == False


def test_is_equal():
    assert str(arr1.is_equal(arr1)) == "[True, True]"
    assert str(arr1.is_equal(arr3)) == "[False, False]"


def test_mean():
    assert arr1.mean() == 2.5
    assert arr2.mean() is None


def test_averance():
    assert round(arr8.variance(), 1) == 0.7
    assert round(arr9.variance(), 1) == 0.2


def test_min():
    assert arr8.min_element() == 2
    assert arr9.min_element() == 3
    assert arr2.min_element() is None


""" Tests for 2D array """
arr_1 = Array((3, 2), 1, 2, 3, 4, 5, 6)
arr_2 = Array((4, 3), 1, 1, 1, 1, 3, 3, 3, 3, 5, 5, 5, 5)
arr_3 = Array((2, 2), True, True, True, False)


def test_2d_add():
    assert str(arr_1 + arr_1) == "[[2, 4], [6, 8], [10, 12]]"
    assert arr_1 + arr_2 is None


def test_2d_sub():
    assert str(arr_1 - arr_1) == "[[0, 0], [0, 0], [0, 0]]"
    assert arr_2 - arr_1 is None
    assert str(arr_1 - 1) == '[[0, 1], [2, 3], [4, 5]]'


def test_2d_equal():
    assert (arr_1 == arr_1)
    assert not (arr_1 == arr_2)


def test_2d_is_equal():
    assert str(arr_1.is_equal(arr_1)) == "[[True, True], [True, True], [True, True]]"
    assert str(arr_1.is_equal(1)) == "[[True, False], [False, False], [False, False]]"
    with pytest.raises(ValueError):
        arr_1.is_equal(arr_2)


def test_2d_mean():
    assert arr_1.mean() == 3.5
    assert  arr2.mean() is None


def test_2d_min_element():
    assert arr_1.min_element() == 1
    assert arr_2.min_element() == 1



