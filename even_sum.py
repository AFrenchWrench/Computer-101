# n = int(input("Enter a number: "))

# sum_of_sequence = 0

# for i in range(2, n + 1, 2):
#     sum_of_sequence += i

# print(sum_of_sequence)


n = int(input("Enter a number: "))

sum_of_sequence = 0

i = 2

while i <= n:
    sum_of_sequence += i
    i += 2

print(sum_of_sequence)