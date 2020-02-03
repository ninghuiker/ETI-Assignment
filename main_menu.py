from read_and_load import *
from view_maze import *
from play_maze import *


def mainMenu():
    finalList = []
    print("""Main Menu
=========
[1] Read and load maze from file
[2] View Maze
[3] Play maze game
[4] Configure current maze

[0] Exit Maze\n""")

    while True:
        try:
            selection = int(input('Enter your input:'))
            if selection==1:
                Read_Load(finalList)
            elif selection==2:
                View_Maze(finalList)
            elif selection==3:
                Play_Maze(finalList)
            elif selection==0:
                quit()
            else:
                print("Invalid choice. Enter 1-5")
                mainMenu()
        except ValueError:
            print("Invalid syntax. Enter 1-5")
    exit

def Exit():
    quit()
    
mainMenu()
