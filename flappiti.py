a = 5
b = [[1, 2, 3], [2, 5, 0], [1, 1, 4], [3, 4, 0], [2, 6, 0], [3, 1, 0]]
# x = [0]*a
# y = [0]*a
# ans = []
# for i in range(len(b)):
#     if b[i][0] == 1:
#         print("1")
#         l = b[i][1]
#         r = b[i][2]
#         for j in range(l-1, r):
#             if x[j] == 0:
#                 x[j] = 1
#             elif x[j] == 1:
#                 x[j] = 0
#     elif b[i][0] == 2:
#         for k in range(a):
#             y[k] += x[k]*b[i][1]
#         print("2")
#     else:
#         print("y[j]", y[b[i][0]])
#         ans += [y[b[i][0]]]
#         print("3")

#     # print()


def func(A, B):
    a = A
    b = B
    x = [0]*a
    y = [0]*a
    ans = []
    for i in range(len(b)):
        if b[i][0] == 1:
            # print("1")
            l = b[i][1]
            r = b[i][2]
            for j in range(l-1, r):
                if x[j] == 0:
                    x[j] = 1
                elif x[j] == 1:
                    x[j] = 0
        elif b[i][0] == 2:
            for k in range(a):
                y[k] += x[k]*b[i][1]
            # print("2")
        else:
            # print("y[j]", y[b[i][0]])
            ans += [y[b[i][0]]]
            # print("3")
    return ans


print(func(a, b))
