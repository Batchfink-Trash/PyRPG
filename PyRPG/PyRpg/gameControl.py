def end_game():
    """End the game if player has 0 health"""
    if health < 0:
        print("Oh no! You appear to be REALLY dead! Goodbye")
        exit
    else:
        print("Oh no!  You appear to be dead! Goodbye!")
        exit

def createCharacter():
    gender = input("Gender: ")
    race = input("Race: ")
    name = input("Name: ")
    return list(gender + race + name)

print(createCharacter())
input("")