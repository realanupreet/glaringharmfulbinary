a = [[0, 4, 8], [6, 0, 0], [5, 9, 7]]
print(a)
row0 = []
col0 = []
for i in range(len(a)):
    print(f"i[{i}] row contains {a[i]}")
    for j in range(len(a[i])):
        print(f"j[{j}] containes {a[i][j]}")
        if a[i][j] == 0:
            row0.append(i)
            col0.append(j)

for i in range(len(a)):
    for j in range(len(a[i])):
        if i in row0:
            a[i][j] = 0
        if j in col0:
            a[i][j] = 0

print(a)
