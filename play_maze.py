import csv


def Play_Maze(finalList):

    print("========================================")

    rowN = -1
    columnN = 0
    colStart = 0
    rowStart = 0
    colEnd = 0
    rowEnd = 0
        
    for item in finalList:
        print(item)
        rowN += 1
        for value in item:
            if value == "A":
                colStart = columnN
                rowStart = rowN
            elif value == "B":
                colEnd = columnN
                rowEnd = rowN   
            columnN += 1
        columnN = 0

    print("\nLocation of Start (A) = (Row " + str(rowStart) + ", Column " + str(colStart) + ")")
    print("Location of End (B) = (Row " + str(rowEnd) + ", Column " + str(colEnd) + ")")

    while True:
        move = input("\nPress 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MAIN MENU: ")            

        if move == "W" or move == "w":
            upRow = rowStart - 1
            upCol = colStart
            if upRow > -1:
                upPos = finalList[upRow][upCol]
                if upPos == "O":
                    print("Move Successful!")
                    for item in finalList:
                        finalList[upRow][upCol] = "A"
                        finalList[rowStart][colStart] = "O"
                        print(item)
                    rowStart = upRow
                    colStart = upCol
                elif upPos == "B":
                    print("Congratulations! You have escaped from the maze!")
                    anykey = input("\nEnter any keys to return to the Main Menu\n")
                    break
                else:
                    print("Invalid Movement. Please Try again")
            else:
                print("Invalid Movement. Please Try again")

        elif move == "A" or move == "a":
            leftRow = rowStart
            leftCol = colStart - 1
            if leftCol > -1:
                leftPos = finalList[leftRow][leftCol]
                if leftPos == "O":
                    print("Move Successful!")
                    for item in finalList:
                        finalList[leftRow][leftCol] = "A"
                        finalList[rowStart][colStart] = "O"
                        print(item)
                    rowStart = leftRow
                    colStart = leftCol
                elif leftPos == "B":
                    print("Congratulations! You have escaped from the maze!")
                    anykey = input("\nEnter any keys to return to the Main Menu\n")
                    break
                else:
                    print("Invalid Movement. Please Try again")
            else:
                print("Invalid Movement. Please Try again")
                

        if move == "S" or move == "s":
            downRow = rowStart + 1
            downCol = colStart
            if rowStart < 8:
                downPos = finalList[downRow][downCol]
                if downPos == "O":
                    print("Move Successful!")
                    for item in finalList:
                        finalList[downRow][downCol] = "A"
                        finalList[rowStart][colStart] = "O"
                        print(item)
                    rowStart = downRow
                    colStart = downCol
                elif downPos == "B":
                    print("Congratulations! You have escaped from the maze!")
                    anykey = input("\nEnter any keys to return to the Main Menu\n")
                    break
                else:
                    print("Invalid Movement. Please Try again")
            else:
                print("Invalid Movement. Please Try again")

        elif move == "D" or move == "d":
            rightRow = rowStart
            rightCol = colStart + 1
            if rightCol < 8:
                rightPos = finalList[rightRow][rightCol]
                if rightPos == "O":
                    print("Move Successful!")
                    for item in finalList:
                        finalList[rightRow][rightCol] = "A"
                        finalList[rowStart][colStart] = "O"
                        print(item)
                    rowStart = rightRow
                    colStart = rightCol
                elif rightPos == "B":
                    print("Congratulations! You have escaped from the maze!")
                    anykey = input("\nEnter any keys to return to the Main Menu\n")
                    break
                else:
                    print("Invalid Movement. Please Try again")
            else:
                print("Invalid Movement. Please Try again")
                
        
        elif move == "M" or move == "m":
            break
        
