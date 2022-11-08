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
n = int(input())
for k in range(n):
    smap = {"10": 10000000, "01": 10000000, "11": 10000000, "00": 10000000}
    for i in range(int(input())):
        h, s = [a for a in input().split()]
        h = int(h)
        
        smap[s] = min(smap[s], h)
    # print(smap)
    print(min(smap["10"]+smap["01"], smap["11"])) if min(smap["10"]+smap["01"], smap["11"]) != 10000000 else print(-1)
