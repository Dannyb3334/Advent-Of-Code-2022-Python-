totalpt1 = ""
totalpt2 = ""
row = []
steps = []
with open('Day5/data5.txt') as f:
    raw = f.readlines()
with open('Day5/data5pt2.txt') as f:
    instructions = f.readlines()
#Pt 1
for line in raw:
    line = line.rstrip('\n')
    crates = []
    while line:
        crates.append(line[:4])
        line = line[4:]
    row.append(crates)
columns = [[row[j][i] for j in range(len(row))] for i in range(len(row[0]))]
for x in range(len(columns)):
    columns[x].reverse()
del columns[1][len(columns[1]) - 5:]
del columns[2][len(columns[2]) - 4:]
del columns[3][len(columns[3]) - 1:]
del columns[4][len(columns[4]) - 2:]
del columns[7][len(columns[7]) - 1:]
del columns[8][len(columns[8]) - 3:]

for line in instructions:
    line = line.rstrip('\n').split(' ')
    _qty = (int)(line[1]) * -1
    _from = (int)(line[3]) - 1
    _to = (int)(line[5]) - 1
    take = columns[_from][_qty:]
    
    take.reverse()
    columns[_from] = columns[_from][:_qty]
    for item in take:
        columns[_to].append(item)
for i in columns:
    totalpt1 = totalpt1 + i[-1]
    
#Pt 2
columns = [[row[j][i] for j in range(len(row))] for i in range(len(row[0]))]
for line in instructions:
    line = line.rstrip('\n').split(' ')
    _qty = (int)(line[1]) * -1
    _from = (int)(line[3]) - 1
    _to = (int)(line[5]) - 1
    take = columns[_from][_qty:]
    
    columns[_from] = columns[_from][:_qty]
    for item in take:
        columns[_to].append(item)
    
for i in columns:
    totalpt2 = totalpt2 + i[-1]

print(f"Answer pt.1 :{totalpt1}\nAnswer pt.2 :{totalpt2}")