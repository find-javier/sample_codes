# this is an example of a linear search, in this case we are searching for Gold

#dataset
import csv
with open("../../periodicTable.csv", "r") as infile:
    data = csv.reader(infile)
    table = [row for row in data]

#handle searching
def linearsearch(term):
    for row in table:
        if row[1] == term:
            return row
    return "Not Found"

print(linearsearch("Gold"))
print(linearsearch("Adamantite"))
