# // Algorithms //

## Recursion
- based on pmi(principle of mathematical induction)
- task1: prove a small value is true f(0),f(1)
- task2: asssume f(k) is true
- task3: prove f(k+1) is true
- eg
```python
def fact(n):
  if n==0:
    return 1
  return n * fact(n-1)

n=int(input())
print(fact(n))
```