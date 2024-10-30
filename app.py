from termcolor import colored
from tabulate import tabulate
from utilities.cleancsv import (main as cleancsv)
from utilities.csv2xlsx import (main as csv2xlsx)

#Add functionalitites here
utilities = [
    "Clean CSV file (remove coloumns)",
    "Convert to XLSX",
    ]

def main(running):
    while running:
        print(colored(tabulate([[index + 1, utility] for index, utility in enumerate(utilities)], ["Selection", "Utility"], tablefmt="grid"), "yellow"))
        run = input(colored("Choose Utility to run, press Enter to quit: ", "light_yellow"))
        if run == "1":
            cleancsv()
            main(True)
        elif run == "2":
            csv2xlsx()
            main(True)
        break

if __name__ == "__main__":
    print(colored("\nKRISTIANS UTILITIES\n-------------------", 'blue'))
    main(True)
