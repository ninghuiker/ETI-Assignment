import pytest

from main_menu import *

def test_mainmenu():
    menu = mainMenu()
    assert ("""Main Menu
=========
[1] Read and load maze from file
[2] View Maze
[3] Play maze game
[4] Configure current maze

[0] Exit Maze\n""")

    
    
    

