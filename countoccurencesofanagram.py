a = "forxxorfxdofr"
b = "for"
bmap = {}
amap = {}

for _ in b:
    if _ not in bmap:
        bmap[_] = 1
    else:
        bmap[_] += 1

wend, wstart = 0, 0
k = len(b)
count = 0
for wend in range(len(a)):
    if a[wend] not in amap:
        amap[a[wend]] = 1
    else:
        amap[a[wend]] += 1
    if wend >= k-1:
        if amap == bmap:
            print("woohoo")
            count += 1
        if amap[a[wstart]] == 1:
            del amap[a[wstart]]
        else:
            amap[a[wstart]] -= 1
        wstart += 1

print(count)
