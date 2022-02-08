"""
Author: Taylor Brown
This program starts the cell modem troubleshooter
For the purpose of helping customers get their cell modems working again
"""
#global variables
invalid = "invalid response, please try again"
"""list of local variables used in functions
1: firstQuestion
2: secondQuestion
3: select
4: dL
5: cable
6: power
7a: light
7b: color
8a: service
8b: carrier
9: address"""

#function asking about IP address
def q9():
    address = input("Does your cellular account come with a Public Static IP address or a Private Dymanic IP address?\n"
                    "[1] Public Static\n"
                    "[2] Private Dynamic\n"
                    "[3] Unsure\n"
                    "")
    if address == "1":
        print("The end, more to come :)")
    elif address == "2":
        print("The end, more to come :)")
    elif address == "3":
        print("Contact the person in your office who handles your cellular service.")
        print("")
        q9()
    else:
        (invalid)
        print("")
        q9()

#function asking where service was obtained
def q8b():
    carrier = input("Who did you get your service through?\n"
                    "[1] Verizon\n"
                    "[2] AT&T\n"
                    "[3] Campbell Scientific\n"
                    "[4] Another Carrier\n"
                    "")
    if carrier == "1":
        q9()
    elif carrier == "2":
        q9()
    elif carrier == "3":
        q9()
    elif carrier == "4":
        q9()
    else:
        print(invalid)
        print("")
        q8b()

#function asking if modem has cellular service
def q8a():
    service = input("Does your modem already have cellular service? (y/n) ")
    if service == "y":
        q8b()
    elif service == "n":
        print("That's a problem that needs to be remedied. Get some service!")
        print("")
        q8a()
    else:
        print(invalid)
        print("")
        q8a()

#function asking aboutt color of light
def q7b():
    color = input("What is the color of the light?\n"
                  "[1] green\n"
                  "[2] amber\n"
                  "[3] red\n"
                  "")
    if color == "1":
        q8a()
    elif color == "2":
        q8a()
    elif color == "3":
        q8a()
    else:
        print(invalid)
        print("")
        q7b()

#function asking about power light
def q7a():
    light = input("Is the power light as seen below on your datalogger lit? (y/n) ")
    if light == "y":
        q7b()
    elif light == "n":
        print("That may be a problem. Make sure your modem is powered on.")
        print("If you have a CR1000, there won't be a power light.\n"
              "Make sure the datalogger has power and press y to continue.")
        print("")
        q7a()
    else:
        print(invalid)
        print("")
        q7a()

#function asking about power source
def q6():
    power = input("How is your datalogger connected to power?\n"
                  "[1] CS I/O\n"
                  "[2] Power cable or Green power connector going to datalogger's 12V port\n"
                  "[3] SW12 port\n"
                  "[4] modem straight to the battery or charging regulator\n"
                  "[5] other 12V power source\n"
                  "[6] USB only\n"
                  "")
    if power == "1":
        q7a()
    elif power == "2":
        q7a()
    elif power == "3":
        q7a()
    elif power == "4":
        q7a()
    elif power == "5":
        q7a()
    elif power == "6":
        print("Connect your modem to a 12V power source")
        q6()
    else:
        print(invalid)
        print("")
        q6()

#function asking how modem is connected to logger
def q5():
    cable = input("What cable type are you using to connect the modem to your datalogger?\n"
                  "[1] RS232\n"
                  "[2] CS I/O\n"
                  "[3] Ethernet\n"
                  "")
    if cable == "1":
        q6()
    elif cable == "2":
        q6()
    elif cable == "3":
        q6()
    else:
        print(invalid)
        print("")
        q5()

#function asking which datalogger is being used
def q4():
    dL = input("What model datalogger are you connecting to your modem?\n"
               "[1] CR1000\n"
               "[2] CR800\n"
               "[3] CR3000\n"
               "[4] CR1000X\n"
               "[5] CR6\n"
               "[6] CR300/310/350\n"
               "")
    if dL == "1":
        q5()
    elif dL == "2":
        q5()
    elif dL == "3":
        q5()
    elif dL == "4":
        q5()
    elif dL == "5":
        q5()
    elif dL == "6":
        q5()
    else:
        print(invalid)
        print("")
        q4()

#function asking which cellular modem is being used
def q3():
    select = input("Select the cellular modem you are using or new modem you are installing:\n"
                   "[1] CELL2XX\n"
                   "[2] RV50 (X)\n"
                   "[3] CR300-CELL2XX\n"
                   "")
    if select == "1":
        q4()
    elif select == "2":
        q4()
    elif select == "3":
        q4()
    else:
        print(invalid)
        print("")
        q3()

#function asking if using an older modem
def q2():
    secondQuestion = input("Are you replacing an older LS300 or Raven XT cellular modem? (y/n) ")
    if secondQuestion == "y":
        print("Before continuing, verify that you do not have any Serial open instructions\n"
              "in your datalogger program that use the exact same port that your new modem\n"
              "will use. It will break the connection with your new modem.\n"
              "")
        follow = input("Shall we continue? (y/n) ")
        if follow == "y":
            q3()
        elif follow == "n":
            print("I'll wait")
            q2()
        else:
            print(invalid)
            print("")
            q2()
    elif secondQuestion == "n":
        q3()
    else:
        print(invalid)
        print("")
        q2()

#function asking if setup is new or existing
def q1():
    firstQuestion = input("Is your modem setup on a station that was working and then it stopped? Or is it a new setup?\n"
          "[1] working then stopped\n"
          "[2] new setup\n")
    if firstQuestion == "1":
        q2()
    elif firstQuestion == "2":
        q2()
    else:
        print(invalid)
        print("")
        q1()


#main function to introduce the program and call the first question function
def main():
    #logo
    print(r"""

     _________  _____                               _________         _
    |___   ___|| ___ \                             |___   ___|       | | 
        | |    | |_/ / _  __  ___ __    __    __ _ __  | | ___  _____| |__
        | |    | ___ \| |/ _|/ _ \\ \  /  \  / /| '_ \ | || __\/  __/|  _ \
        | |    | |_/ /| |_/   (_)  \ \/ /\ \/ / | | | || || __/| |__ | | | |
        |_|    \____/ |_|    \___/  \__/  \__/  |_| |_||_||___||____\|_| |_|""")
    print("\n****************************************************************")
    print("\n* Copyright of Taylor Brown, 2022                              *")
    print("\n* https://www.tbrowntech.com                                   *")
    print("\n* https://www.youtube.com/channel/UC44aHM1kG8lnqIs9B2SFIzw     *")
    print("\n****************************************************************")

    #opening statement
    print("")
    print("To help you fix your modem connection problem, I need to ask you a few questions:")
    print("")
    q1()

#main function to start running the program
if __name__ == "__main__":
    main()


