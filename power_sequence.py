def power_sequence(x: int, n: int) -> float:
    """
    Calculates the answer following sequence x - x^2 / 3 + x^3 / 5 ...

    Args:
        x (int): the number in sequence
        n (int): the last power of sequence
    Returns:
        float: the answer to sequence based on x and n
    """

    answer = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            answer -= (x**i) / ((i * 2) - 1)
        else:
            answer += (x**i) / ((i * 2) - 1)

    return answer


x, n = map(int, input().split())

print(f"{power_sequence(x,n):.2f}")

# 3 - 3 + 27/5