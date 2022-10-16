for i in range(5):
    a = input().split()
    for j in range(5):
        if a[j] == "1":
            r, c = i+1, j+1
            break
print(abs(3-r)+abs(3-c))
