# n = int(input("Enter a number: "))

# fibonacci_sequence = [0,1]

# for i in range(2,n):
#     last_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
#     fibonacci_sequence.append(last_number)
    
# print(fibonacci_sequence)


n = int(input("Enter a number: "))

fibonacci_sequence = [0,1]

i = 2

while i < n:
    last_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
    fibonacci_sequence.append(last_number)
    i += 1
    
print(fibonacci_sequence)