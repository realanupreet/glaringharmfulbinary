arr = [2, 1, 5, 1, 3, 2]
k = 3

# k=3
wstart, msum, maxsum = 0, 0, 0
for wend in range(len(arr)):
    msum += arr[wend]
    if wend >= k-1:
        maxsum = max(msum, maxsum)
        msum -= arr[wstart]
        wstart += 1

print(maxsum)
