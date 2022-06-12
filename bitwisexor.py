a = [1, 2]
b = [4, 10]
c = []

for i in range(len(a)):
    for j in range(len(b)):
        c.append(a[i] | b[j])

xortillnow = int()
for c in c:
    xortillnow = xortillnow ^ c


def bitwisexor(A, B):
    a = A
    b = B
    c = []

    for i in range(len(a)):
        for j in range(len(b)):
            c.append(a[i] | b[j])

    xortillnow = int()
    for c in c:
        xortillnow = xortillnow ^ c
    return xortillnow


print(bitwisexor(a, b))
