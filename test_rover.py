import unittest
from mars_rover_main import Plateau, MarsRover


class TestPlateau(unittest.TestCase):

    def test_create_plateau(self):
        plateau = Plateau(7, 7)

        self.assertEqual(plateau.width, 7)
        self.assertEqual(plateau.height, 7)

    def test_move_unavailable_north(self):

        plateau = Plateau(5, 10)
        rover = MarsRover(5, 10, 'N', plateau)
        rover.move()
        result = plateau.check_move_available(rover)
        self.assertEqual(result, True)

    def test_move_unavailable_south(self):

        plateau = Plateau(5, 10)
        rover = MarsRover(5, 0, 'S', plateau)
        rover.move()
        result = plateau.check_move_available(rover)
        self.assertEqual(result, True)

    def test_move_unavailable_east(self):

        plateau = Plateau(5, 10)
        rover = MarsRover(5, 10, 'E', plateau)
        rover.move()
        result = plateau.check_move_available(rover)
        self.assertEqual(result, True)

    def test_move_unavailable_west(self):

        plateau = Plateau(5, 10)
        rover = MarsRover(0, 10, 'W', plateau)
        rover.move()
        result = plateau.check_move_available(rover)
        self.assertEqual(result, True)    


class TestRover(unittest.TestCase):

    def test_move_forward_north(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'N', plateau)
        rover.move()
        self.assertEqual(rover.Y, 21)   

    def test_move_forward_south(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'S', plateau)
        rover.move()
        self.assertEqual(rover.Y, 19)  

    def test_move_forward_east(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'E', plateau)
        rover.move()
        self.assertEqual(rover.X, 21)  

    def test_move_forward_west(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'W', plateau)
        rover.move()
        self.assertEqual(rover.X, 19)  


    def rotate_left_from_north(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'N', plateau)
        rover.rotate_left()
        self.assertEqual(rover.heading, 'W')

    def rotate_left_from_west(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'W', plateau)
        rover.rotate_left()
        self.assertEqual(rover.heading, 'S')    

    def rotate_left_from_south(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'S', plateau)
        rover.rotate_left()
        self.assertEqual(rover.heading, 'E') 

    def rotate_left_from_east(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'E', plateau)
        rover.rotate_left()
        self.assertEqual(rover.heading, 'N')   


    def rotate_right_from_north(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'N', plateau)
        rover.rotate_right()
        self.assertEqual(rover.heading, 'E')

    def rotate_right_from_east(self):

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'E', plateau)
        rover.rotate_right()
        self.assertEqual(rover.heading, 'S')   

    def rotate_right_from_south(self): 

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'S', plateau)
        rover.rotate_right()
        self.assertEqual(rover.heading, 'W') 

    def rotate_right_from_west(self): 

        plateau = Plateau(30, 30)
        rover = MarsRover(20, 20, 'W', plateau)
        rover.rotate_right()
        self.assertEqual(rover.heading, 'N')



if __name__ == '__main__':
    unittest.main()