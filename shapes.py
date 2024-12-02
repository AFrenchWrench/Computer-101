# n, m = map(int, input("Enter number to create rectangle: ").split())

# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         print(f"[{i}][{j}]", end=" ")

#     print("\n", end="")


n, m = map(int, input("Enter number to create rectangle: ").split())

i = 1

while i <= n:
    j = 1

    while j <= m:
        print(f"[{i}][{j}]", end=" ")
        j += 1

    print("\n", end="")
    i += 1
