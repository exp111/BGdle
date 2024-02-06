import csv

result = {4:[],5:[],6:[]}
with open("boardgames_ranks.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    first = True
    for row in reader:
        if first:
            first = False
            continue
        name = row[1]
        rank = int(row[3])
        length = len(name)
        if (length in result and rank > 0 and rank <= 1000):
            result[length].append(name)
print(result)
for i in result:
    print(i)
    print(len(result[i]))