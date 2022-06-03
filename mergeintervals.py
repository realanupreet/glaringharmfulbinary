intervals = [[1, 4], [5, 6], [6, 8], [10, 13]]


def f(x):
    return x[0]


def killoverlaps(intervals):
    if len(intervals) == 1:
        return intervals
    intervals = sorted(intervals, key=f)
    print(f"sorted intervals are -> {intervals}")
    res = []
    print(f"res is -> {res}")
    current = intervals[0]
    print(f"current goes -> {current}")
    for i in intervals[1:]:
        print(f"i is {i}")

        if current[1] >= i[0]:
            print(f"{current[1]} > {i[0]}")
            current[1] = i[1]
            print(f"current is now {current}")
            res.append(current)
            print(f"updated res is {res}")
        else:

            # res.append(current)
            res.append(i)
            print(f"res appended in else block as {res}")
        print(f"new current is {current} ")

    print(f"at lasr res is {res}")
    return res


print(killoverlaps(intervals))
