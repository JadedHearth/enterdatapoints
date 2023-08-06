""" 
Python 3.9.17 64-bit
Escape characters probably only work on *nix, not tested on Windows.

A script to enter data points easily into a csv file, for
my physics EE experiment. Modify for other headers by changing
the *header* variable.
"""

import csv

# Changeable header and filename variable
HEADER = ["Time"] + ["Metal Temperature"] + ["Outside Temperature"]
FILENAME = "table.csv" 
MUSTBENUMBER = True

class TextColors:
    """
    A list of console printing color escape characters.
    """
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class Cursor:
    """Cursor manipulation escape codes."""
    UP = "\033[1A" # Moves cursor up one line
    CLEAR = "\x1b[2K" # Erases current line.

def longestLengthInList(list):
    """ Returns the int length of longest string in the given list."""
    headerLengths = []
    for headerItem in list:
        headerLengths.append(len(headerItem))
    return int(max(headerLengths))

# A list of various words that could stop the program. Includes blank and newline.
stopWords = ["exit", "Exit", "EXIT", "stop", "Stop", "STOP", "no", "No", "NO",
             "arret", "Arret", "ARRET", "不", "nie", "Nie", "NIE", "non", "Non",
             "NON", "halt", "Halt", "HALT", "desist", "Desist", "DESIST", "cease", 
             "Cease", "CEASE", "leave", "Leave", "LEAVE", "finish", "Finish", 
             "FINISH", "", "\n"]

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
            break
except FileNotFoundError:
    writeMode = "x"
    

with open("table.csv", writeMode, newline="") as table:
    writer = csv.writer(table, delimiter="|",
                           quotechar="|", quoting=csv.QUOTE_MINIMAL)
    if writeMode == "w" or writeMode == "x": 
        writer.writerow(HEADER)

    entriesDone = False
    nextRowToWrite = [None] * len(HEADER)
    i=0
    longestHeaderLength = longestLengthInList(HEADER)

    # Data entry prompts and input with hacky solution for verifying inputs.
    while entriesDone == False:
        i = 0
        for eachValue in nextRowToWrite:
            while True:
                headerDisplay = HEADER[i] + ":" + " " * (longestHeaderLength - len(HEADER[i]) + 1)
                inputWord = input(f"{TextColors.OKCYAN}Enter the {headerDisplay}{TextColors.ENDC}")
                if inputWord in stopWords: 
                    entriesDone = True
                    break

                if MUSTBENUMBER: 
                    try: 
                        float(inputWord)
                    except ValueError:
                        print(f"{TextColors.FAIL}Not a number.")
                        continue

                nextRowToWrite[i] = inputWord
                i += 1
                break

            if entriesDone == True: break

        print("") # nicer formatting
        if entriesDone == True: break
        writer.writerow(nextRowToWrite)

print(f"{Cursor.UP}{Cursor.CLEAR}" * (i + 2) + f"{TextColors.OKGREEN}Exited and saved.")