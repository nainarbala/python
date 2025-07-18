def find_duplicate(a, b):
    """
    Finds and returns a list of duplicate elements present in both input lists.

    Args:
        a (list): The first list of elements.
        b (list): The second list of elements.

    Returns:
        list: A list containing elements that are present in both `a` and `b`. Each element appears only once in the result.

    Example:
        >>> find_duplicate([1, 2, 3], [2, 3, 4])
        [2, 3]
    """
    # Return a list of elements that are present in both a and b
    return list(set(a) & set(b))

def find_big_numner(a, b, c, d, e):
    # Return the largest number among the five arguments
    return max(a, b, c, d, e)