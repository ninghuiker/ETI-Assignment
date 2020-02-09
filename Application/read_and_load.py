#Read and Load Function 

import csv

def Read_Load(finalList):
    print('\nOption [1] Read and load maze from file')
    print('')
    userinput = input('Enter the name of the data file:')
    
    if userinput[-4:] == ".csv":
        try:
            file = open(userinput)
            row = len(file.readlines())
            print('Number of lines reads:', str(row))
            if len(finalList) > 0:
                finalList = []
            save_data(finalList, userinput)
        except:
            print("\nError: please key in the correct name of the data file")
        
    else:
        print("\nError: please key in an excel file")
        #Read_Load() 
    
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
            
