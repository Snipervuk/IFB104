
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10194444
#    Student name: Christian Milicevic 
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#

# Erect buildings as per the provided city plan
def make_building_shape(list_building_format): #Creating a bulding function to use for creating building parts
    begin_fill()
    for length in list_building_format:
        forward(length)
        left(90)
    setheading(0)
    end_fill()


def draw_A_base(): #Draws building's A base
    home_x = xcor()
    home_y = ycor()
    
    fillcolor('MediumBlue') #Fills colour with MediumBlue
    pendown()
    

    A_Base_Num = [50,20,100,20,50] #List the dimensions for base A
    make_building_shape(A_Base_Num)
   

#Draws a door
    fillcolor('Black') #Fills colour with Black
    
    door_num = [7.5, 15, 15, 15] #List the dimensions for the door 
    make_building_shape(door_num)

    penup()
    goto(home_x, home_y)

#Draws windows for the building
def draw_A_window():
    make_building_shape([20,20,20,20])

def draw_A_floor(): #Creating building A's floor part
    home_x = xcor()
    home_y = ycor()
    
    fillcolor('MediumBlue') #Fills colour with MediumBlue
    pendown()

    A_floor_Num = [50,26,100,26,50] #Dimenstions for floor A floor
    make_building_shape(A_floor_Num)

#Add windows
    fillcolor('MediumSlateBlue') #Fills colour with MediumSlateBlue

    penup()
    goto(xcor() - 40 , ycor() +3)
    pendown()
    for window in range(3):
        draw_A_window()
        penup()
        forward(30)
        pendown()
        
    penup()
    goto(home_x, home_y)
    

def draw_A_roof(): #Draws building A roof part
    home_x = xcor()
    home_y = ycor()
    
    pendown()
    fillcolor('BlueViolet')
    begin_fill()
    forward(50)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(50)
    end_fill()

    penup()
    goto(home_x, home_y)
    
    
def draw_B_base(): #Draws building B base part
    home_x = xcor()
    home_y = ycor()
    
    pendown()
    fillcolor('Lime')
    B_base_Num = [100, 25, 200, 25, 100]
    make_building_shape(B_base_Num)
    penup()

    #Draw doors
    goto(xcor() -50, ycor())
    pendown()
    door_num2 = [10, 23, 10, 23]
    fillcolor('Olive')
    make_building_shape(door_num2)
    penup()
    forward(90)
    pendown()
    make_building_shape(door_num2)

    penup()
    goto(home_x, home_y)


def draw_B_floor(width): #Draws building B floor part
    home_x = xcor()
    home_y = ycor()
    
    pendown()
    fillcolor('Lime')
    B_floor_Num = [width/2, 26, width, 26, width/2]
    make_building_shape(B_floor_Num)
    penup()

    #Work how many windows will fit on floor
    windows_left = int(10 - abs(width - 200)/18)

    #Draw windows
    goto( xcor() - width/2 + 19, ycor() + 6)
    fillcolor('White')
    for window in range(windows_left):
        pendown()
        begin_fill()
        circle(7)
        end_fill()
        penup()
        forward(18)
    
    penup()
    goto(home_x, home_y)
        
def draw_B_roof(): #Draws building B roof part
    home_x = xcor()
    home_y = ycor()
    
    goto( xcor() - 15, ycor())
    pendown()
    left(90)
    forward(20)
    penup()
    goto( xcor() + 30, ycor() -20)
    pendown()
    forward(20)
    right(90)

    fillcolor('Orange')
    B_roof_num = [30, 40, 88, 40, 58]
    make_building_shape(B_roof_num)
    penup()

    goto(home_x, home_y)

def draw_pillar_feet(): #Creates the pillar feet for building C base
    pendown()
    fillcolor('Tan')
    begin_fill()
    forward(30)
    left(117)
    forward(11)
    left(63)
    forward(20)
    left(63)
    forward(11)
    left(117)
    end_fill()
    penup()
    

def draw_C_base(): #Draws building C base
    home_x = xcor()
    home_y = ycor()
    
    pendown()
    fillcolor('Peru')
    C_base_num = [90, 25, 180, 25, 90]
    make_building_shape(C_base_num)
    penup()
    

    #Draw base pillars
    goto( xcor() - 80, ycor()+25)
    draw_pillar_feet()
    forward(40)
    draw_pillar_feet()
    forward(50)
    draw_pillar_feet()
    forward(40)
    draw_pillar_feet()

    goto(home_x, home_y)

def draw_C_floor(): #Draws building C floor
    home_x = xcor()
    home_y = ycor()
    
    goto( xcor() - 75, ycor())
    pendown()
    box_num = [20, 20, 20, 20]
    make_building_shape(box_num)
    penup()
    forward(40)
    pendown()
    make_building_shape(box_num)
    penup()
    forward(50)
    pendown()
    make_building_shape(box_num)
    penup()
    forward(40)
    pendown()
    make_building_shape(box_num)
    penup()

    goto(home_x, home_y)
    
def draw_C_roof(): #Draws building C roof
    home_x = xcor()
    home_y = ycor()
    
    setheading(180)
    goto( xcor() + 80, ycor()+10)
    draw_pillar_feet()
    forward(40)
    draw_pillar_feet()
    forward(50)
    draw_pillar_feet()
    forward(40)
    draw_pillar_feet()
    
    pendown()
    forward(30)
    setheading(0)
    roof_num = [170,25, 180, 25, 10]
    fillcolor('Peru')
    make_building_shape(roof_num)
    penup()

    left(90)
    forward(25)
    fillcolor('Tan')
    pendown()
    begin_fill()
    right(90)
    forward(157)
    left(120)
    forward(156)
    left(120)
    forward(156)
    end_fill()
    penup()
    setheading(0)

    goto(home_x, home_y)

