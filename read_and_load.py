#Read and Load Function 
def Read_Load():
    print('\nOption [1] Read and load maze from file')
    print('')
    userinput = input('Enter the name of the data file:')
    if userinput == "":
        print("\nError: please key in the name of the data file")
        Read_Load()
        
    else:
        file = open(userinput)
        row = len(file.readlines())
        print('Number of lines reads:', str(row))
 
    
    
    anykey = input("\nEnter anything to return to Main Menu\n")

from main_menu import *
mainMenu()
