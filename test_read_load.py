import pytest
#from ETI-Assignment.read_and_load import* Im not sure about this
import csv
result = ""

def test_input_filename():
    result = check_filename("maze.csv")
    assert result == "Correct filename"

def test_filename_case_sensitive():
    result = check_filename("ABC")
    assert result == "Incorrect filename"
