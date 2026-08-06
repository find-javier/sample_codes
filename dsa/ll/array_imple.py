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
    if head == -1:
        return "nothing to do"
    old_head = head
    head = nxt[head]
    nxt[old_head], data[old_head], freeHead = freeHead, None, old_head
    return

def pop_back():
    global capacity, data, nxt, head, freeHead
    if head == -1:
        return "nothing to do"
    if nxt[head] == -1:
        curr = head
        head = -1
    else:
        prev = head
        curr = nxt[head]
        while nxt[curr] != -1:
            prev = curr
            curr = nxt[curr]
        nxt[prev] = -1
    nxt[curr], data[curr], freeHead = freeHead, None, curr


capacity = 6 # slots
data = [None for _ in range(capacity)] # this is the ACTUAL LINKED LIST
nxt = [i+1 for i in range(capacity)] # this is a FREE SPACE LIST
nxt[capacity - 1] = -1 # chain nothing after this point (sentinel value)
head = -1 # head of the REAL linked list
freeHead = 0 # head of the FREE SPACE linked list

# === helpers to inspect logical state ===
def to_list():
    result = []
    curr = head
    while curr != -1:
        result.append(data[curr])
        curr = nxt[curr]
    return result

def free_count():
    count = 0
    curr = freeHead
    while curr != -1:
        count += 1
        curr = nxt[curr]
    return count

def reset(cap=6):
    global capacity, data, nxt, head, freeHead
    capacity = cap
    data = [None for _ in range(capacity)]
    nxt = [i + 1 for i in range(capacity)]
    nxt[capacity - 1] = -1
    head = -1
    freeHead = 0


#     __          __
#    / /____ ___ / /________ ____ ___ ___
#   / __/ -_|_-</ __/ __/ _ `(_-</ -_|_-<
#   \__/\__/___/\__/\__/\_,_/___/\__/___/

# === 1. Empty list ===
reset()
assert to_list() == []
assert free_count() == 6
assert isfull() == False
assert head == -1


# === 2. Append ===
reset()
append(10)
assert to_list() == [10]
assert free_count() == 5

append(20)
append(30)
assert to_list() == [10, 20, 30]
assert free_count() == 3


# === 3. Prepend ===
prepend(5)
assert to_list() == [5, 10, 20, 30]
assert free_count() == 2


# === 4. Delete (middle, head, tail, only-node, missing) ===
delete(20)                     # delete middle
assert to_list() == [5, 10, 30]
assert free_count() == 3

delete(5)                      # delete head
assert to_list() == [10, 30]
assert free_count() == 4

delete(30)                     # delete tail
assert to_list() == [10]
assert free_count() == 5

delete(10)                     # delete only node
assert to_list() == []
assert head == -1
assert free_count() == 6

assert delete(999) == "nothing to do"   # missing item


# === 5. Pop back ===
reset()
append(100)
append(200)
append(300)
assert to_list() == [100, 200, 300]

pop_back()
assert to_list() == [100, 200]
pop_back()
assert to_list() == [100]
pop_back()
assert to_list() == []
assert head == -1
assert free_count() == 6

assert pop_back() == "nothing to do"    # empty list


# === 6. Pop front  (NOTE: your current pop_front has a bug:
#      it reads nxt[freeHead] instead of nxt[head], and it never
#      returns the popped node to the free list. Uncomment below
#      after fixing those two issues.) ===
reset()
append(1)
append(2)
append(3)
assert to_list() == [1, 2, 3]

pop_front()
assert to_list() == [2, 3]
assert free_count() == 4

pop_front()
assert to_list() == [3]
assert free_count() == 5

pop_front()
assert to_list() == []
assert head == -1
assert free_count() == 6

assert pop_front() == "nothing to do"   # empty list


# === 7. isfull / overflow ===
reset(3)
assert isfull() == False
append(1)
append(2)
append(3)
assert isfull() == True
assert append(4) == "nothing to do"
assert prepend(0) == "nothing to do"


# === 8. Mixed sequence ===
reset(5)
append(10)          # [10]
append(20)          # [10, 20]
prepend(5)          # [5, 10, 20]
delete(10)          # [5, 20]
append(30)          # [5, 20, 30]
append(40)          # [5, 20, 30, 40]
assert to_list() == [5, 20, 30, 40]
assert free_count() == 1

pop_back()          # [5, 20, 30]
delete(5)           # [20, 30]
prepend(15)         # [15, 20, 30]
assert to_list() == [15, 20, 30]
assert free_count() == 2

print("all testcases passed :)")
