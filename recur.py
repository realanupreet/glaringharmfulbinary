print("\n\n\n\n from recursion file\n\n\nHello world")

# factorial
def fact(n):
  if n==0:
    return 1
  return n * fact(n-1)

# sum of n natural numbers
def sum_n(n):
  if n==0:
    return 0
  return n + sum_n(n-1)
n=5
#print 1 to n

# print(fact(n))
print(sum_n(n))


