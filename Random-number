#Guess My Number:(if-else conditions, loops)
#The computer randomly generates a number. The user inputs a number, and the computer will tell you if you are too high,
#or too low. Then you will get to keep guessing until you guess the number.
#!/usr/bin/python
import random
guess = 0
ran_num = random.randint(0, 100)
while guess<100:
    print "\nGuess a number : "
    guess = input()
    guess=int(guess)
    if guess>ran_num:
        print "Too high!!"
    if guess<ran_num:
        print "Too low!!"
    if guess==ran_num: 
        break

if guess==ran_num:
    print "\nYou guessed right!!"
