#Read and Load Function 

import csv

def Read_Load(finalList):
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
        if len(finalList) > 0:
            finalList = []
        save_data(finalList, userinput)
    
    
    anykey = input("\nEnter anything to return to Main Menu\n")
    return finalList
    
def save_data(finalList, userinput):
    with open(userinput) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        innerlist = []
        for row in readCSV:
            for column in row:
                innerlist.append(column)
            finalList.append(innerlist)
            innerlist = []
            
