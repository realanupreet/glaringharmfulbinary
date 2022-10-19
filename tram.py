n = int(input())
intram = 0
maxintram = 0
for i in range(n):
    a, b = [int(x) for x in input().split()]
    intram -= a
    intram += b
    maxintram = max(maxintram, intram)

print(maxintram)
