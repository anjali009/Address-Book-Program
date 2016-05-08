#!/usr/bin/python

# Open a file
sum = 0;
fo = open("columnnum.txt", "r+")
for line in fo:
	new=line.split();
	print new[0]
    
