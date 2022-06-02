input_string = "{}((({})))(([}]))"


def vParen(str):
    arr = []
    braces = {"(": ")", "[": "]", "{": "}"}
    for c in str:
        if c in braces:
            arr.append(c)
        elif c == braces[arr[-1]]:
            arr.pop()
        else:
            return False

    if len(arr) == 0:
        return True


print(vParen(input_string))


# input_string = "{}((({})))(([]))"


# def vParen(str):
#     c = 0
#     for letter in str:
#         print("reading", letter, "C value", c)
#         if letter == "(" or letter == "[" or letter == "{":
#             c += 1
#             print("c++", c)
#         elif letter == ")" or letter == "]" or letter == "}":
#             c -= 1
#             print("c--", c)
#         if c < 0:
#             return False
#     print("at last c is", c)
#     if c == 0:
#         return True
#     else:
#         return False


# print(vParen(input_string))
