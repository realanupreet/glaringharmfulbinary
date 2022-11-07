num1 = "0"
num2 = "0"


def convtoint(a):
    num = 0
    for i, n in enumerate(a):
        # print(n,(ord(n)-48)*10**(len(num2)-i-1))
        num += (ord(n)-48)*10**(len(a)-i-1)
    return num


# print(convtoint(num1))
# print(convtoint(num2))
print(convtoint(num1)+convtoint(num2))
ans = (convtoint(num1)+convtoint(num2))
realans = ""
if ans==0:
    return "0"
while ans > 0:
    print(chr(ans % 10 + 48), type(chr(ans % 10 + 48)))
    realans = chr(ans % 10 + 48)+realans
    ans = ans // 10
print(realans)
