"""stone = 1
paper = -1
scissors = 0"""
import random
computer = random.choice([1,-1,0])

youstr = input("Enter your choice:")
youdict = {"stone":1,"paper":-1,"scissor":0}
revers_dict ={1:"stone", -1:"paper", 0:"scissor"}
you=youdict[youstr]

print(f"you chose :{revers_dict[you]}\ncomputer chose :{revers_dict[computer]}")

if computer == you:
    print("It's a draw")
else:
    if (computer == 1 and you == -1):
        print("You win!!")
    elif (computer == 1 and you == 0):
        print("You loss!")
    elif(computer == -1 and you == 0):
        print("You win!!")
    elif (computer == -1 and you== 1):
        print("You loss!")
    elif(computer == 0 and you == 1):
        print("You win!!")
    elif (computer == 0 and you == -1):
        print("You loss!")
    else:
        print("Somthing is wrong")
    