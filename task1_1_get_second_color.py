def get_second_color(colors: tuple) -> str:
    """
    Get the second color from a tuple of three colors.
    Args:
        colors (tuple): A tuple containing three color strings
    Returns:
        str: The second color in the tuple
    """
    tuple=('green','yellow','orange','blue')
    return tuple[0:2]
print(get_second_color(tuple))
