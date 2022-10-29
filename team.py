n = int(input())
count = 0
for i in range(n):
    b = input().split()
    a = int(b[0])+int(b[1])+int(b[2])
    if a >= 2:
        count += 1
print(count)
