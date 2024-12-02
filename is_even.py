def is_even(n: int) -> None:
    """
    Args:
        n (int): an int value
    """

    if n % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
        
for _ in range(10):
    n = int(input())
    
    is_even(n)