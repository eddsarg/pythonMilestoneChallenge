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
    print(f"You wake up")
    time.sleep(5)
    print(f"An incoherent string of text is on your screen and your face is imprinted with the keys from your keyboard")
    time.sleep(5)
    print()
    print(f"Time to get back to work and do these tickets in my queue: ")
    print(f"    ##################################################################################################################################")
    print(f"    #  1. \"We are unable to upload anything to the SFTP servers. This is impacting our customers\"")
    print(f"    #                                                                                     - Scott, business manager")
    print(f"    #")
    print(f"    #  2. \"Multiple users report that sometimes when they come back in to the office, they are unable to connect to the internet\"")
    print(f"    #                                                                                     - Eli, Helpdesk Tech")
    print(f"    #")
    print(f"    #  3. \"The coffee machine is broken\"")
    print(f"    #                            - Matt, accountant")
    print(f"    #")
    print(f"    #  4. \"Call me when you get the chance\"")
    print(f"    #                                - Mike, Admin Assistant")
    print(f"    #")
    print(f"    #  5. \"Go home\"")
    print(f"    ##################################################################################################################################")
    print(f"")
    
    firstChoice = input(f"Select a choice?")


def firstChoice5():
    print(f"You get up and collect your things and book it towards the exit of the building")
    time.sleep(3)
    print(f"All of the people whom you have tickets for try to talk to you as you pick up the pace")
    time.sleep(3)
    print(f"")



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
