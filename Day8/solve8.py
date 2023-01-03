#pt.1 only
totalpt1 = 0
totalpt2 = 0
horizontal_view = []
caught = []
with open('Day8/data8.txt') as f:
    for line in f.readlines():
        horizontal_view.append([eval(i) for i in line.rstrip()])

def find_num_visible_trees(direction):
    for line in range(len(direction)):
        min_h = -1
        for tree in range(len(direction[line])):
            height = direction[line][tree]

            if height < -1:
                height = (height + 10)*-1 
                min_h = height
                
            elif height > min_h:
                global  totalpt1
                totalpt1 =  totalpt1 + 1
                direction[line][tree] = (height + 10)*-1 
                min_h = height
            else:
                continue
    direction.reverse()
            #Unsuccessful
find_num_visible_trees(horizontal_view)
find_num_visible_trees(horizontal_view)
vertical_view = ([[horizontal_view[j][i] for j in range(len(horizontal_view))] for i in range(len(horizontal_view[0]))])
find_num_visible_trees(vertical_view)
find_num_visible_trees(vertical_view)

print(f"Answer pt.1 :{totalpt1}\nAnswer pt.2 :{totalpt2}")