a = set(input().split(","))
b = set(input().split(","))


a_list = list(a)
b_list = list(b)

a_subs = ""
for i in range(0, len(a_list) + 1):
    for j in range(i, len(a_list)):
        if (j + 1) == len(a_list):
            a_subs += f"({",".join(a_list[i:])})"
        else:
            a_subs += f"({",".join(a_list[i:j+1])})"
print("A subsets : " + a_subs)

b_subs = ""
for i in range(0, len(b_list) + 1):
    for j in range(i, len(b_list)):
        if (j + 1) == len(b_list):
            b_subs += f"({",".join(b_list[i:])})"
        else:
            b_subs += f"({",".join(b_list[i:j+1])})"
print("B subsets : " + b_subs)


print("Is a a subset of b : " + str(a.issubset(b)))
print("Is b a subset of a : " + str(b.issubset(a)))
