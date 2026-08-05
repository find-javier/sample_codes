# assume bst = [[left, root, right], ...]
# bst should be a 2d array
def insert(val):
    global bst
    if not bst:
        bst.append([-1, val, -1])
        return
    # handle traversal
    curr_index = 0
    curr = bst[0]
    while True:
        if val < curr[1]:
            if curr[0] == -1:
                bst.append([-1, val, -1])
                curr[0] = len(bst)-1
            curr_index = curr[0]
            curr = bst[curr_index]
        elif val > curr[1]:
            if curr[2] == -1:
                bst.append([-1, val, -1])
                curr[2] = len(bst)-1
            curr_index = curr[2]
            curr = bst[curr_index]
        else:
            return

def preorder(node):
    global bst
    if not bst:
        print("die")
        return
    else:
        print(node[1])
        if node[0] != -1:
            preorder(bst[node[0]])
        if node[2] != -1:
            preorder(bst[node[2]])


def inorder(node):
    global bst
    if not bst:
        print("die")
        return
    else:
        if node[0] != -1:
            inorder(bst[node[0]])
        print(node[1])
        if node[2] != -1:
            inorder(bst[node[2]])


def postorder(node):
    global bst
    if not bst:
        print("die")
        return
    else:
        if node[0] != -1:
            postorder(bst[node[0]])
        if node[2] != -1:
            postorder(bst[node[2]])
        print(node[1])



def collect_inorder(node):
    result = []
    if node[0] != -1:
        result += collect_inorder(bst[node[0]])
    result.append(node[1])
    if node[2] != -1:
        result += collect_inorder(bst[node[2]])
    return result

def collect_preorder(node):
    result = [node[1]]
    if node[0] != -1:
        result += collect_preorder(bst[node[0]])
    if node[2] != -1:
        result += collect_preorder(bst[node[2]])
    return result

def build_tree(values):
    global bst
    bst = []
    for v in values:
        insert(v)
    return bst

# test 1: basic structure
build_tree(["1", "2", "5", "4", "3"])
assert bst[0] == [-1, "1", 1]
assert bst[1][1] == "2"

# test 2: preorder order
build_tree(["1", "2", "5", "4", "3"])
assert collect_preorder(bst[0]) == ["1", "2", "5", "4", "3"]

# test 3: inorder gives sorted order
build_tree(["5", "3", "8", "1", "4", "7", "9"])
assert collect_inorder(bst[0]) == ["1", "3", "4", "5", "7", "8", "9"]

# test 4: duplicate insert is a no-op
build_tree(["5", "3", "8"])
size_before = len(bst)
insert("5")
assert len(bst) == size_before

print("all tests passed")
