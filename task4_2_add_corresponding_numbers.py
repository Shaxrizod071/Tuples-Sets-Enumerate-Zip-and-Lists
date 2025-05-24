def add_corresponding_numbers(list1: list, list2: list) -> list:
    """
    Add corresponding numbers from two lists.
    Args:
        list1 (list): First list of numbers
        list2 (list): Second list of numbers
    Returns:
        list: List containing sum of corresponding numbers
    """
    return [key+value for key,value in zip(list1, list2)]
print(add_corresponding_numbers([1,2,3,4],[1,2,3,4]))
