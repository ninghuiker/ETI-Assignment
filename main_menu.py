from read_and_load import *
from view_maze import *
from play_maze import *
from configure_maze import *

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

    while True:
        try:
            selection = input('Enter your input:')
            if selection=='1':
                Read_Load(finalList)
            elif selection=='2':
                View_Maze(finalList)
            elif selection=='3':
                Play_Maze(finalList)
            elif selection =='4':
                Configure_Maze(finalList)
            elif selection=='0':
                quit()
            else:
                print("Invalid choice. Enter 0-4")
                mainMenu()
        except ValueError:
            print("Invalid syntax. Enter 0-4")
    exit

def Exit():
    quit()
    
mainMenu()
