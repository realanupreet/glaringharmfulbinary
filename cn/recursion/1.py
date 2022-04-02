#recursion is a function calling itself
from functools import lru_cache

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

a=fact(5)

print( "factoriall through recursion",a)


def add(n):
    if n==0:
        return 0
    return n + add(n-1)

a=add(5)
print(a)









def print_n(n):
    if n==0:
        return 0
    print_n(n-1)
    print(n)
a=print_n(5)
print("----")
def print_n2(n):
    if n==0:
        return 0
    print(n)
    print_n2(n-1)

print_n2(5)








#fibonnaci series
print("----")
@lru_cache
def fibonnaci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
for n in range(1,10):
    print(n,";",fibonnaci(n))