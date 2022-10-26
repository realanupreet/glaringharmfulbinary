k, n, w = [int(x) for x in input().split()]
total = 0
for i in range(1, w+1):
    total += i*k
print(total-n if (total-n) > 0 else 0)
