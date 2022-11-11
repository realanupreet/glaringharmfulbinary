standard_input = """6
4
2 00
3 10
4 01
4 00
5
3 01
3 01
5 01
2 10
9 10
1
5 11
3
9 11
8 01
7 10
6
4 01
6 01
7 01
8 00
9 01
1 00
4
8 00
9 10
9 11
8 11
"""

n=int(input())
for k in range(n):
    sk1=-1
    sk2=-1
    bs=-1
    for i in range(int(input())):
        h,s = [a for a in input().split()]
        h=int(h)
        if s=="11":
            bs=min(bs,h) if bs!=-1 else h 
        elif s[0]=="1":
            sk1=min(sk1,h) if sk1!=-1 else h
        elif s[1]=="1":
            sk2=min(sk2,h) if sk2!=-1 else h
    if sk1==-1 and sk2==-1:
        print(bs)
    elif sk2 == -1 and bs!=-1:
        print(min(sk1,bs))
    elif sk1 == -1 and bs!=-1:
        print(min(sk2,bs))
    elif sk1==-1 or sk2==-1:
        print(-1)
    else:
        print(min(sk1+sk2,bs)) if bs!=-1 else print(sk1+sk2)