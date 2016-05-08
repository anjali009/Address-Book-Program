#!/usr/bin/python

# Open a file
count = 0 
a='a'
#fo = open("printfile.txt", "r+")
#for line in fo:
#	new=line.split();
if 'a' in open('printfile.txt').read():
		count = count+1
print count
