#!/usr/bin/python

# Open a file
sum = 0;
fo = open("splitnum.txt", "r+")
for line in fo:
	new=line.split();
	for i in new:	
		sum = sum + int(i)
    
print sum
