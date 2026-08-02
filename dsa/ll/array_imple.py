# Note -> for this implementation we are going to use one 2d list, it is also possible to use two 1d lists/arrays.

def display():
    global capacity, data, nxt, head, freeHead
    if head == -1:
        return "nothing to do"
    curr = head
    while curr != -1:
        print(data[curr])
        curr = nxt[curr]

def isfull():
    global freeHead
    return freeHead == -1

def append(item):
    global head, freeHead

    if isfull():
        return "nothing to do"

    newNode, freeHead = freeHead, nxt[freeHead]
    data[newNode], nxt[newNode] = item, -1

    if head == -1:
        head = newNode
    else:
        cur = head
        while nxt[cur] != -1:
            cur = nxt[cur]
        nxt[cur] = newNode

def prepend(item):
    global capacity, data, nxt, head, freeHead
    if isfull():
        return "nothing to do"
    curr = head
    head = freeHead
    freeHead = nxt[freeHead]
    data[head] = item
    nxt[head] = curr
    return 
    
def delete(item_to_delete):
    global capacity, data, nxt, head, freeHead
    curr = head
    prev = None
    while curr != -1 and data[curr] != item_to_delete:
        prev = curr
        curr = nxt[curr]
    if curr == -1:
        return "nothing to do"
    if prev is None:
        head = nxt[curr]
    else:
        nxt[prev] = nxt[curr]

    nxt[curr], data[curr], freeHead = freeHead, None, curr

def pop_front():
    global capacity, data, nxt, head, freeHead
    #FIX ME
    pass


def pop_back():
    global capacity, data, nxt, head, freeHead
    #FIX ME
    pass


capacity = 6 # slots
data = [None for _ in range(capacity)] # this is the ACTUAL LINKED LIST
nxt = [i+1 for i in range(capacity)] # this is a FREE SPACE LIST
nxt[capacity - 1] = -1 # chain nothing after this point (sentinel value)
head = -1 # head of the REAL linked list
freeHead = 0 # head of the FREE SPACE linked list


