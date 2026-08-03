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
            if curr[1] == -1:
                bst.append([-1, val, -1])
                curr[2] = len(bst)-1
            curr_index = curr[2]
            curr = bst[curr_index]
        else:
            return

def preorder():
    #clearly broken btw
    global bst
    for i in bst:
        print (i)


#init bst
bst = []
root = 0

insert("1")
insert("2")
insert("5")
insert("4")
insert("3")

preorder()
