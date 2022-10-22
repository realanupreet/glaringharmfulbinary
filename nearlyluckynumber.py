def chkl(n):
    n = str(n)
    for c in n:
        if c == "4" or c == "7":
            pass
        else:
            return False
    return True


n = input()
l = 0
for i in n:
    if i == "4" or i == "7":
        l += 1

if chkl(l):
    print("YES")
else:
    print("NO")
