# // DSA with python //

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
 
## 2-d arrays
- stores in 2 dimensions
- eg ```[[1,3,5],[6,7,9],[8,4,7]]```
- 