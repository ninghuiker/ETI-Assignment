import pytest
import csv
import mock

from main_menu import *
from view_maze import *

def test_viewmaze(finalList):
    
     
    #print("=========================================")
     
    for item in finalList:
        print(item)
        
    assert ("""['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X']
['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X']
['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X']
['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X']
['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X']
['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X']
['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']""")