def draw_D_base(): #Draws building D base
    home_x = xcor()
    home_y = ycor()

    fillcolor('OrangeRed')
    pendown()

    D_base_num = [35, 40, 70, 40, 35]
    make_building_shape(D_base_num)

    #Draw a door
    fillcolor('Magenta')
    
    door_num3 = [8, 20, 16, 20, 8]
    make_building_shape(door_num3)

    penup()

    goto(home_x, home_y)

def draw_D_floor(): #Draws building D floor 
    home_x = xcor()
    home_y = ycor()
    
    fillcolor('OrangeRed')
    pendown()

    D_floor_num = [35, 40, 70, 40, 35]
    make_building_shape(D_floor_num)

    penup()

    #Draws windows
    goto(xcor() +15, ycor() + 30)
    fillcolor('Cyan')
    pendown()
    begin_fill()
    setheading(180)
    circle(10, steps = 3)
    end_fill()
    penup()
    forward(30)
    pendown()
    begin_fill()
    circle(10, steps = 3)
    end_fill()
    penup()
    setheading(0)

    goto(home_x, home_y)
    
def draw_D_roof(): #Draws building D roof 
    home_x = xcor()
    home_y = ycor()
    
    fillcolor('Gold')
    pendown()

    D_roof_num = [35, 40, 70, 40, 35]
    make_building_shape(D_roof_num)
    penup()
    
    #Draws the arch on top of building D's roof
    goto(xcor() + 35, ycor()+ 38)
    color('Gold')
    pensize(3)
    pendown()
    
    setheading(90)
    circle(17, 180)
    setheading(90)
    circle(17, 180)
    penup()
    width(1)
    color('Black')
    setheading(0)
    
    goto(home_x, home_y)

#------------------Part B Code incropated 

def draw_warning_sign(): #Function creates the warning sign to be placed on top of buildings
    
    home_x = xcor()
    home_y = ycor()

    forward(20)
    pendown()
    left(90)
    forward(30)
    penup()
    goto(home_x - 20, home_y)
    pendown()
    forward(30)
    penup()
    left(90)
    forward(20)
    pendown()
    begin_fill()
    fillcolor('Yellow')    
    right(120)
    forward(80)
    right(120)
    forward(80)
    right(120)
    forward(80)
    end_fill()
    penup()

    goto(home_x, home_y + 40) #Creates dot inside the warning sign
    fillcolor('Black')
    dot(7)

    goto(xcor(), ycor() + 10) #Creates triangular shape inside the warning sign
    pendown()
    begin_fill()
    setheading(80)
    forward(30)
    setheading(180)
    forward(10)
    setheading(280)
    forward(30)
    end_fill()
    penup()
    setheading(0)


def build_A(floors, warning_sign): #Creates warning sign on top of the building whenever 'X' is present 
    draw_A_base()
    goto(xcor(), ycor() + 20)
    for floor in range(floors):
        draw_A_floor()
        goto(xcor(), ycor() + 26)
    if (warning_sign == 'X'):
        draw_warning_sign()
    else:
        draw_A_roof()

        
def build_B(floors, warning_sign): #Creates warning sign on top of the building whenever 'X' is present
    draw_B_base()
    goto(xcor(), ycor() + 25)
    width = 200
    for floor in range(floors):
        draw_B_floor(width)
        width -= 18
        goto(xcor(), ycor() + 26)
    if (warning_sign == 'X'):
        draw_warning_sign()
    else:
        draw_B_roof()

def build_C(floors, warning_sign): #Creates warning sign on top of the building whenever 'X' is present
    draw_C_base()
    goto(xcor(), ycor() + 35)
    for floor in range(floors):
        draw_C_floor()
        goto(xcor(), ycor() + 20)
    if (warning_sign == 'X'):
        draw_warning_sign()
    else:
        draw_C_roof()

def build_D(floors, warning_sign): #Creates warning sign on top of the building whenever 'X' is present
    draw_D_base()
    goto(xcor(), ycor() + 40)
    for floor in range(floors):
        draw_D_floor()
        goto(xcor(), ycor() + 40)
    if (warning_sign == 'X'):
        draw_warning_sign()
    else:
        draw_D_roof()


def build_city(dataset):
    #Build dictionary for site coords
    sites = {1 : [-225, 0],
             2 : [25,0],
             3 : [275,0],
             4 :[-375,-25],
             5 : [-125,-25],
             6 : [125,-25],
             7 : [375,-25],
             8 : [-275,-50],
             9 : [-25,-50],
             10 : [225,-50]}
    
    
    for each_building in dataset:
        #Place turtle cursor at relevant site
        site_coords = sites[each_building[0]]
        # goto(x,y)
        goto(site_coords[0], site_coords[1])
        print("Building set:",each_building)
        
        if each_building[1] == 'A':
            build_A(each_building[2], each_building[3])
        elif each_building[1] == 'B':
            build_B(each_building[2], each_building[3])
        elif each_building[1] == 'C':
            build_C(each_building[2], each_building[3]) 
        elif each_building[1] == 'D':
            build_D(each_building[2], each_building[3])
            
    print("Done.") # Print when program is done running
    
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Last Minute City")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
# build_city(fixed_plan_1) # <-- used for code development only, not marking


build_city(random_plan()) # <-- used for assessment



# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

