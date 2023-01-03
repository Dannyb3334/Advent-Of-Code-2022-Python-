with open('Day2/data2.txt') as f:
    raw = f.readlines()
#Pt.1
cpu = []
player = []
rock = 'AX'
paper = 'BY'
scissors = 'CZ'
score = 0 
for data in raw:
    cpu.append(data[0])
    player.append(data[2])

for x in range(len(cpu)):
    c=cpu[x]
    p=player[x]
    if c in rock:
        if p in rock:
            #draw
            score = score + 4
        if p in scissors:
            #lose
            score = score + 3
        if p in paper:
            #win
            score = score + 8
    if c in paper:
        if p in paper:
            #draw
            score = score + 5
        if p in rock:
            #lose
            score = score + 1
        if p in scissors:
            #win
            score = score + 9
    if c in scissors:
        if p in scissors:
            #draw
            score = score + 6
        if p in paper:
            #lose
            score = score + 2
        if p in rock:
            #win
            score = score + 7
print(f"Answer pt.1 :{score}")
#Pt.2
cpu = []
outcome = []
rock = 'A'
paper = 'B'
scissors = 'C'
lose = 'X'
draw = 'Y'
win = 'Z'
score = 0 
for data in raw:
    cpu.append(data[0])
    outcome.append(data[2])
for x in range(len(cpu)):
    c=cpu[x]
    o=outcome[x]
    if c == rock:
        if o == draw:
            #draw
            score = score + 4
        if o == lose:
            #lose
            score = score + 3
        if o == win:
            #win
            score = score + 8
    if c == paper:
        if o == draw:
            #draw
            score = score + 5
        if o == lose:
            #lose
            score = score + 1
        if o == win:
            #win
            score = score + 9
    if c == scissors:
        if o == draw:
            #draw
            score = score + 6
        if o == lose:
            #lose
            score = score + 2
        if o == win:
            #win
            score = score + 7
print(f"Answer pt.2 :{score}")
        
