import pytest
import mock
import builtins
from play_maze import * 


# Test that the maze is displayed correctly

# Test that the move function allows 5 moves (WASD, M)
def test_get_move():
    # Test that move M brings user back to main menu
    with mock.patch("builtins.input", "m"):
        assert "Enter your input: "

# Test that the move function allows for small letters





# Test that if move input is not W,A,S,D or M, invalid message is displayed



# Test that move is valid if A moves towards a "O"


# Test that move is invalid if A moves towards a "O"



# Test that congratulations message is displayed after A touches B


# Test that user is returned to main menu after A touches B
 
