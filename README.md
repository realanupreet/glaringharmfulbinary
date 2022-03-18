# // DSA with python //
![](https://c.tenor.com/fMUOPRVdSzUAAAAd/python.gif)
doing this course on dsa with python, so thought of making notes and posting them basically so i dont forget :P

## Lists ```[]```
- mutable
- indexing can be done
- not homogenous[not same data structure possible]
- allow duplicates
- eg ```hello=[10,'string',0.3]```
- methods for insertion
  - hello.append([10,38]) //takes an object
  - hello.insert(index,value)
  - hello.extend(91,22) //takes an iterable
- methods for removing
  - hello.pop() //pop the last element
  - hello.clear() //will clear up all elements
  - hello.remove('bye') //remove the element that given
- other useful methods
  - hello.sort() //will sort the string
  - hello.count(10) //will return the no. of happenings of 10
  - hello.index(10) //find index of 10

## Tuple ```()```

- immutabe(means cannot just change the data but can add more if wanted)
- can indexing
- allow duplicates
- collection of python objects
- eg ```tup=(1,2,3,'string')```
- methods for appending
  - use + operator ```tup=(10,20,30) tup=tup+(40,50,60)```
- methods for slicing
  - use colon : for slice ```tup[1:3]```
  - the first index in ```[first:second]``` will come but second index will not
- methods for deletion
  - use del ```del tup```
- other methods
  - ```len(tup)``` for length
  - ```lst=tuple([11,22,33])``` will convert it to a tuple
  - ```tup.count(22)``` will count the no. of instances of 22 in tuple

## Sets ```{}```

- no duplicates allowed
- no indexing
- whole set is mutable
- order of printing will be random
- 2 ways of making sets
  - eg ```days={92,74,204,67}```
  - eg ```times=set([12,34,56,77])```
- for accessing elements
  - ``` for element in days: ```
  - ``` print(element)```
- methods for adding
  - ```times.add(10)``` will add 10
- methods for removing
  - ```times.discard(5)``` will remove 5
- methods for union
  - pipe | will do the union```times | timer```
- method for intersection
  - ampersand & will do the intersection ```times & timer```
- method for comparing
  - ```times <= timer``` will return a boolean value

## Dictionaries ```{ A : 10,}```
- mutable
- key-value pairs
- 2 ways of making dictionary
  - eg ```book={1:'intro',2:'blogs',3:'content',4:'end'}```
  - eg ```okay=dict([(0,2),(1,4)])``` here output would be ```{0:2,1:4}```
- accessing  ```book[2]``` here 2 is the key not the index
- methods for changing and adding key-value pairs
  - ```book[1]='titles'```
  - ```book[5]='sign'```
- methods for deleting
  - ```book.pop(2)``` will pop element at 2 key
  - ```book.clear()``` will remove all elements of the dictionary
- other methods
  - ```book.keys()``` will give out all the keys
  - ```book.values()``` will give out all the values
  - ```book.items()``` will give the items like ```[(1,'intro'),(2,'blogs')]```
 
## 2-d arrays ```[[2,4],[5,6]]```
- stores in 2 dimensions
- uses a list basically
- eg ```array=[[1,3,5],[6,7,9],[8,4,7]]```
- eg of inputing can be:
  ```python

  size=int(input())
  arr=[]
  
  for x in range(size):
    arr.append([
      int(y) for y in input().split()
    ])
  
  print(arr)
  ```
- eg for traversing the 2-d array
```python
arr = [[1,3,5],[6,9,2],[6,8,3]]
for i in arr:
  for j in i:
    print(j,end=" ")
  print()
  
```
- eg deletion can be done by ```del(arr[i][j])```
- array slicing eg ```arr[1:3] #index 1 to 2```
- array length eg ```len(arr) #no. of rows```

## // ```OOPS``` in python

![](https://c.tenor.com/fp6gyOn-A5gAAAAd/oops-alexandria-ocasio-cortez.gif)

- Object oriented programming
- because somehow procedural way isn't cool
- uses classes which have functions
- class has init method
- eg of class made
```python

class Employee:
  def __init__(self,name='harry'):
    self.name = name
  def display(self):
    print("name of employee is", self.name)

first = Employee()
first.display()
```

## // Time ```Complexity```
![](https://c.tenor.com/FOxYFhcMTXIAAAAd/timeless-clock.gif)

- describes the amount of computer time to take to run an algorithm
- uses Big O notation basically
- ```O(1)``` means for any input time taken is same ```fastest```
- ```O(log n)``` means for n input then time is log n ```faster```
- ```O(n)``` time increasing steadily as input size increasing ```normal```
- ```O(n^2)``` time increasing very rapidly for input ```slow```

## Stacks

- uses lifo [ Last in, first out ]
- push for adding data
- pop for removing the top element
- peek for getting value of top element
- for array implimentation time complexity is O(1)
- eg
```python
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
```

## Queue

- based on fifo [ first in, first out ]