
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
  
    return stack.pop()

stack=create_stack()
push(stack,str(6))
push(stack,str(5))
pop(stack)
print(stack)


class Queue:
  def __init__(self):
    self.queue=[]
    print("Queue is created 🎉")
    
  def enqueue(self,item):
    self.queue.append(item)

  def dqueue(self):
    if(len(self.queue)<1):
      return None
    return self.queue.pop(0)
    
  def display(self):
    print(self.queue)

tom = Queue()
tom.enqueue(5)
tom.enqueue(6)
tom.enqueue(8)
tom.enqueue(9)
tom.display()
tom.dqueue()
tom.display()



# class Node:
#   def __init__(self,data=None,next=None):
#     self.data=data
#     self.next=next

# class LL():
#   def __init__(self):
#     self.head=None
#     print("linked list created, lol")

#   def printlist(self):
#     temp=self.head
#     while(temp):
#       print(temp.data)
#       temp=temp.next

#   def push(self, new_data):
#     new_node = Node(new_data)
#     new_node.next=self.head
#     self.head=new_node
  
#   def insertAfter(self,prev_node, new_data):
#     if prev_node is None:
#       print "The given previous node must be in linked list"
#       return
#     new_node = Node(new_data)

#     new_node.next = prev_node.next
#     prev_node.next = new_node


#   def append(self,new_data):
#     last=self.head
#     if self.head is None:
#       self.head=new_node
#       return
      
#     while(last):
#       last=last.next
#     last
#     new_node=Node(new_data)
#     last.next=new_node
  
#   def delNode(self, pos):
#     cur_node= self.head
#     prev=None
#     count=0
#     while cur_node and count != pos:
#       prev=cur_node
#       cur_node=cur_node.next
#       count += 1

#     if cur_node is None:
#       return
#     prev.next = cur_node.next
#     cur_node = None
    

# cat = LL()
# cat.push(4)
# cat.push(5)
# cat.push(6)
# cat.printlist()

import recur