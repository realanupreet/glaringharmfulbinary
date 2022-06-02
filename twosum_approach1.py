input_array = [3, 5, 8, 4, 6, 7]
input_target = 12


def twosum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i]+arr[j] == target:
                    return [i, j]


print(twosum(input_array, input_target))
