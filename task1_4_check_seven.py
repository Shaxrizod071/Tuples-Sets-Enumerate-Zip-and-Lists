
def check_seven(numbers: tuple) -> bool:
    """
    Check if the number 7 exists in a tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        bool: True if 7 is in the tuple, False otherwise
    """
    for i in numbers:
        if i==7 :
            return True
    return False
print(check_seven((1,7,2,42)))
