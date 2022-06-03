matrix = [[1, 2, 3], [4, 5, 6], [9, 7, 0]]

a = matrix
print(a)
for i in range(len(a)):
    print(a[i])
for i in range(len(a)):
    # print(a[i])
    for j in range(i, len(a[i])):
        # print(a[i][j])
        temp = 0

        temp = a[i][j]
        print(f"temp is {temp}")
        a[i][j] = a[j][i]
        print(f"a[{i}][{j}] becomes {a[i][j]} because a[{j}][{i}] is {a[j][i]}")
        a[j][i] = temp
        print(f"a[{j}][{i}] becomes {a[j][i]} because temp is {temp}")

print("----------")

print(a)
for i in range(len(a)):
    print(a[i])
