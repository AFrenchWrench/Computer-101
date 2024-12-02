def next_prime(n: int) -> int:
    """
    Args:
        n (int): The starting number
    Returns:
        int: The first prime number bigger than n
    """

    while True:
        n += 1
        prime = True
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            return n

n = int(input())

print(next_prime(n))