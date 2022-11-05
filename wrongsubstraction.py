def dividebyone(n):
    if str(n)[-1] == "0":
        return int(str(n)[:-1])
    else:
        return n-1


n, k = [int(x) for x in input().split()]

for i in range(k):
    n = dividebyone(n)
print(n)
