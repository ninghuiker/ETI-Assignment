import pytest
import mock
import builtins
#from main_menu import *
#from read_and_load import *
import read_and_load
import time
#from view_maze import *

inputs = ["1", "maze.csv"]
ouput = []

def mockInput(s):
    ouput.append(s)
    return inputs.pop(0)

def test_read_load_csv():
    

    read_and_load.input = mockInput
    read_and_load.print = lambda s : ouput.append(s)
    print("geer")
    print(ouput)

    read_and_load.Read_Load([])
    
        
