# this is the implementation of a stack and circular queue statically

# if you would like the classless implementation of this
# (say to make python an actually good language)
# then create a stack with a for loop, and do operations on it


class stack():
    def __init__(self, size):
        self.data = [None for _ in range(size)]
        self.size = size
        self.top = 0

    def push(self, data):
        if self.top >= self.size:
            return "full"
        self.data[self.top] = data
        self.top += 1
        return

    def pop(self):
        if self.top <= 0:
            return "empty"
        self.top -= 1
        ret = self.data[self.top]
        self.data[self.top] = None
        return f"popped {ret}"

    def search(self, search_term):
        ptr = 0
        while ptr < self.top:
            if self.data[ptr] == search_term:
                return True
            ptr += 1
        return False

    def display(self):
        return self.data

class circularqueue:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.front = -1
        self.back = -1
        self.length = 0

    def check_full(self):
        # size check
        size_flag = False 
        if self.length == self.size:
            size_flag = True
        
        return size_flag  

    def check_empty(self):
        #size check
        size_flag = False
        if self.length == 0:
            size_flag = True

        #pointer_bullshit
        ptr_flag = False
        if self.front == self.back:
            ptr_flag = True
        if self.front == -1:
            ptr_flag = True

        return size_flag == ptr_flag == True

    def enqueue(self, val):
        if not self.check_full():
            self.back = (self.back + 1) % self.size
            self.data[self.back] = val
            self.length += 1
            return "appended"
        return "full lol"

    def dequeue(self):
        if not self.check_empty():
            self.front = (self.front + 1) % self.size
            ret = self.data[self.front] 
            self.data[self.front] = None
            self.length -=1
            return ret
        return "empty"

    def display(self):
        pointer = self.back
        while pointer < self.front:
            print(self.data[pointer % self.size], end = ", ")
            pointer += 1

    def search(self, target):
        pointer = self.back
        while pointer < self.front:
            if self.data[pointer] == target:
                return True
            pointer += 1
        return False

def test_stack():
    s = stack(3)

    assert s.push(1) is None
    assert s.push(2) is None
    assert s.push(3) is None
    assert s.push(4) == "full"

    assert s.pop() == "popped 3"
    assert s.pop() == "popped 2"
    assert s.pop() == "popped 1"
    assert s.pop() == "empty"

    s.push(5)
    s.push(6)

    assert s.search(5) is True
    assert s.search(99) is False

    print("stack tests passed")

def test_circularqueue():
    q = circularqueue(3)

    assert q.enqueue(1) == "appended"
    assert q.enqueue(2) == "appended"
    assert q.enqueue(3) == "appended"
    assert q.enqueue(4) == "full lol"

    assert q.dequeue() == 1
    assert q.enqueue(4) == "appended"   # wraps around now that there's room
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == "empty"

    print("circular queue tests passed")

test_stack()
test_circularqueue()

            
