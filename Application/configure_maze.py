import csv

def Configure_Maze(finalList):


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

    print("\nConfiguration Menu")
    print("========================================\n")
    print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
      
    while True:
        Choice = input("Enter your options to configure: ")
        #Choice = input("\n Enter your options: ")
        
        if Choice == "1":
            print("========================================\n")
            for item in finalList:
                print(item)
            print("Press Enter if you wish to change an item.")
            mainORconfig=(input("'B' to return to ConfigureMenu.\n'M' to return to Main Menu:"))
            
            if mainORconfig == "B" or mainORconfig == "b":
                
                print("========================================\n")
                for item in finalList:             
                    print(item)
                print("\nConfiguration Menu")
                print("========================================\n")
                print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
                
            elif mainORconfig == "M" or mainORconfig == "m":
                break
                
            elif mainORconfig == "":
                value1=input("Enter Row:")
                value2=input("Enter Col:")
                try:
                    rowChosen = int(value1)
                    colChosen = int(value2) 
                    if rowChosen < 8 and rowChosen > -1 and colChosen < 8 and colChosen > -1:
                        if finalList[rowChosen][colChosen] != "X":
                            finalList[rowChosen][colChosen] = "X"
                            print("========================================\n")
                            for item in finalList:
                                print(item)
                            print("\nConfiguration Menu")
                            print("========================================\n")
                            print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
                        
                        else:
                            print("It is already a wall.")
                            print("========================================\n")
                            for item in finalList:
                                print(item)
                            print("\nConfiguration Menu")
                            print("========================================\n")
                            print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")

                except ValueError:
                    print("Please enter a valid value.")

            else:
                print("Please enter a valid value.")


        
        # Create passage way
        elif Choice == "2":
            print("========================================\n")
            for item in finalList:
                print(item)
            print("Press Enter if you wish to change an item.")
            mainORconfig=(input("'B' to return to ConfigureMenu.\n'M' to return to Main Menu:"))
            
            if mainORconfig == "B" or mainORconfig == "b":
                
                print("========================================\n")
                for item in finalList:             
                    print(item)
                print("\nConfiguration Menu")
                print("========================================\n")
                print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
                
            elif mainORconfig == "M" or mainORconfig == "m":
                break
                
            elif mainORconfig == "":
                value1=input("Enter Row:")
                value2=input("Enter Col:")
                try:
                    rowChosen = int(value1)
                    colChosen = int(value2) 
                    if rowChosen < 8 and rowChosen > -1 and colChosen < 8 and colChosen > -1:
                        if finalList[rowChosen][colChosen] != "O":
                            finalList[rowChosen][colChosen] = "O"
                            print("========================================\n")
                            for item in finalList:
                                print(item)
                            print("\nConfiguration Menu")
                            print("========================================\n")
                            print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
                        
                        else:
                            print("It is already a passageway.")
                            print("========================================\n")
                            for item in finalList:
                                print(item)
                            print("\nConfiguration Menu")
                            print("========================================\n")
                            print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")

                except ValueError:
                    print("Please enter a valid value.")

            else:
                print("Please enter a valid value.")

                
        #Create Start point
        elif Choice == "3":
            print("========================================\n")
            for item in finalList:
                print(item)
            print("Press Enter if you wish to change an item.")
            mainORconfig=(input("'B' to return to ConfigureMenu.\n'M' to return to Main Menu:"))
            
            if mainORconfig == "B" or mainORconfig == "b":
                
                print("========================================\n")
                for item in finalList:             
                    print(item)
                print("\nConfiguration Menu")
                print("========================================\n")
                print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
                
            elif mainORconfig == "M" or mainORconfig == "m":
                break
                
            elif mainORconfig == "":
                value1=input("Enter Row:")
                value2=input("Enter Col:")
                try:
                    rowChosen = int(value1)
                    colChosen = int(value2) 
                    if rowChosen < 8 and rowChosen > -1 and colChosen < 8 and colChosen > -1:
                        if finalList[rowChosen][colChosen] != "A":
                            finalList[rowChosen][colChosen] = "A"
                            finalList[rowStart][colStart] = "O"
                            print("========================================\n")
                            for item in finalList:
                                print(item)
                            print("\nConfiguration Menu")
                            print("========================================\n")
                            print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
                        
                        else:
                            print("It is already a start point.")
                            print("========================================\n")
                            for item in finalList:
                                print(item)
                            print("\nConfiguration Menu")
                            print("========================================\n")
                            print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")

                except ValueError:
                    print("Please enter a valid value.")

            else:
                print("Please enter a valid value.")
                
                            
        #Create end point
        elif Choice == "4":
            print("========================================\n")
            for item in finalList:
                print(item)
            print("Press Enter if you wish to change an item.")
            mainORconfig=(input("'B' to return to ConfigureMenu.\n'M' to return to Main Menu:"))
            
            if mainORconfig == "B" or mainORconfig == "b":
                
                print("========================================\n")
                for item in finalList:             
                    print(item)
                print("\nConfiguration Menu")
                print("========================================\n")
                print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
                
            elif mainORconfig == "M" or mainORconfig == "m":
                break
                
            elif mainORconfig == "":
                value1=input("Enter Row:")
                value2=input("Enter Col:")
                try:
                    rowChosen = int(value1)
                    colChosen = int(value2) 
                    if rowChosen < 8 and rowChosen > -1 and colChosen < 8 and colChosen > -1:
                        if finalList[rowChosen][colChosen] != "B":
                            finalList[rowChosen][colChosen] = "B"
                            finalList[rowEnd][colEnd] = "O"
                            print("========================================\n")
                            for item in finalList:
                                print(item)
                            print("\nConfiguration Menu")
                            print("========================================\n")
                            print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
                        
                        else:
                            print("It is already an end point.")
                            print("========================================\n")
                            for item in finalList:
                                print(item)
                            print("\nConfiguration Menu")
                            print("========================================\n")
                            print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")

                except ValueError:
                    print("Please enter a valid value.")

            else:
                print("Please enter a valid value.")


        elif Choice == "0":
            break

        else:
            print("Please enter a valid value.")

               
            
