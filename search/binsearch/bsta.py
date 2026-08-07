# simple implementation of binary search
# we are searching for the 79th element

import csv
table = []
with open("../../periodicTable.csv", "r") as infile:
    cursor = csv.reader(infile)
    for row in cursor:
        table.append(row)

# to make the binsearch easier, we will typecase the first column to ints
# we will also nuke the first row of the csv
table = table[1::]
table = [ [int(row[0])] + row[1::] for row in table]

def binsearch(table, target, start = 0, end = -1):
    if end == -1:
        end = len(table)-1
    mid = (start + end)//2
    if start == end == mid:
        return "nothing found"
    if (x:=table[mid][0]) > target:
        return binsearch(table, target, start, mid)
    elif x < target:
        return binsearch(table, target, mid+1, end)
    else:
        return table[mid]

print(binsearch(table, 79))
print(binsearch(table, 119))

