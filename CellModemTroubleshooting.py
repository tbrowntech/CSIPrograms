"""
Author: Taylor Brown
This program starts the cell modem troubleshooter
For the purpose of helping customers get their cell modems working again
"""
#function to ask which modem is being used
def main():
    print("-----------------------------------")
    modem = input("Which modem are you using?\n"
                  "[1] CELL2XX\n"
                  "[2] CR300-CELL2XX Integrated\n"
                  "[3] Sierra Wireless RV50/RV50x\n ")
    if modem == "1":
        cell2XX()
    elif modem == "2":
        integrated()
    elif modem == "3":
        sierra()
    else:
        print("invalid response, please try again")
        print("")
        main()

#function printing questions used in sierra and cell2xx
def modelQs():
    modelQ = "What model datalogger are you connecting the modem to?"
    portQ = "What port is the modem being connected to?"
    dL = "CR800/850/1000/3000\n" \
         "CR300/310/350\n" \
         "CR1000X/CR6"
    portType = "RS232\n" \
               "CS I/O\n" \
               "Other COM port"
    print(modelQ)
    print(dL)
    print("")
    print(portQ)
    print(portType)
    print("")
    cable = input("Is the cable correct? (y/n) ")
    if cable == "y":
        print("yes")
        print("")
    elif cable == "n":
        print("please connect the correct cable")
        print("")
        modelQs()
    else:
        print("invalid input, please try again")
        print("")
        modelQs()

#function for troubleshooting the CELL2XX series
def cell2XX():
    modelQs()
    #function within cell2xx asking about webpage loading
    def pageLoad():
        print("Does the model CELL2XX webpage load?")
    pageLoad()

#function for integrated modem
def integrated():
    print("integrated")

#function for sierra wireless modems
def sierra():
    modelQs()

#main function to start running the program
if __name__ == "__main__":
    main()


