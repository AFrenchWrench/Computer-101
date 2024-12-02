# n = int(input("Enter a number: "))

# sum_of_sequence = 0

# for i in range(3, n + 1):
#     sum_of_sequence += (1 / i)

# print(f"{sum_of_sequence:.3f}")

n = int(input("Enter a number: "))

sum_of_sequence = 0

i = 3

while i <= n:
    sum_of_sequence += 1 / i
    i += 1

print(f"{sum_of_sequence:.3f}")
