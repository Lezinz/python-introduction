from src import MarsRover, Direction

def test_init_rover():
    rover = MarsRover((2, 4), Direction.NORTH)
    assert rover.coordinates == (2, 4)
    assert rover.direction == Direction.NORTH

def test_advance_rover_north():
    rover = MarsRover((2, 4), Direction.NORTH)
    rover.advance()
    assert rover.coordinates == (2, 3)

def test_advance_rover_south():
    rover = MarsRover((2, 4), Direction.SOUTH)
    rover.advance()
    assert rover.coordinates == (2, 5)

def test_advance_rover_east():
    rover = MarsRover((2, 4), Direction.EAST)
    rover.advance()
    assert rover.coordinates == (3, 4)

def test_advance_rover_west():
    rover = MarsRover((2, 4), Direction.WEST)
    rover.advance()
    assert rover.coordinates == (1, 4)