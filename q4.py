def transform_num(n: int, p: int):
    """
    Transform and print int n.

    :param n: a positive int.
    :param p: an int: 1 <= p <= length of n.
    :return: a transformed int described by the problems document.
    """
    int_as_str = str(n)
    array_index_p = len(str(n)) - p
    pth_digit = int(int_as_str[array_index_p])
    transformed_int_as_str = ""
    for digit in int_as_str[0:array_index_p]:
        transformed_int_as_str += str((int(digit) + pth_digit) % 10)
    transformed_int_as_str += str(pth_digit)
    for digit in int_as_str[array_index_p + 1:]:
        transformed_int_as_str += str(int(digit) - pth_digit)[-1]
    return transformed_int_as_str


def transform_array_of_nums(data_sets: [[int, int]]):
    """
    Transform and print outputs for the data sets data_sets.

    :param data_sets: a list of lists of two ints.
    """
    for i, data_set in enumerate(data_sets):
        print(f"{i + 1}. {transform_num(*data_set)}")


if __name__ == '__main__':
    test_input_1 = [
        [296351, 5],
        [762184, 3],
        [45873216, 7],
        [19750418, 6],
        [386257914, 5]
    ]

    test_input_2 = [
        [4318672, 4],
        [35197545, 1],
        [975318642, 9],
        [9876543210, 5],
        [314159265358, 10]
    ]
    transform_array_of_nums(test_input_2)
