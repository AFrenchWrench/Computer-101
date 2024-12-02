# n, m = map(int, input("Enter two numbers separated with space: ").split())

# n3 = []

# for i in range(n,m+1):
#     if i % 3 == 0:
#         n3.append(i)

# print(n3)


n, m = map(int, input("Enter two numbers separated with space: ").split())

n3 = []

i = n

while i <= m:
    if i % 3 == 0:
        n3.append(i)
    i += 1

print(n3)
