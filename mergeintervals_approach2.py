intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]


def merge(self, intervals):
    i = 0
    ans = []
    intervals.sort()

    ans.append(intervals[0])
    for i in intervals[1:]:
        if i[0] <= ans[-1][1]:
            ans[-1][1] = max(i[1], ans[-1][1])
        else:
            ans.append(i)
    return ans


print(f"{merge(self, intervals)}")
