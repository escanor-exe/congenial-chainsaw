def add(a, b):
    """
    Return the sum of two numbers.

    >>> add(2, 3)
    5
    >>> add(-1, 5)
    4
    >>> add(0, 0)
    0
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
