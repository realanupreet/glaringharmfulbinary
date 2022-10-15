n = int(input())
s = input()
a = 0
for c in s:
    if c == "A":
        a += 1

d = n-a
if a == d:
    print("Friendship")
elif a > d:
    print("Anton")
else:
    print("Danik")
