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
        result = []
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result.append(self.data)
        return result



class BST:
    def __init__(self):
        self.head = None

    def insert(self, newData):
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


# === helper to build trees quickly ===
def build_tree(values):
    """Insert values in given order and return the BST."""
    bst = BST()
    for v in values:
        bst.insert(v)
    return bst


# === 1. Empty tree ===
t = BST()
assert t.preorder() == []
assert t.inorder() == []
assert t.postorder() == []
assert t.head is None


# === 2. Single node ===
t = build_tree([42])
assert t.preorder() == [42]
assert t.inorder() == [42]
assert t.postorder() == [42]
assert t.head.data == 42
assert t.head.left is None
assert t.head.right is None


# === 3. Left-skewed tree (descending insertions) ===
t = build_tree([30, 20, 10])
assert t.preorder() == [30, 20, 10]
assert t.inorder() == [10, 20, 30]
assert t.postorder() == [10, 20, 30]


# === 4. Right-skewed tree (ascending insertions) ===
t = build_tree([10, 20, 30])
assert t.preorder() == [10, 20, 30]
assert t.inorder() == [10, 20, 30]
assert t.postorder() == [30, 20, 10]


# === 5. Balanced small tree ===
t = build_tree([20, 10, 30])
assert t.preorder() == [20, 10, 30]
assert t.inorder() == [10, 20, 30]
assert t.postorder() == [10, 30, 20]


# === 6. Complex tree (multiple levels, mixed insertions) ===
#            50
#          /    \
#        30      70
#       /  \    /  \
#     20   40  60   80
t = build_tree([50, 30, 70, 20, 40, 60, 80])
assert t.preorder() == [50, 30, 20, 40, 70, 60, 80]
assert t.inorder() == [20, 30, 40, 50, 60, 70, 80]
assert t.postorder() == [20, 40, 30, 60, 80, 70, 50]


# === 7. Duplicates (goes right per your logic: curr.data <= newData) ===
t = build_tree([10, 10, 10])
assert t.preorder() == [10, 10, 10]
assert t.inorder() == [10, 10, 10]
assert t.postorder() == [10, 10, 10]


# === 8. Larger mixed sequence ===
t = build_tree([25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90])
assert t.preorder() == [25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]
assert t.inorder() == [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90]
assert t.postorder() == [4, 12, 10, 18, 24, 22, 15, 31, 44, 35, 66, 90, 70, 50, 25]


# === 9. Verify BST property via inorder (must be sorted) ===
import random
random.seed(0)
values = list(range(100))
random.shuffle(values)
t = build_tree(values)
assert t.inorder() == list(range(100))


# === 10. Verify structure: parent/child links ===
t = build_tree([50, 30, 70, 20])
assert t.head.data == 50
assert t.head.left.data == 30
assert t.head.right.data == 70
assert t.head.left.left.data == 20
assert t.head.left.right is None
assert t.head.right.left is None
assert t.head.right.right is None

print("all test passed :)")
