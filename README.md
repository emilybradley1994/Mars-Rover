**<h1>Problem : Mars Rover</h1>**

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

 

A rover’s position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).



 

**<h1>Input:</h1>** 

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.
The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau.
The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation.
Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.
Output: The output for each rover should be its final co-ordinates and heading.

 

**<h2>Input and Output</h2>**

**<h3>Test Input:</h3>**

5 5

1 2 N

LMLMLMLMM

3 3 E

MMRMMRMRRM

 

**<h3>Expected Output:</h3>**

1 3 N

5 1 E


<br><br><br>

**<h1>Design and assumptions</h1>**

I have designed an OOP structure for this project, where all code can be found in the 'mars_rover_main.py' file, and all testing can be found in the 'test_rover.py' file.

I have implemented a 'MarsRover' class which initializes the parameters 'X' (the X-coordinate of the rover's initial position), 'Y' (the Y-coordinate of the rover's initial position), 'heading' (the rover's initial heading - 'N', 'S', 'E' or 'W') and plateau (linking the rover to the instance of Plateau created prior, as to ensure that the rover remains within the confines of the plateau). This class contains all functions related to the Rover that is currently moving; its position, processing and running its movement, and printing the result of its movement.

I have implemented a 'Plateau' class which sets the size of the plateau, and verifies that the rovers remains inside the plateau.

I have made the assumption that input will be of the form of two integers with a space inbetween (for example, [3 4]) when setting the size of the plateau. I have also made the assumption that input for the rover's initial position will be of the form of two integers followed by one of 'N', 'S', 'E' or 'W', with a space inbetween (for example, [3 4 S]). The input of directions for the rover is assumed to be a sequence using only the capital letters 'L', 'R' and 'M' without a space (for example [LMMRRLMMLMR])
 
 Please include a brief explanation of your design and assumptions, along with your code, as well as detailed instructions to run your application.
 
 <br><br><br>
 **<h1>Instructions</h1>**
 
-- Requires Python installed --
 
<h3>To run the main code:</h3>
<ol>
 <li>Extract files from MarsRover.zip</li>
 <li>Run at command line/terminal: python mars_rover_main.py</li>
 <li>When prompted with 'Plateau size:', input height and width of plateau using the structure of two integers separated by a space</li>
 <li>When prompted with 'Position:', input initial position of rover using the structure of two integers (X- and Y-coordinate) and one of 'N', 'E', 'S', 'W', separated by a space</li>
 <li>When prompted with 'Please input directions for rover.', enter a sequence using the capital letters 'L', 'M' and 'R' with no space</li>
 </ol>
 <br>
<h3>To run the test:</h3>
<ol>
 <li>Extract files from MarsRover.zip</li>
 <li>Run at command line/terminal: test_rover.py</li>
 </ol>
 
  





