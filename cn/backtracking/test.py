def permutations("abc"):
    if len(abc) == 1:  # because its 3

    perms = permutations(bc)  # abc

    def permutations(bc):
        if len(bc) == 1  # because its 2

        perms = permutations(c)  # answer is c
        # def permutations(c):
        #     if len(c) == 1: #true
        #         return [c]

        char = word[0]  # b

        result = []

        for perm in perms:  # for perm in c # perm=c
            for i in range(len(perm)+1):  # for i in range(len(c)+1) // range(2) i=0,1

                # i=0
                result.append(perm[:i]+char+perm[i:])

                # [] + ( [] + b + [c] )
                # [bc]

                # i=1
                # result.append(perm[:1]+char+perm[1:])
                # [[bc]] + ( [c] + b +  [] )
                # [ [bc] [cb] ]

        return result
