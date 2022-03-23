'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################

def setUpDartboard(window, myturtle):
  '''
  this function sets the limits of the window and creates the dartboard
  args: window and the turtle created
  returns: a drawing of the dartboard
  '''
  window.setworldcoordinates(-1,0,2,3)
  myturtle.color("black")
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle, -1, 2, 1, 2)
  drawLine(myturtle, 0, 3, 0, 1)
  drawCircle(myturtle, 1)

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  '''
  function draws a square in the window
  args: the turtle, the width of the square, the cooardinates of the top left corer
  returns: a drawn square 
  '''
  myturtle.penup()
  myturtle.goto(top_left_x, top_left_y)
  myturtle.pendown()
  for angle in range(4):
    myturtle.forward(width)
    myturtle.left(90)

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  '''
  draws a line between two given coordinates
  args: the turtle, the beginning and end coordinates
  returns: a horizontal and vertical axis
  '''
  myturtle.penup()
  myturtle.goto(x_start, y_start)
  myturtle.pendown()
  myturtle.goto(x_end, y_end)

def drawCircle(myturtle, radius):
  '''
  takes a radius and draws a circle from it
  args: the turtle and the radius of the circle
  returns: a circle on the window
  '''
  myturtle.pendown()
  myturtle.circle(radius)

def throwDart(myturtle):
  '''
  sends the turtle to a random position on the board
  args: the turtle
  returns: a dot in a random spot on the board, it the dot is in the circle the 
  dot will be green, if the dot is outside the circle, the dot will be red
  '''
  myturtle.penup()
  myturtle.goto(random.uniform(-1,1), random.uniform(1,3))
  if myturtle.distance(0,2) < 1:
    myturtle.color("green")
  else:
    myturtle.color("red")
  myturtle.dot()

def isInCircle(myturtle):
  '''
  checks if the dot is within one unit of the origin of the circle
  args: the turtle
  returns: True if the dot is in the circle, false if not
  '''
  if myturtle.distance(0,2) < 1:
    return True
  else:
    return False

def playDarts(myturtle):
  '''
  Sends ten darts for each player, checks to see if the dart is in the circle or 
  not and awards the player for which the dart is in the circle, does the sume, 
  then announces the 
  winner
  args: the turtle
  returns: the points of the two players and which has won
  '''
  playerOneScore = 0
  playerTwoScore = 0
  for throw in range(10):
    throwDart(myturtle)
    if isInCircle(myturtle) == True:
      playerOneScore += 1
    throwDart(myturtle)
    if isInCircle(myturtle) == False:
      playerTwoScore += 1
  print("Player one has",playerOneScore, "points" )
  print("Player two has",playerTwoScore, "points" )
  if playerOneScore > playerTwoScore:
    print("Player one has won!")
  elif playerOneScore == playerTwoScore:
    print("Tie!")
  else:
    print("Player Two has won!")

def montePi(myturtle, number_darts):
  '''
  throws a given number of darts in the circle and calculates the darts in 
  circle/numdarts * 4 which should be close to pi
  args: the turtle, the number of darts thrown
  returns: the number of darts in the circle over the total number of darts times 4
  '''
  inside_count = 0
  for i in range(number_darts):
    throwDart(myturtle)
    if isInCircle(myturtle) == True:
      inside_count += 1
  return (inside_count/number_darts)*4

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
  
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()
main()
