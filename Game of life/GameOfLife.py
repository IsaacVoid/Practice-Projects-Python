# Conaway's game of life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Createa list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] # Create a column
    for y in range (HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # This adds a living cell
        else:
            column.append(' ') # This adds a dead cell
    nextCells.append(column) # nextCell is a list of column lists

while True: 
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    # Print the current cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Prints the '#' or ' '
        print() # Prints a new line at the end of the row

# Calculate the new step's cells based on current cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates: 
            #  '% WIDTH' ensures leftCord is always between 0 and wIDTH - 1
            leftCord = (x - 1) % WIDTH
            rigtCord = (x + 1) % WIDTH
            aboveCord = (y - 1) % HEIGHT
            belowCord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCord][aboveCord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive
            if currentCells[x][aboveCord] == '#':
                numNeighbors += 1 # Top neighbor is alive
            if currentCells[rigtCord][aboveCord] == '#':
                numNeighbors += 1 # Topright neighbor is alive
            if currentCells[leftCord][y] == '#':
                numNeighbors += 1 # Left neighbor alive
            if currentCells[rigtCord][y] == '#':
                numNeighbors += 1 # Right neighbor alive
            if currentCells[leftCord][belowCord] == '#':
                numNeighbors += 1 # Bottom-left is alive
            if currentCells[x][belowCord] == '#': 
                numNeighbors += 1 # Bottom is alive
            if currentCells[rigtCord][belowCord] == '#':
                numNeighbors += 1 # Bottom-right alive

            # Set game rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighors stay alive: 
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else: 
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
time.sleep(5)