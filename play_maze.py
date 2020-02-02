import csv

def Play_Maze():

    print("========================================")
    
    with open('maze.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rowN = -1
        columnN = 0
        colStart = 0
        rowStart = 0
        colEnd = 0
        rowEnd = 0
        for row in readCSV:
            print(row)
            rowN += 1
            for column in row:
                if column=="A":
                    colStart = columnN
                    rowStart = rowN
                elif column=="B":
                    colEnd = columnN
                    rowEnd = rowN   
                columnN += 1
            columnN = 0

        print("\nLocation of Start (A) = (Row " + str(colStart) + ", Column " + str(rowStart) + ")")
        print("Location of End (B) = (Row " + str(colEnd) + ", Column " + str(rowEnd) + ")\n")

        move = input("Press 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MAIN MENU: ")
                        
                        
