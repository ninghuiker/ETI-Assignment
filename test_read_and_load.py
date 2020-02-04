import pytest
import mock
import builtins
from main_menu import *
from read_and_load import *
from view_maze import *

def test_read_load_csv():
    test = mainMenu(1)
    assert test == "viewing maze"
    
