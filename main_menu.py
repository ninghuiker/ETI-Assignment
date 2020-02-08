from read_and_load import *
from view_maze import *
from play_maze import *
from configure_maze import *

options = ['1','2','3','4']
def mainMenu():
    finalList = []
    print("""Main Menu
=========
[1] Read and load maze from file
[2] View Maze
[3] Play maze game
[4] Configure current maze

[0] Exit Maze\n""")
    #return False (unit test case for menu)
    select = 0 

    while True:
        selection = input('Enter your input:')
        if selection not in options:
            print("Invalid syntax. Enter 0-4")
        if select == 0:                    
            if selection=='1':
                Read_Load(finalList)
                if finalList != []:
                    select = select + 1
            else:
                print("Please enter option 1 first to load the file.")
        else:
            if selection=='1':
                Read_Load(finalList)
            if selection=='2':
                View_Maze(finalList)
            elif selection=='3':
                Play_Maze(finalList)
            elif selection=='4':
                Configure_Maze(finalList)
        if selection=='0':
            quit()

    exit

def Exit():
    quit()
    
mainMenu()
