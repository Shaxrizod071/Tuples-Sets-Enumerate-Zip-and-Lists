def print_with_index(items: list) -> None:
    """
    Use enumerate to print each item in a list with its index.
    Args:
        items (list): List of items to print with their indices
    Returns:
        None: Prints each item with its index
    """
    data=enumerate(items)
    return list(data)
print(print_with_index(['q','v','a','a']))
