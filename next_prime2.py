def next_prime(n: int, k: int) -> int:
    """
    Args:
        n (int): The starting number
        k (int): The Kst appearance of a prime number
    Returns:
        int: The Kst appearance of a prime number bigger than n
    """

    while True:
        n += 1
        prime = True
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            k -= 1
            if k == 0:
                return n


n, k = map(int, input().split())

print(next_prime(n, k))
