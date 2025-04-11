#value = input("please enter a value:  ")

#print("your user input was: " + value)

import sys
import random

print("")

mesg = """
enter ...
1 for rock
2 for paper
3 for scissors:\n\n
"""
rps = ("nothing","rock" ,"paper","sissors")

playerchoice =input(mesg)
player = int(playerchoice)
print(playerchoice)
player = int(playerchoice)


if player< 1 | player > 3:
     sys.exit("you must enter 1,2, or 3. ")

computerchoice =random.choice("123")

computer =int(computerchoice)

print("")
print("You chose " + playerchoice + " " + rps[player] + ".")
print("Python chose " +computerchoice + " " + rps[computer] + ".")
print("")


if player == 1 and computer == 3:
     print("🫡you win!")
elif player == 2 and computer == 1:
     print("🤫you win!")
elif player == 3 and computer == 1:
     print("🫣you win!")
elif player == computer:
     print("🤔Tie game!")
else:
     print("👾python wins")