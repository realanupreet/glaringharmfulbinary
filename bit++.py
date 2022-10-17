x = 0
n = int(input())
for i in range(n):
    a = input()[1]
    if a == "+":
        x += 1
    elif a == "-":
        x -= 1
print(x)
