# All things displaying stuff #

### SETS UP ALL INITIAL CONDITIONS AND WINDOW STUFFS ###

import pygame, sys
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
CENTRE = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Q-Learning Path Finder')
windowSurface.fill((255, 255, 255))

# Create colour class
class Colour:
	def __init__(self):
		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.RED = (255, 0, 0)
		self.GREEN = (0, 255, 0)
		self.BLUE = (0, 0, 255)
		
colour = Colour()

################### FUNCTIONS ####################

# Draw grid
def drawGrid(columns, rows, edgeMargin, stateList):
	for column in range(columns):
		for row in range(rows):
			cell = stateList[column][row]
			
			# Fill in grid cells
			pygame.draw.rect(windowSurface, cell.colour, (cell.leftEdge, cell.topEdge, cell.width, cell.height), 0)
			# Draw grid cell outlines
			pygame.draw.rect(windowSurface, colour.BLACK, (cell.leftEdge, cell.topEdge, cell.width, cell.height), 1)
			
	# Add outer edge to look pretty
	pygame.draw.rect(windowSurface, colour.BLACK, (edgeMargin-1, edgeMargin-1, WINDOWWIDTH-(2*edgeMargin)+2, WINDOWHEIGHT-(2*edgeMargin)+2), 1)

	pygame.display.update()


# Display finder cell
def showFinderCell(finderCell, stateList):
	cell = stateList[finderCell.position[0]][finderCell.position[1]]
	pygame.draw.rect(windowSurface, colour.BLUE, (cell.leftEdge+1, cell.topEdge+1, cell.width-2, cell.height-2), 0)
