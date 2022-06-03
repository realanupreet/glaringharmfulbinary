matrix = [[1, 2, 3], [4, 5, 6]]

a = matrix
ab = []
print(a)
for i in range(len(a)):
    print(a[i])

print("===============")

for j in range(len(a[i])):
    ab.append([])

for i in range(len(a)):
    print(a[i])
    for j in range(len(a[i])):
        # ab.append([])
        print(a[i][j])
        ab[j].append(a[i][j])
        print("ab is", ab)

print("----------")

print(ab)
for i in range(len(ab)):
    print(ab[i])
