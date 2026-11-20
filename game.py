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
print("If you get a candy, you will take the candy.")
print("If you get a ghost, the ghost will take one of your candies away.")
print("And if you get nothing, nothing will happen to your candy.")
print("The first one to 3 pieces of candy WINS!!!\n")

#This tells the code that I want these variables, and I have to start them off at zero
point1 = 0
point2 = 0
point3 = 0
point4 = 0

#I am asking how many players there are
players = input("How many players (2-4): ")

#If there are two players there has to be an entirely different code
if players == "2":
    name1 = input("\nEnter player 1's name: ")
    name2 = input("Enter player 2's name: ")
    items = ["candy", "candy", "candy", "ghost", "nothing"]

    #Making sure the players don't cheat
    while point1 < 3 and point2 < 3:
        random.shuffle(items) #This shows me calling the random function for the items
        while True: #I can pick a door and the item in the door will be random
            pick_door = input(f"\n{name1}:\nPick a door (left, middle or right): ").lower()
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

        #This code tells me if I got another candy, ghost or nothing
        #it also shows me how many points I have
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

        #This checks if anyone won
        if point1 >= 3 or point2 >= 3:
            print(f"\nCONGRATULATIONS {name1}!")
            break

        random.shuffle(items) #This shuffles the items again using the random import
        while True: #Player 2 picks a room
            pick_door = input(f"\n{name2}:\nPick a door (left, middle or right): ").lower()
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

        #This shows what item player 2 found and changes their points
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

        #This checks if anyone won
        if point2 >= 3:
            print(f"\nCONGRATULATIONS {name2}!")

#If there are three players it runs this, because there are three players there has to be a different code
elif players == "3":
    name1 = input("\nEnter player 1's name: ")
    name2 = input("Enter player 2's name: ")
    name3 = input("Enter player 3's name: ")
    items = ["candy", "candy", "candy", "ghost", "nothing"]

    #Making sure the players don't cheat
    while point1 < 3 and point2 < 3 and point3 < 3:
        random.shuffle(items) #This shows me calling the random function for the items
        while True: #Player 1 picks a room
            pick_door = input(f"\n{name1}:\nPick a door (left, middle or right): ").lower()
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

        #This shows what player 1 found and changes their points
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

        #This checks if anyone won
        if point1 >= 3 or point2 >= 3 or point3 >= 3:
            print(f"\nCONGRATULATIONS {name1}!")
            break

        random.shuffle(items) #This shuffles the items
        while True: #Player 2 picks a room
            pick_door = input(f"\n{name2}:\nPick a door (left, middle or right): ").lower()
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

        #This shows what player 2 found and changes their points
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

        #This checks if anyone won
        if point1 >= 3 or point2 >= 3 or point3 >= 3:
            print(f"\nCONGRATULATIONS {name2}!")
            break

        random.shuffle(items) #This shuffles the items 
        while True: #Player 3 picks a room
            pick_door = input(f"\n{name3}:\nPick a door (left, middle or right): ").lower()
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

        #This shows what player 3 found and changes their points
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

        #This checks if anyone won
        if point3 >= 3:
            print(f"\nCONGRATULATIONS {name3}!")

#If there are four players it runs this section because it is different for 4 players
elif players == "4":
    name1 = input("\nEnter player 1's name: ")
    name2 = input("Enter player 2's name: ")
    name3 = input("Enter player 3's name: ")
    name4 = input("Enter player 4's name: ")
    items = ["candy", "candy", "candy", "ghost", "nothing"]

    #Making sure the players don't cheat
    while point1 < 3 and point2 < 3 and point3 < 3 and point4 < 3:
        random.shuffle(items) #This shows me calling the random function for the items
        while True: #Player 1 picks a room
            pick_door = input(f"\n{name1}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items.__getitem__(0)
                break
            elif pick_door == "middle":
                chosen = items.__getitem__(1)
                break
            elif pick_door == "right":
                chosen = items.__getitem__(2)
                break
            else:
                print("Invalid door choice, please try again.")

        #This shows what player 1 found and changes their points
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

        #This checks if anyone won
        if point1 >= 3 or point2 >= 3 or point3 >= 3 or point4 >= 3:
            print(f"\nCONGRATULATIONS {name1}!")
            break

        random.shuffle(items) #This shuffles the items
        while True: #Player 2 picks a room
            pick_door = input(f"\n{name2}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items.__getitem__(0)
                break
            elif pick_door == "middle":
                chosen = items.__getitem__(1)
                break
            elif pick_door == "right":
                chosen = items.__getitem__(2)
                break
            else:
                print("Invalid door choice, please try again.")

        #This shows what player 2 found and changes their points
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

        #This checks if anyone won
        if point1 >= 3 or point2 >= 3 or point3 >= 3 or point4 >= 3:
            print(f"\nCONGRATULATIONS {name2}!")
            break

        random.shuffle(items) #This shuffles the items
        while True: #Player 3 picks a room
            pick_door = input(f"\n{name3}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items.__getitem__(0)
                break
            elif pick_door == "middle":
                chosen = items.__getitem__(1)
                break
            elif pick_door == "right":
                chosen = items.__getitem__(2)
                break
            else:
                print("Invalid door choice, please try again.")

        #This shows what player 3 found and changes their points
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

        #This checks if anyone won
        if point1 >= 3 or point2 >= 3 or point3 >= 3 or point4 >= 3:
            print(f"\nCONGRATULATIONS {name3}!")
            break

        random.shuffle(items) #This shuffles the items
        while True: #Player 4 picks a room
            pick_door = input(f"\n{name4}:\nPick a door (left, middle or right): ").lower()
            if pick_door == "left":
                chosen = items.__getitem__(0)
                break
            elif pick_door == "middle":
                chosen = items.__getitem__(1)
                break
            elif pick_door == "right":
                chosen = items.__getitem__(2)
                break
            else:
                print("Invalid door choice, please try again.")

        #This shows what player 4 found and changes their points
        print(f"You found: {chosen}")
        if chosen == "candy":
            point4 = point4 + 1
            print(f"points for {name4}: {point4}")
        elif chosen == "ghost":
            point4 = point4 - 1
            print(f"points for {name4}: {point4}")
        else:
            print("Nothing happens!")
            print(f"points for {name4}: {point4}")

        #This checks if anyone won
        if point4 >= 3:
            print(f"\nCONGRATULATIONS {name4}!")

#If the user does not type 2, 3, or 4 this runs
else:
    print("\nInvalid input, please enter a number from 2-4")
