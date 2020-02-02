from read_and_load import *
from view_maze import *

def mainMenu():
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
                Read_Load()
                break
            elif selection==2:
                View_Maze()
                break
            elif selection==0:
                quit()
                break
            else:
                print("Invalid choice. Enter 1-5")
                mainMenu()
        except ValueError:
            print("Invalid syntax. Enter 1-5")
    exit

def Exit():
    quit()
    
mainMenu()
