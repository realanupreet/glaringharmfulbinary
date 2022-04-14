#trees

class Node():
    def __init__(self,value):
        self.value = value
        self.left=None
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def countnodes(root):
    if root is None:
        return 0
    return (1+countnodes(root.left)+countnodes(root.right))


def height(root):
    if root is None:
        return -1
    lefth=height(root.left)
    righth=height(root.right)
    return (1+max(lefth,righth))


root=Node(1)
root.left=Node(2)
root.right=Node(3)
h=height(root)
print(h)