from read_and_load import *

def mainMenu():
    print('MAIN MENU\n=========')
    print('[1] Read and load maze from file')
    print('[2] View Maze')
    print('[3] Play maze game')
    print('[4] Configure current maze')
    print('\n[0] Exit Maze\n')


    while True:
        try:
            selection = int(input('Enter your input:'))
            if selection==1:
                Read_Load()
                break
            elif selection==2:
                View()
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
