s = "abbaca"
print(s)
i = 3
print(s[:i]+s[i+1:])

returnees = []


def killdupli(s):  # ca
    if len(s) > 1:
        a = s[0]  # c
        print("a is", a)
        for i in range(1, len(s)):
            print(f"s[{i}] is", s[i])
            if s[i] == a:
                print(i)
                s = s[:i]+s[i+1:]
                s = s[:i-1]+s[i:]
                print("new s i", s)
                killdupli(s)
                returnees.append(s)
                print("returnees is ", returnees)
                print("returned s is", s)

                return returnees[0]
                break
            a = s[i]
            print("a is", a)
    print(returnees)


print("print prints", killdupli(s))
