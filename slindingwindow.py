arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
sum = 0
for i in range(k):
    print(arr[i])
    sum += arr[i]

ans = []
for i in range(k, len(arr)):
    ans.append(sum/k)
    print("ans appended with ",sum/k)
    sum -= arr[i-k]
    sum += arr[i]

print(ans)
