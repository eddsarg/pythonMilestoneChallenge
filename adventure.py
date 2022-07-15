import time

def game():
    print(f"Starting the game...")
    time.sleep(2)
    sysadminName = input("What is your name? ")
    time.sleep(2)
    print(f"Welcome to the game, {sysadminName}")
    print(f"You are starting off another day at \"Everything is Broken Corp\" where everything is...")
    time.sleep(3)
    wellBroken = "well... broken..."
    wellBroken = wellBroken.split()
    for word in wellBroken:
        print(word)
        time.sleep(3)

    print(f"You will be given a series of decisions to make that can impact your job and others around you.")
    time.sleep(3)
    print("Some decisions will end your game quicker than others. See if you can make it back home without destroying the company!")
    time.sleep(5)



print()
print()
time.sleep(2)
print(f"    ##############################")
time.sleep(2)
print(f"    Welcome to Sysadmin simulator!")
time.sleep(2)
print(f"    ##############################")
time.sleep(2)
print()
print()

loop = True
while loop is True:
    start = input(f"Start the game? y/yes/n/no: ")
    start = start.lower()
    if start == "n" or start == "no":
        print()
        print("Goodbye :(")
        print()
        break
    elif start == "y" or start == "yes":
        print()
        game()
        loop = 2
    else:
        print()
        print(f"Please enter \"y\" or \"n\" or \"no\" or \"yes\"")
        print()
