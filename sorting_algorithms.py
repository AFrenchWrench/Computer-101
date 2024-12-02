numbers = [1,2,3,4,5,6,7,8]
print("Initial List:", numbers)

for pass_num in range(len(numbers) - 1):
    swapped = False
    print(f"\nPass {pass_num + 1}:")
    for idx in range(len(numbers) - 1 - pass_num):
        if numbers[idx] > numbers[idx + 1]:
            print(f"  Swapping {numbers[idx]} and {numbers[idx + 1]}")
            numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
            swapped = True
        print("  Current State:", numbers)
    if not swapped:
        print("  No swaps in this pass, stopping early.")
        break

print("\nSorted List:", numbers)


numbers = [8, 6, 2, -5, -8, 14, 3, 10, 5, -3]
print("Initial List:", numbers)

for current_index in range(1, len(numbers)):
    current_value = numbers[current_index]
    position = current_index - 1
    print(f"\nInserting {current_value}:")
    while position >= 0 and current_value < numbers[position]:
        print(
            f"  {current_value} < {numbers[position]}, shifting {numbers[position]} to the right"
        )
        numbers[position + 1] = numbers[position]
        position -= 1
        print("  Current State:", numbers)
    numbers[position + 1] = current_value
    print(f"  Placed {current_value} at position {position + 1}")
    print("  Current State:", numbers)

print("\nSorted List:", numbers)
