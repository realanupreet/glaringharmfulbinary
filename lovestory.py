standard_input = """5
coolforsez
cadafurcie
codeforces
paiuforces
forcescode"""
sample = "codeforces"
for m in range(int(input())):
    s = input()
    d = 0
    for i in range(len(sample)):
        if s[i] != sample[i]:
            d += 1
    print(d)
