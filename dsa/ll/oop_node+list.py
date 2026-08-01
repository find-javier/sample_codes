# this is a linked list imple with a Node and Linked List class

class Node:
    def __init__(self, data):
        self.val = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        return


    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return

    def delete(self, val): #by value
        if not self.head or self.head.val == val:
            self.head = None
            return 
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
            if curr.val == val:
                if curr.next:
                    prev.next = curr.next #skip the node
                else:
                    prev.next = None
        return

    def search(self, val): #val is the search term
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def to_list(self):
        curr = self.head
        builder = []
        while curr:
            builder.append(curr.val)
            curr = curr.next
        return builder
            
if __name__ == "__main__":
    def checker():
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.prepend(0)

        assert ll.to_list() == [0, 1, 2, 3]
        assert ll.search(2) ==  True
        ll.delete(2)
        assert ll.to_list() == [0, 1, 3]

        print("all good")
