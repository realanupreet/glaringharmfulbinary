n = input()
flag = 0
for i in n.split("0"):
    if len(i) >= 7:
        flag += 1
        break
if flag == 0:
    for i in n.split("1"):
        if len(i) >= 7:
            flag += 1
            break
if flag == 0:
    print("NO")
else:
    print("YES")
