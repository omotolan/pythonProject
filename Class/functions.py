def get_digit(number: int, position: int) -> int:
    """"
    return digit at position in number, counting from right

    >>> get_digit(234, 0)
    4
    >>> get_digit(234, 2)
    2
    >>> "hello"
    'hello'
    >>> '2' + 3 # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError:
    """
    # assert 6 == 2, "4 is not equal 2"
    return number // (10 ** position) % 10


x = get_digit(4654, 2)
print(x)
# print(get_digit(2435, 3))
