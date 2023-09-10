k = 3
arr = [12, -1, -7, 8, -15, 30, 16, 38]

neg = []
wstart, wend = 0, 0
for wend in range(len(arr)):
    if arr[wend] < 0:
        neg.append(arr[wend])
        # print(neg)
    if wend >= k-1:
        print(neg[0]) if len(neg) > 0 else print("haha")
        if arr[wstart] < 0:
            neg.pop(0)
        wstart += 1
