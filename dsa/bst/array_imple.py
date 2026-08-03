# assume bst = [left, root, right]
# bst should be a 2d array

# THIS FUNCTION IS BROKEN, FIX ME
def insert(val):
    global bst

    if bst[0] == [-1, None, -1]:
        bst[0] = [2, val, 3]
        return

    # handle traversal
    curr = bst[0]
    nxt = -1
    while curr[0] != -1 and curr[2] != -1:
        if val < curr[1]:
            nxt = curr[0]
            curr = bst[curr[0]]
        if val > curr[1]:
            nxt = curr[2]
            curr = bst[curr[2]]
    bst[nxt] = [nxt*2, val, nxt*2+1]
    return


def preorder():
    global bst
    for i in bst:
        print (i)

#init bst
bst = [[-1, None, -1] for _ in range(20)]
root = 0


preorder()
