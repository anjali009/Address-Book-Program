# Find Surface area and Volume

#!/usr/bin/python

print('\n****MENU****')
print('\n1. Area and volume of cube')
print('\n2. Area and volume of sphere')
print('\n3. Area and volume of cyinder')
c = input()
a=0
b=0

if c==1:
    a=int(input("\nEnter the side of the cube: "))
    area = (6*a*a)
    volume = (a*a*a)
    print('\nThe area is: ', area)
    print('\nThe volume is: ', volume)

elif c==2:
    a=int(input("\nEnter the radius of a sphere: "))
    area = (4*3.144*r*r)
    volume = (4/3)*3.144*r*r*r
    print('\nThe area is: ', area)
    print('\nThe volume is: ', volume)

elif c==3:
     a=int(input("\nEnter the radius of a cylinder: "))
     b=int(input("\nEnter the height of a cylinder: "))
     area = 2*3.144*r*h
     volume = 3.144*r*r*h
     print('\nThe area is: ', area)
     print('\nThe volume is: ', volume)

else:
    print("\nYou entered an invalid number!!")
