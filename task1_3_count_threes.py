def count_threes(numbers: tuple) -> int:
    """
    Count how many times 3 appears in the tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        int: The count of number 3 in the tuple
    """
    return numbers.count(3)
print(count_threes((1,2,3,4,5,3,6,3)))
