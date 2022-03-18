from array import *
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

# print("Enter the size for the elements of 2d - array: ")
# size=int(input())
# arr=[]

# for x in range(size):
#   arr.append([
#     int(y) for y in input().split()
#   ])

# print(arr)

arr = [[1,3,5],[6,9,2],[6,8,3]]
for i in arr:
  for j in i:
    print(j,end=" ")
  print()

class Employee:
  def __init__(self,name='harry'):
    self.name = name
  def display(self):
    print("name of employee is", self.name)

first = Employee()
first.display()


# stack nowww

def create_stack():
  stack=[]
  return stack

def push(stack,item):
  stack.append(item)
  print("pushed "+item)

def check_empty():
  return len(stack)==0

def pop(stack):
  if(check_empty(stack)):
    return "Stack is empty"
  else:
    return stack.pop()

stack=create_stack()
push(stack,str(6))
push(stack,str(5))
pop(stack)
print(stack)


class Queue:
  def __init__(self):
    self.queue=[]
  def enqueue(self,item):
    self.queue.append(item)
  