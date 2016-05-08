#!/usr/bin/python

# Open a file
sum = 0;
fo = open("numbers.txt", "r+")
for line in fo:
    sum = sum + int(line)
    
print sum
