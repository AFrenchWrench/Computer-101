def most_count(n: int) -> None:
    """
    prints out the number that appeared the most with the count

    Args:
        n (int): the count of number to get input
    Returns:
        None
    """
    numbers = {}
    
    for _ in range(n):
        number = input()
        if number in numbers:
            numbers[number] += 1
        else:
            numbers[number] = 1
            
    max_appearance = max(numbers.values())
    
    for key,value in numbers.items():
        if value == max_appearance:
            print(f"{key}: {value}")


n = int(input())

most_count(n)