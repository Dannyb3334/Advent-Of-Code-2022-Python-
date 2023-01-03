list = []
sums = []
sum = 0
import numpy as np
with open('Day 1/data1.txt') as f:
    lines = f.readlines()
data = (''.join(str(x) for x in lines)).split("\n\n")
for items in data:
    list.append(items.split("\n"))
for part in list:
    sum = 0
    for num in part:
        sum = sum + int(num)
    sums.append(sum)
#Pt.1
print(max(sums))
#Pt.2
sumsSorted = np.sort(sums)
print((sumsSorted[-3:]))