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

    print("Configuration Menu")
      
    print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
      
    while True:
        Choice = input("Enter your options to configure: ")
        #Choice = input("\n Enter your options: ")
        
        if Choice == "1":
            print("Enter the coordinate of the item you wish to change E.g Rows,Colum:")

            
            value1=int(input("Enter Row:"))
            value2=int(input("Enter Col:"))
            value1 = rowStart
            value2 = colStart
            if value1 < 8:
             for item in finalList:
                 finalList[value1][value2] = "X"
                
                 print(item)
                 rowStart = value1
                 colStart = value2



               #else:
                   #print("Invalid Movement. Please Try again")
             #else:
              #print("'B' to return to Configure Menu.")
              #print("'M' to return to Main Menu:")
   



           #All this tried
            #value1 = rowStart 
            #value2 = colStart
            #if value1 < 8 and value2 < 8:
                #pos = finalList[value1][value2]
                
                    #for item in finalList:
                      
                        #finalList[rowStart][colStart] = "X"
                        #print(item)
                  
                    #rowStart = value1
                    #colStart = value2


                         
         #Tried second
            #value1=int(input("Enter Row:"))
            #value2=int(input("Enter Col:"))
            #for item in finalList:
                  #finalList[value1][value2] = "X"
                  #finalList[newvalue1][newvalue2]=
                  #print(item)
     
                          
         





        
      
        #if Choice == "2":
        #if Choice == "3":
        #if Choice == "4":
        elif Choice =="B" or Choice == "b":
            
            print("Configuration Menu")
            print("=================")      
            print("""[1] Create Wall
[2] Create Passageway
[3] Create start point
[4] Create end point
[0] Exit Main Menu\n""")
                         
                          

        elif Choice == "M" or Choice == "m":
                break
            
