"""
-------------------------------------------------------
# frozen-maze.py
Create a maze similar to Frozen-v0 from OpenAI Gym
and use a Stack to solve it using Breadth-first search.
-------------------------------------------------------
Author:  Rick Henderson
Email:   rhenderson@wlu.ca
__created__ = "2016-05-06"
__updated__ = "2016-05-13"
-------------------------------------------------------
"""
import numpy as np
from stack import Stack

print("\n===== An A-MAZEing Solution =====\n")

# Create the stack to store agent moves.
moves = Stack()

"""
Constants
  - taken directly from the OpenAI Gym env frozen_lake.py
"""

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

MAPS = {
    "4x4": [
        "SFFF",
        "FHFH",
        "FFFH",
        "HFFG"
    ],
    "8x8": [
        "SFFFFFFF",
        "FFFFFFFF",
        "FFFHFFFF",
        "FFFFFHFF",
        "FFFHFFFF",
        "FHHFFFHF",
        "FHFFHFHF",
        "FFFHFFFG"
    ],
}

# Set the map name to your preferred size. 4x4 or 8x8
map_name = "4x4"

# Store the required map. desc may stand for 'description' as used in the OpenAI Gym environment
# Basically, I'm copying a lot of the OpenAI code to try and understand it better.
desc = MAPS[map_name]

# Convert the list into an Array by column
desc = np.asarray(desc, dtype='c')

# Store the number of rows and number of columns
# shape returns a tuple
# nrow, ncol = desc.shape # Works
nRows = desc.shape[0]
nCols = desc.shape[1]
print("The current maze has {} rows and {} columns.".format(nRows, nCols))
print(desc) # Prints the map.

# The Agent starts at position S, which is at index 0,0
xpos = 0
ypos = 0

# Look for next safe position
for x in range(-1,1):
	for y in range(-1,1):
		if not (x == xpos and y == ypos) and not (x == y):
			# Can't check out of bounds
			if (xpos + x) >= 0 or (ypos + y) >= 0:
				# Check to see the current next position is safe.
				if desc[xpos + x, ypos + y] == "G":
					# You found the Goal
					print("You won!")
					exit() # Probably a better way
				elif desc[xpos + x, ypos + y] == "H":
					# Contains a hole
					print("Hole found at {},{}".format(xpos+x, ypos+y))
				else:
					# You found a frozen area, store it in the stack
					moves.push([xpos + x, ypos + y])
					print("Safe: {}", [xpos + x, ypos + y])

# Now need some other set of actions.


print("** Program complete. **")
