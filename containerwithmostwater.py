input_array = [2, 5, 7, 5, 3, 6, 7, 2, 1]


def mostwater(arr):
    maxwater = 0
    l = 0
    r = len(arr)-1
    while l < r:
        water = min(arr[l], arr[r]) * (r-l)
        print(
            f"water between {arr[l]} and {arr[r]} is min({arr[l]}, {arr[r]}) * ({r-l}) = {water}")
        if water > maxwater:
            maxwater = water
            print("maxwater updated to ->", maxwater)
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return maxwater


print(mostwater(input_array))
