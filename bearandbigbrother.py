a,b=[int(x) for x in input().split()]
count=0
while a<=b:
    count+=1
    a=a*3
    b=b*2
    
print(count)