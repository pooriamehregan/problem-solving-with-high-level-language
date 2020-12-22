def calc_shape(shape):
    product = 1
    for factor in shape:
        product *= factor
    return product


def shape_is_correct(shape, values):
    """ A helper function to help calculate number of array elements ffor nd arrays using shape.
    Args:
        values:
        shape: is the shape of the array (e.g. (2, 2) for 2d array)
    Returns:
        the product av elements is  the tupple (e.g. returns 4 for shape(2, 2) )
    """
    if len(shape) == 0:
        raise ValueError("shape not given!")
    else:
        flat_shape = calc_shape(shape)
        if len(values) != flat_shape:
            raise ValueError('Shape and number of values does not match')


def type_is_correct(values):
    if len(values) > 0:
        elem_type = values[0]
        if isinstance(elem_type, (int, float, bool)):
            for val in values:
                if not isinstance(val, type(elem_type)):
                    raise ValueError("Array can only contain one type of element!")
        else:
            raise ValueError("Array can only contain int, float or bool!")


def group_elements(values, n):
    new_list = []
    for i in range(0, len(values), n):
        temp_list = []
        for j in range(n):
            temp_list.append(values[i + j])
        new_list.append(temp_list)
    return new_list


def shape_values(shape, values):
    shaped = list(values)
    for i in range(len(shape)-1, 0, -1):
        shaped = group_elements(shaped, shape[i])
    return shaped


