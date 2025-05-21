def find_oldest(people: list) -> tuple:
    """
    Find the oldest person from a list of tuples (name, age).
    Args:
        people (list): List of tuples containing (name, age) pairs
    Returns:
        tuple: A tuple containing (name, age) of the oldest person
    """
    asd=max(people,key=lambda x: x[1])
    return asd
print(find_oldest([("Ali", 20), ("Sara", 12), ("John", 2)]))
