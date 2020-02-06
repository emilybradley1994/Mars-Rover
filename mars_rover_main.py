class Plateau():
     
    
    
    def __init__(self, width, height, min_width = 0, min_height = 0):        
        self.width = width
        self.height = height
        self.min_width = min_width
        self.min_height = min_height
                

    def check_move_available(self, rover):        
        return rover.X > self.width or rover.Y > self.height or rover.X < self.min_width or rover.Y < self.min_height


    

class MarsRover():
    
    RIGHT_ROTATE = {
        'N':'E',
        'E':'S',
        'S':'W',
        'W':'N'
    }

    LEFT_ROTATE = {
        'N':'W',
        'W':'S',
        'S':'E',
        'E':'N'
    }
    
    

    def __init__(self, X, Y, heading, plateau):
        self.X = X
        self.Y = Y
        self.heading = heading
        self.plateau = plateau
        
        
    def run_instructions(self, instruction):
        if instruction == 'L':
            self.rotate_left()
        elif instruction == 'R':
            self.rotate_right()
        elif instruction == 'M':
            self.move()
    
    
    def process(self, instructions):
        for i in range(len(instructions)):
            self.run_instructions(instructions[i])


    def rotate_right(self):
        self.heading = self.RIGHT_ROTATE[self.heading]
                         
    
    def rotate_left(self):
        self.heading = self.LEFT_ROTATE[self.heading]
            
            
    def move(self):
                
        if self.heading == 'N':
            self.Y += 1
        elif self.heading == 'E':
            self.X += 1
        elif self.heading == 'S':
            self.Y -= 1    
        elif self.heading == 'W':
            self.X -= 1
            
    def __str__(self):        
        return str(self.X) + " " + str(self.Y) + " " + self.heading
    
    
    

    
        
        
def main():

    plateau_size = input("Plateau size:")
    width = int(plateau_size[0])
    height = int(plateau_size[2])
    plateau = Plateau(width, height)
    '''Set plateau'''
    
    while True:
        position = input("Position:")
        while True:
            X = int(position[0])
            Y = int(position[2])
            direction = position[4]
            rover = MarsRover(X, Y, direction, plateau)
            instructions = input("Please input directions for rover.")
            rover.process(instructions)
            if plateau.check_move_available(rover):
                print ("You cannot move the rover here.") 
            else:
                print (rover)
                break
    
    

if __name__ == '__main__':
    
    main()
            
  