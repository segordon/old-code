import random
import time

def displayIntro():
    print("You are in a land full of dragons.")
    print("In front of you, you see two caves.")
    print("In one cave is a friendly dragon who will share his treasures with you.")
    print("In the other cave is a greedy, hungry dragon, who would surely eat you.")
    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave would you like to enter? (1 or 2)")
        cave = input()

    return cave

def checkCave(chosenCave):
    print("You approach the cave..")
    time.sleep(2)
    print("It is dark and spooky..")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws, and..")
    print()
    time.sleep(2)
    
    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print("Gives you half of his treassure!")
    else:
        print("Gobbles you down in one deft bite.")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":

    displayIntro()

    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you  want to play again? (yes or no)")
    playAgain = input()