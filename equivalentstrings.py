word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]
c1 = ""
c2 = ""
for w in word1:
    c1 += w
for w in word2:
    c2 += w
if c1 == c2:
    print(True)
