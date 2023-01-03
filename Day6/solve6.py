totalpt1 = 0
totalpt2 = ""
sequence = ''

with open('Day6/data6.txt') as f:
    string = f.readlines()
    for i in  range(len(string[0])):
        sequence = string[0][1+i:5+i]
        if (len(set(sequence)) == len(sequence)) and (len(sequence) == 4) :
            totalpt1 = totalpt1 + (i + 5)
            print(sequence)


print(f"Answer pt.1 :{totalpt1}\nAnswer pt.2 :{totalpt2}")