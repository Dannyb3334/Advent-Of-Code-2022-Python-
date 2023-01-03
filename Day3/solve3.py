import string
parts = []
list = []
totalpt1, totalpt2 = 0, 0
with open('Day3/data3.txt') as f:
    data = f.readlines()
#Pt.1
for line in data:
    parts.append([data[:len(data)//2], data[len(data)//2:-1]])
for part_1,part_2 in parts:
    for letter_1 in part_1:
        if letter_1 in part_2:
            list.append(letter_1)
            break    
for letter in list:
    print(letter)
    totalpt1 = totalpt1 + (string.ascii_letters).index(letter) + 1

#Pt.2
part_1 = []
part_2 = []
list = []
del data[3-1::3]
    
for index, obj in enumerate(data):
    if (index % 2) == 0:
        part_1.append(obj)
    else:
        part_2.append(obj)

for index, obj in enumerate(part_1):
    for letter in obj:
        if letter in part_2[index]:
            list.append(letter)
            break
        
for letter in list:
    totalpt2 = totalpt2 + (string.ascii_letters).index(letter) + 1

print(f"Answer pt.1 :{totalpt1}\nAnswer pt.2 :{totalpt2}")