class Array:
    # Assignment 3.3
    # works with nD arrays
    def __init__(self, shape, *values):
        """
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.

        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        shape_is_correct(shape, values)
        type_is_correct(values)

        self.shape = shape
        self.values = values
        self.shaped_values = shape_values(shape, values)

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        return str(self.shaped_values)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        # check for same type, same shape, and special cases like empty array + array with length grater than 1
        # (according to numpy.array)
        oth_type = type(other)
        arr = None
        if isinstance(other, (int, float)):  # if other element is a number
            if len(self.values) > 0:  # if our array is not empty
                if isinstance(self.values[0], (int, float)):  # if array elements are also number, then add
                    new_list = []
                    for val in self.values:
                        new_list.append(val + other)
                    arr = Array(self.shape, *new_list)
                else:  # not same type
                    return NotImplemented
            else:  # array is empty, number plus empty array equals empty array
                arr = Array((0,))
        elif isinstance(self, type(other)):  # if other element is array
            print("")
            if self.shape == other.shape:  # have same length
                new_list = []
                for i in range(0, len(self.values)):
                    new_list.append(self.values[i] + other.values[i])
                arr = Array(self.shape, *new_list)
            else:  # some special cases
                if self.shape == 0 or other.shape == 0:  # if one array is empty
                    if calc_shape(self.shape) > 1 or calc_shape(
                            other.shape) > 1:  # and other array has more than one element
                        return NotImplemented
                    elif calc_shape(self.shape) == 1 or calc_shape(
                            other.shape) == 1:  # or one array has exactly one element
                        arr = Array((0,))
                if calc_shape(self.shape) == 1:  # if neither arrays are empty
                    sel_val = self.values[0]
                    other_type = type(other.values[0])
                    new_list = []
                    if ((type(sel_val) is other_type) is type(float)) or ((type(sel_val) is other_type) is type(
                            int)):  # if both types are equel and types are numbers
                        for val in other.values:
                            new_list.append(val + sel_val)
                        arr = Array(self.shape, *new_list)
                    else:
                        return NotImplemented
        else:  # other element is neither array nor a number
            return NotImplemented
        return arr

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        # call __add__ with other and return the result
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        if type(other) is int or type(other) is float:  # if number
            new_list = []
            for val in self.values:
                new_list.append(val - other)
            return Array(self.shape, *new_list)
        elif type(self) is type(other):  # if array
            if self.shape == other.shape:  # have same length
                new_list = []
                for i in range(0, len(self.values)):
                    new_list.append(self.values[i] - other.values[i])
                return Array(self.shape, *new_list)
            else:  # some special cases
                if calc_shape(self.shape) == 0 or calc_shape(other.shape) == 0:  # if one array is empty
                    if calc_shape(self.shape) > 1 or calc_shape(
                            other.shape) > 1:  # and other array has more than one element
                        return NotImplemented
                    elif calc_shape(self.shape) == 1 or calc_shape(
                            other.shape) == 1:  # or one array has exactly one element
                        return Array((0,))
                if calc_shape(self.shape) == 1:  # if neither arrays are empty
                    sel_val = self.values[0]
                    other_type = type(other.values[0])
                    new_list = []
                    if type(sel_val) is other_type:
                        if isinstance(other_type, (int, float)):  # if both types are equel and types are numbers
                            for val in other.values:
                                new_list.append(val - sel_val)
                            return Array(self.shape, *new_list)
                        else:
                            return NotImplemented
                    else:
                        return NotImplemented
        else:
            return NotImplemented

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """

        if type(other) is int or type(other) is float:  # if number
            new_list = []
            for val in self.values:
                new_list.append(val * other)
            return Array(self.shape, *new_list)
        elif type(self) is type(other):  # if array
            if self.shape == other.shape:  # have same length
                new_list = []
                for i in range(0, len(self.values)):
                    new_list.append(self.values[i] * other.values[i])
                return Array(self.shape, *new_list)
            else:  # some special cases
                if calc_shape(self.shape) == 0 or calc_shape(other.shape) == 0:  # if one array is empty
                    if calc_shape(self.shape) > 1 or calc_shape(
                            other.shape) > 1:  # and other array has more than one element
                        return NotImplemented
                    elif calc_shape(self.shape) == 1 or calc_shape(
                            other.shape) == 1:  # or one array has exactly one element
                        return Array((0,))
                if calc_shape(self.shape) == 1:  # if neither arrays are empty
                    sel_val = self.values[0]
                    other_type = type(other.values[0])
                    new_list = []
                    if type(sel_val) is other_type:
                        if other_type is int or other_type is float:  # if both types are equel and types are numbers
                            for val in other.values:
                                new_list.append(val * sel_val)
                            return Array(self.shape, *new_list)
                    else:
                        return NotImplemented
                elif calc_shape(other.shape) == 1:
                    oth_val = other.values[0]
                    self_type = type(self.values[0])
                    new_list = []
                    if type(oth_val) is self_type:
                        if type(oth_val) is int or type(
                                oth_val) is float:  # if both types are equel and types are numbers
                            for val in self.values:
                                new_val = val * oth_val
                                new_list.append(new_val)
                            return Array(self.shape, *new_list)
                        else:
                            return NotImplemented
                    else:
                        return NotImplemented
        else:
            return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal. False otherwise.

        """

        if self.shape == other.shape:  # if shapes are equal
            if calc_shape(self.shape) > 0:
                if isinstance(self.values[0], type(other.values[0])):  # if same type
                    if isinstance(self.values[0], (int, float)):
                        for i in range(0, calc_shape(self.shape)):
                            if self.values[i] != other.values[i]:
                                return False
                        return True
                    return NotImplemented
                else:
                    return False
            else:
                return True
        else:
            return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """

        if type(other) is type(self):  # if array
            if self.shape == other.shape:  # if shapes are equal
                if calc_shape(self.shape) > 0:
                    if type(self.values[0]) is int or type(self.values[0]) is float:  # if elements are number
                        new_list = []
                        for i in range(0, calc_shape(self.shape)):
                            new_list.append(self.values[i] == other.values[i])
                        return Array(self.shape, *new_list)
                    else:
                        return NotImplemented
                else:  # both arrays are empty
                    return Array((0,))
            else:
                raise ValueError("Shapes do not match!")
        else:  # other is not array
            if len(self.values) == 0:
                return Array((0,))
            else:
                if type(other) is int or type(other) is float:
                    new_list = []
                    for val in self.values:
                        new_list.append(val == other)
                    return Array(self.shape, *new_list)
                else:
                    return NotImplemented

    def mean(self):
        """Computes the mean of the array

        Only needs to work for numeric data types.

        Returns:
            float: The mean of the array values.

        """
        if calc_shape(self.shape) > 0:  # if not empty
            if isinstance(self.values[0], int) or isinstance(self.values[0], float):  # if number type
                sum_el = 0.0
                for val in self.values:
                    sum_el += val
                return sum_el / len(self.values)

    def variance(self):
        """Computes the variance of the array

        Only needs to work for numeric data types.
        The variance is computed as: mean((x - x.mean())**2)

        Returns:
            float: The mean of the array values.

        """
        if len(self.values) > 0:
            if isinstance(self.values[0], (int, float)):
                x = self - self.mean()
                new_list = []
                for val in x.values:
                    new_list.append(val * val)
                return Array(self.shape, *new_list).mean()

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for numeric data types.

        Returns:
            float: The value of the smallest element in the array.

        """
        if len(self.values) > 0:
            if isinstance(self.values[0], (int, float)):
                min_el = self.values[0]
                for val in self.values:
                    if val < min_el:
                        min_el = val
                return min_el
