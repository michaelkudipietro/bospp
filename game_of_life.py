'''Conway's Game of Life, by Al Sweigart
The classic cellular automata simulation. Press CRTL-C to stop.
'''

import copy, random, sys, time

#Set up constants
WIDTH = 79 #width of cell grid
HEIGHT= 20 #height of cell grid

ALIVE='0' #the character representing a living cell
DEAD=' '

#The cells and nextCells are dictionaries for the state of the game.
#their keys are (x,y) tuples and their values are one of the aLIVE
#or DEAD cells

nextCells={}
#put random dead and alive cells into nextCells
for x in range(WIDTH): #loop over each column
    for y in range(HEIGHT): #loop over every possible row
        #50/50 change for starting cells to be dead or alive
        if random.randint(0,1) == 0:
            nextCells[(x,y)]=ALIVE #Add a living cell
        else:
            nextCells[(x,y)]=DEAD #Add a dead cell

while True: #main program loop
    #Each iteration of this loop is a step of the simulation

    print('\n'*50) #separate each step with newlines
    cells=copy.deepcopy(nextCells)

    #print cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)],end='') #Print the # or space
        print() #add a newline at the end of the row
    print('Press CTRL + C to quit.')

    #Calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get the neigboring coordinate of (x,y) even if they
            #wrap around the edge
            left  = (x-1)%WIDTH
            right = (x+1)%WIDTH
            above = (y+1)%HEIGHT
            below = (y-1)%HEIGHT

            #Calculate the number of living neighbors
            numNeighbors=0
            if cells[(left,above)]==ALIVE:
                numNeighbors+=1 #Top left neighbor is alive
            if cells[(x,above)]==ALIVE:
                numNeighbors+=1 #Top neighbor is alive
            if cells[(right, above)]==ALIVE:
                numNeighbors+=1 #Top right neighbor is alive
            if cells[(left,y)]==ALIVE:
                numNeighbors+=1 #Left neighbor is alive
            if cells[(right,y)]==ALIVE:
                numNeighbors+=1 #Right neighbor is alive
            if cells[(right,below)]==ALIVE:
                numNeighbors+=1 #bottom right neighbor is alive
            if cells [(left, below)]==ALIVE:
                numNeighbors+=1 #bottom left neighbor is alive
            if cells[(x,below)]==ALIVE:
                numNeighbors+=1 #bottom neighbor is alive

            #Set cell based on Conway's Game of Life rules
            if cells[(x,y)]==ALIVE and (numNeighbors==2 or numNeighbors==3):
                #living cells with 2 or 3 neighbor cells stay alive
                nextCells[(x,y)]=ALIVE
            elif cells[(x,y)]==DEAD and numNeighbors==3:
                #Dead cells with 3 neighbors become alive
                nextCells[(x,y)]=ALIVE
            else:
                #everything else stays dead
                nextCells[(x,y)]=DEAD
    try:
        time.sleep(1) #add a one second pause to reduce flickering
    except KeyboardInterrupt:
        print("Conway's Game of Life, by Al Sweigart")
        sys.exit() #When CRTL+C is pressed, end the program
