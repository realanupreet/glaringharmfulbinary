n = [int(x) for x in input().split("+")]
n.sort()
print("+".join(str(x) for x in n))
