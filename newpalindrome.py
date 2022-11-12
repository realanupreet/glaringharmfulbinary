standard_input = """3
codedoc
gg
aabaa"""
n = int(input())
for i in range(n):
    a = input()
    rev = ""
    if len(a) % 2 == 0:
        # print("YES")
        # print(a[0:len(a)//2])
        rev = a[0:len(a)//2]
        if (rev+rev) == a:
            print("NO")
        else:
            print("YES")
    else:
        # print("NO")
        # print(a[0:len(a)//2])
        rev = a[0:len(a)//2]
        if (rev+a[len(a)//2]+rev) == a:
            print("NO")
        else:
            print("YES")
    # print()
