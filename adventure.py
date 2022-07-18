import time

global sysadminName

def intro():
    global sysadminName
    print(f"Starting the game...")
    time.sleep(2)
    sysadminName = input("What is your name? ")
    time.sleep(2)
    print(f"Welcome to the game, {sysadminName}")
    time.sleep(1)
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
    game()

def game():
    global sysadminName
    print(f"You wake up")
    time.sleep(5)
    print(f"An incoherent string of text is on your screen and your face is imprinted with the keys from your keyboard")
    time.sleep(5)
    print()
    print(f"\"Time to get back to work and do these tickets in my queue: \"")
    time.sleep(3)
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
    print(f"    #")
    print(f"    #  6. You probably shouldn't do this one but... give it a try and see what happens!")
    print(f"    ##################################################################################################################################")
    print(f"")
    
    firstChoice = input(f"Select a choice: ")
    print("")
    print("")

    if firstChoice == "1":
        firstChoice1()
    elif firstChoice == "2":
        firstChoice2()
    elif firstChoice == "3":
        firstChoice3()
    elif firstChoice == "4":
        firstChoice4()
    elif firstChoice == "5":
        firstChoice5()
    else:
        print(f"You navigate to the root directory of the hypervisor and you try this cool trick that you read on reddit from the subreddit r/linuxmemes")
        time.sleep(3)
        print(f"rm -rf")
        time.sleep(3)
        print(f"The screen turns black. \"Everything is Broken Corp\" is now \"Everything is On Fire Corp\".")
        time.sleep(2)
        print(f"Rewinding this sequence... Try again in: ")
        time.sleep(2)
        print(f"3")
        time.sleep(2)
        print(f"2")
        time.sleep(2)
        print(f"1")
        time.sleep(3)
        game()


def firstChoice5():
    global sysadminName
    print(f"You get up and collect your things and book it towards the exit of the building")
    time.sleep(3)
    print("")
    print(f"All of the people whom you have tickets for try to talk to you as you pick up the pace")
    time.sleep(3)
    print("")
    print("You make it out the building and start power-walking down the street and abruptly stop....")
    time.sleep(2)
    print("")
    print("???????????????????????????????")
    time.sleep(3)
    print("")
    print(f"\"Wait a minute... I own a car\", you think to yourself. You begin walking back and get in the car")
    time.sleep(4)
    print(f"You try to start it but it doesn't work. Then you hear a knock. It's your manager!!!")
    time.sleep(4)
    print(f"")
    print(f"    ##################################################################################################################################")
    print(f"    #  1. Stay very still. They can't see you if you don't move")
    print(f"    #")
    print(f"    #  2. Run")
    print(f"    #")
    print(f"    #  3. Accept your fate and talk to him")
    print(f"    #")
    print(f"    ##################################################################################################################################")
    print(f"")

    firstChoice5Input = input(f"what do you do? ")

    if firstChoice5Input == "1":
        firstChoice5_1()
    elif firstChoice5Input == "2":
        firstChoice5_2
    elif firstChoice5Input == "3":
        firstChoice5_3
    else:
        print("The car explodes. The end.")
        time.sleep(2)
        print("Nice try. We thought that you would try to be a rebel. Choose 1 through 3 please. Try again in:  ")
        time.sleep(3)
        print("3")
        time.sleep(3)
        print("2")
        time.sleep(3)
        print("1")
        time.sleep(3)
        firstChoice5()

def firstChoice5_2():
    global sysadminName
    print(f"You swing the door open and sprint like an Olympian off in to the distance")
    time.sleep(5)
    print("")
    print(f"You finally slow down as the building disappears out of sight")
    print(f"")
    time.sleep(5)
    print(".....")
    print("")
    time.sleep(5)
    print(f"You snap back to reality.")
    time.sleep(3)
    print("What? You didn't think we were actually running, did you? There is a heat wave!")
    time.sleep(5)
    print("Try again in ")


def firstChoice5_1():
    global sysadminName
    print(f"You freeze and remain in a statue like state for several minutes.")
    time.sleep(3)
    print(f"He calls to you, \"{sysadminName}! Hellooooo\". He eventually gives up and goes inside")
    time.sleep(3)
    print(f"Your car finally starts and you go on your merry way.")
    time.sleep(5)
    print("You pass a Whataburger and a McDonald's.")
    print(f"")
    print(f"    ##################################################################################################################################")
    print(f"    #  1. Whataburger")
    print(f"    #")
    print(f"    #  2. McDonald's")
    print(f"    #")
    print(f"    ##################################################################################################################################")
    print(f"")
    firstChoice5_1_input = input(f"What are we eating? ")
    if firstChoice5_1_input == "1":
        print(f"")
        time.sleep(2)
        print(f"You go to the drive thru and order a feast: A 3 chicken strip meal, a honey barbecue chicken strip sandwich on Texas Toast meal, Large onion rings, a large milkshake, a large sweet tea, and a triple bacon whataburger meal")
        print(f"")
        time.sleep(3)
        print(f"You get home quickly (Of course within the speed limit!!!) and you dig in to the feast!")
        time.sleep(3)
        print(f"You pass out in a food coma.")
        time.sleep(3)
        print(f"Your phone buzzes and buzzes and buzzes but you toss it across the room and go back to sleep")
        time.sleep(3)
        print(f"SURPRISE!!!!!!!")
        print(f"Congrats you won the game!")
        print(f"Thank you for playing")
        print(f"Returning to the start sequence")
        pregame()
    elif firstChoice5_1_input == "2":
        print(f"")
        time.sleep(2)
        print(f"You go to the drive thru and order a feast: A 20 piece spicy nugget meal, two McRibs, 3 McDoubles, a large mango smoothie, a big mac, and a large sweet tea, and a quarter pounder")
        print(f"")
        time.sleep(3)
        print(f"You get home quickly (Of course within the speed limit!!!) and you dig in to the feast!")
        time.sleep(3)
        print(f"You pass out in a food coma.")
        time.sleep(3)
        print(f"Your phone buzzes and buzzes and buzzes but you toss it across the room and go back to sleep")
        time.sleep(3)
        print(f"SURPRISE!!!!!!!")
        print(f"Congrats you won the game!")
        print(f"Thank you for playing")
        print(f"Returning to the start sequence")
        pregame()
    else:
        print(f"....")
        time.sleep(5)
        print(f"....")
        time.sleep(5)
        print(f"You wake up")
        time.sleep(5)
        print(f"An incoherent string of text is on your screen and your face is imprinted with the keys from your keyboard")
        time.sleep(5)
        print()
        print(f"\"Time to get back to work and do these tickets in my queue: \"")
        time.sleep(6)
        print(f"....")
        time.sleep(6)
        print(f"Just kidding! We aren't making you start over! But please only select between 1 and 2 for your restaurant")
        time.sleep(3)
        firstChoice5_1()
    
def pregame():
    print("")
    print("")
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
            intro()
            loop = 2
        else:
            print()
            print(f"Please enter \"y\" or \"n\" or \"no\" or \"yes\"")
            print()

pregame()
