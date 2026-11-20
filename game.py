"""
THE LAST ONE STANDING
In a haunted house
1. Ask how many players (2-4) and how many rounds they want to play
2. Ask the player's names
3. Ask what room they want to go in out of 3 rooms
4. If there is a gem in that room, you get +1 heart
5. If there is a creaky floor, you get nothing
"""
#This imports the library for random and I can call it whenever I want
import random

# Introduction
print("Welcome to the Last One Standing!")
print("You decided to come into a haunted house with your friends.")
print("You will choose a door and when you open that door, there will be candy, a ghost or nothing.")
print("If you get a ghost, the ghost will take one of your candies away.")
print("And if you get nothing, nothing will happen to your candy.")
print("The first one to 3 pieces of candy WINS!!!")
#This tells the code that I want these variables, and I have to start them off at zero
point1 = 0
point2 = 0
point3 = 0
point4 = 0
#I am asking how many 
players = input("How many players (2-4): ")

if players == "2":
    name1 = input("Enter player 1's name: ")
    name2 = input("Enter player 2's name: ")
    items = ["candy", "candy", "candy", "ghost", "nothing"]

    while point1 < 3 and point2 < 3:
        random.shuffle(items)
        while True:
            pick_door = input(f"{name1}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items[0]
                break
            elif pick_door == "middle":
                chosen = items[1]
                break
            elif pick_door == "right":
                chosen = items[2]
                break
            else:
                print("Invalid door choice, please try again.")

        print(f"You found: {chosen}")
        if chosen == "candy":
            point1 = point1 + 1
            print(f"points for {name1}: {point1}")
        elif chosen == "ghost":
            point1 = point1 - 1
            print(f"points for {name1}: {point1}")
        else:
            print("Nothing happens!")
            print(f"points for {name1}: {point1}")

        if point1 >= 3 or point2 >= 3:
            print("CONGRATULATIONS!")
            break

        random.shuffle(items)
        while True:
            pick_door = input(f"{name2}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items[0]
                break
            elif pick_door == "middle":
                chosen = items[1]
                break
            elif pick_door == "right":
                chosen = items[2]
                break
            else:
                print("Invalid door choice, please try again.")

        print(f"You found: {chosen}")
        if chosen == "candy":
            point2 = point2 + 1
            print(f"points for {name2}: {point2}")
        elif chosen == "ghost":
            point2 = point2 - 1
            print(f"points for {name2}: {point2}")
        else:
            print("Nothing happens!")
            print(f"points for {name2}: {point2}")

elif players == "3":
    name1 = input("Enter player 1's name: ")
    name2 = input("Enter player 2's name: ")
    name3 = input("Enter player 3's name: ")
    items = ["candy", "candy", "candy", "ghost", "nothing"]

    while point1 < 3 and point2 < 3 and point3 < 3:
        random.shuffle(items)
        while True:
            pick_door = input(f"{name1}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items[0]
                break
            elif pick_door == "middle":
                chosen = items[1]
                break
            elif pick_door == "right":
                chosen = items[2]
                break
            else:
                print("Invalid door choice, please try again.")

        print(f"You found: {chosen}")
        if chosen == "candy":
            point1 = point1 + 1
            print(f"points for {name1}: {point1}")
        elif chosen == "ghost":
            point1 = point1 - 1
            print(f"points for {name1}: {point1}")
        else:
            print("Nothing happens!")
            print(f"points for {name1}: {point1}")

        if point1 >= 3 or point2 >= 3 or point3 >= 3:
            break

        random.shuffle(items)
        while True:
            pick_door = input(f"{name2}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items[0]
                break
            elif pick_door == "middle":
                chosen = items[1]
                break
            elif pick_door == "right":
                chosen = items[2]
                break
            else:
                print("Invalid door choice, please try again.")

        print(f"You found: {chosen}")
        if chosen == "candy":
            point2 = point2 + 1
            print(f"points for {name2}: {point2}")
        elif chosen == "ghost":
            point2 = point2 - 1
            print(f"points for {name2}: {point2}")
        else:
            print("Nothing happens!")
            print(f"points for {name2}: {point2}")

        if point1 >= 3 or point2 >= 3 or point3 >= 3:
            break

        random.shuffle(items)
        while True:
            pick_door = input(f"{name3}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items[0]
                break
            elif pick_door == "middle":
                chosen = items[1]
                break
            elif pick_door == "right":
                chosen = items[2]
                break
            else:
                print("Invalid door choice, please try again.")

        print(f"You found: {chosen}")
        if chosen == "candy":
            point3 = point3 + 1
            print(f"points for {name3}: {point3}")
        elif chosen == "ghost":
            point3 = point3 - 1
            print(f"points for {name3}: {point3}")
        else:
            print("Nothing happens!")
            print(f"points for {name3}: {point3}")

elif players == "4":
    name1 = input("Enter player 1's name: ")
    name2 = input("Enter player 2's name: ")
    name3 = input("Enter player 3's name: ")
    name4 = input("Enter player 4's name: ")
    items = ["candy", "candy", "candy", "ghost", "nothing"]

    while point1 < 3 and point2 < 3 and point3 < 3:
        random.shuffle(items)
        while True:
            pick_door = input(f"{name1}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items[0]
                break
            elif pick_door == "middle":
                chosen = items[1]
                break
            elif pick_door == "right":
                chosen = items[2]
                break
            else:
                print("Invalid door choice, please try again.")

        print(f"You found: {chosen}")
        if chosen == "candy":
            point1 = point1 + 1
            print(f"points for {name1}: {point1}")
        elif chosen == "ghost":
            point1 = point1 - 1
            print(f"points for {name1}: {point1}")
        else:
            print("Nothing happens!")
            print(f"points for {name1}: {point1}")

        if point1 >= 3 or point2 >= 3 or point3 >= 3:
            break

        random.shuffle(items)
        while True:
            pick_door = input(f"{name2}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items[0]
                break
            elif pick_door == "middle":
                chosen = items[1]
                break
            elif pick_door == "right":
                chosen = items[2]
                break
            else:
                print("Invalid door choice, please try again.")

        print(f"You found: {chosen}")
        if chosen == "candy":
            point2 = point2 + 1
            print(f"points for {name2}: {point2}")
        elif chosen == "ghost":
            point2 = point2 - 1
            print(f"points for {name2}: {point2}")
        else:
            print("Nothing happens!")
            print(f"points for {name2}: {point2}")

        if point1 >= 3 or point2 >= 3 or point3 >= 3:
            break

        random.shuffle(items)
        while True:
            pick_door = input(f"{name3}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items[0]
                break
            elif pick_door == "middle":
                chosen = items[1]
                break
            elif pick_door == "right":
                chosen = items[2]
                break
            else:
                print("Invalid door choice, please try again.")

        print(f"You found: {chosen}")
        if chosen == "candy":
            point3 = point3 + 1
            print(f"points for {name3}: {point3}")
        elif chosen == "ghost":
            point3 = point3 - 1
            print(f"points for {name3}: {point3}")
        else:
            print("Nothing happens!")
            print(f"points for {name3}: {point3}")

        random.shuffle(items)
        while True:
            pick_door = input(f"{name3}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items[0]
                break
            elif pick_door == "middle":
                chosen = items[1]
                break
            elif pick_door == "right":
                chosen = items[2]
                break
            else:
                print("Invalid door choice, please try again.")

        print(f"You found: {chosen}")
        if chosen == "candy":
            point3 = point4 + 1
            print(f"points for {name4}: {point4}")
        elif chosen == "ghost":
            point3 = point4 - 1
            print(f"points for {name4}: {point4}")
        else:
            print("Nothing happens!")
            print(f"points for {name4}: {point4}")
else:
    print("Invalid input, please enter a number from 2-4")
