print("Hello world")
hello=[1,20,'bye',0.5]
print(type(hello))
print(hello)
print(hello[0])
print(hello[:2])
print(hello[-1])

hello.append([10, 40])
print(hello)
hello.insert(0,30)
print(hello)
hello.extend([91,20])
print(hello)

tup=(1,2,4,'tuple')
print(tup)
for element in tup:
  print(element)
tup=tup+(40,50,70)
print(tup)
#candy=input("Hello")
#print(candy)
