totalpt1 = 0
totalpt2 = 0
with open('Day4/data4.txt') as f:
    raw = f.readlines()
#Pt 1
for line in raw:
	pair = line.rstrip().split(',')
	(a, b) = list(map(int, pair[0].split('-')))
	(c, d) = list(map(int, pair[1].split('-')))

	if (a > c) or (a == c and d > b):
		a, b, c, d = c, d, a, b

	if a <= c and b >= d:
		totalpt1 += 1
#Pt 2
for line in raw:
	pair = line.rstrip().split(',')
	(a, b) = list(map(int, pair[0].split('-')))
	(c, d) = list(map(int, pair[1].split('-')))
 
	if (a > c) or (a == c and d > b):
		a, b, c, d = c, d, a, b
  
	if b >= c:
		totalpt2 += 1

print(f"Answer pt.1 :{totalpt1}\nAnswer pt.2 :{totalpt2}")