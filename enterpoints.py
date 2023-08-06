# Python 3.9.17 64-bit

# A script to enter data points easily into a csv file, for
# my physics EE experiment. Modify for other headers by changing
# the *header* variable.

import csv

# Changeable header and filename variable
HEADER = ["Time"] + ["Metal Temperature"] + ["Outside Temperature"]
FILENAME = "table.csv"

# A list of various words that could stop the program 
stopWords = ["exit", "Exit", "EXIT", "stop", "Stop", "STOP", "no", "No", "NO",
             "arret", "Arret", "ARRET", "不", "nie", "Nie", "NIE", "non", "Non",
             "NON", "halt", "Halt", "HALT", "desist", "Desist", "DESIST", "cease", 
             "Cease", "CEASE", "leave", "Leave", "LEAVE", "finish", "Finish", 
             "FINISH", ""]

writeMode = "w" # If the csv is properly formatted for this 
                # it'll append instead of overwrite to avoid
                # losing data if I cancel

try:
    with open(FILENAME, "r") as table:
        reader = csv.reader(table, delimiter="|",
                            quotechar="|", quoting=csv.QUOTE_MINIMAL)
        
        # idk how to properly just read the first one but this does the trick
        # however it will not work if there's another file with "time" or such
        # with the same first header name
        for column in reader: 
            if (column[0] == HEADER[0]): 
                writeMode = "a"
                print(column[0])
            break
except FileNotFoundError:
    writeMode = "x"
    

with open("table.csv", writeMode, newline="") as table:
    writer = csv.writer(table, delimiter="|",
                           quotechar="|", quoting=csv.QUOTE_MINIMAL)
    if writeMode == "w": 
        writer.writerow(HEADER)

    entryDone = False
    nextRowToWrite = [None] * len(HEADER)

    # Data entry prompts and input
    while entryDone == False:
        i = 0
        for eachValue in nextRowToWrite:
            inputWord = input("Enter the {headerName}: ".format(headerName = HEADER[i]))
            if inputWord in stopWords: 
                entryDone = True
                break
            nextRowToWrite[i] = inputWord
            i += 1
        if entryDone == True: break
        writer.writerow(nextRowToWrite)