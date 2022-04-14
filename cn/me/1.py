class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LL():
    def __init__(self):
        self.head =None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def push(self,newd):
        newnode = Node(newd)
        newnode.next = self.head
        self.head=newnode