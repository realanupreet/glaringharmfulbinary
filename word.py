n = input()
upper, lower = 0, 0
for c in n:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
if upper > lower:
    print(n.upper())
else:
    print(n.lower())
