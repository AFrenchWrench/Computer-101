def gcd(a: int, b: int) -> int:
    """
    Args:
        a (int) : the first number
        b (int) : the second number
    Returns:
        int : the gcd of a and b
    """

    a_divisors = []
    b_divisors = []

    for i in range(1, (a // 2) + 1):
        if a % i == 0:
            a_divisors.append(i)

    for j in range(1, (b // 2) + 1):
        if b % j == 0:
            b_divisors.append(j)

    a_divisors.reverse()
    b_divisors.reverse()

    if len(a_divisors) < len(b_divisors):
        for n in a_divisors:
            if n in b_divisors:
                return n
    else:
        for n in b_divisors:
            if n in a_divisors:
                return n


a, b = map(int, input().split())

print(gcd(a, b))
