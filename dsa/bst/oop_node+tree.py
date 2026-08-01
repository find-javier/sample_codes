#this is a binary search tree implemented with a Node and BST class

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.left , self.right = None, None

    def preorder(self):
        result = [self.data]
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result


    def inorder(self):
        result = [self.data]
        if self.left:
            result = self.left.inorder() + result
        if self.right:
            result += self.right.inorder()
        return result

    def postorder(self):
        result = [self.data]
        if self.left:
            result = self.left.postorder() + result
        if self.right:
            result = self.right.postorder() + result
        return result



class BST:
    def __init__(self):
        self.head = None

    def insert(self, newData): #this method feels wrong
        if self.head is not None:
            parent = None
            curr = self.head
            while curr:
                parent = curr
                if curr.data > newData:
                    curr = curr.left
                else:
                    curr = curr.right
            if parent.data > newData:
                parent.left = Node(newData)
            else:
                parent.right = Node(newData)
            return
        self.head = Node(newData)
        return

    def preorder(self):
        if self.head:
            return self.head.preorder()
        return []

    def inorder(self):
        if self.head:
            return self.head.inorder()
        return []

    def postorder(self):
        if self.head:
            return self.head.postorder()
        return []


#main
staff = ['PHILIP', 'CHARLES', 'ANNE', 'ANDREW', 'EDWARD', 'JOHN', 'PETER', 'JAMES', 'HENRY', 'ALEX']

tree = BST()
for name in staff:
  tree.insert(name)

print("PreOrder:")
print(tree.preorder())
print()
print()

print("InOrder:")
print(tree.inorder())
print()
print()

print("PostOrder:")
print(tree.postorder())
