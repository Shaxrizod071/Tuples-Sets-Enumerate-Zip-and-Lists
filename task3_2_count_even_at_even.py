def count_even_at_even(numbers: list) -> int:
    """
    Count how many even numbers are at even indexes.
    Args:
        numbers (list): List of integers
    Returns:
        int: Count of even numbers at even indexes
    """
    x=0
    for i in numbers:
     if i%2==0:
       x+=1
    return x
print(count_even_at_even([1,2,3,4,5,6,7,8,9,10]))
