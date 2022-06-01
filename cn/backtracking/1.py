
def permutations(word):
    if len(word) == 1:
        return [word]

    perms = permutations(word[1:])
    char = word[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])

    return result


print(permutations("abc"))
