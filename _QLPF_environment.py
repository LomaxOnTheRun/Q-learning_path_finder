# All things evironment related

from random import random

# State class
class State:
	def __init__(self, row, column, reward, colour):
		self.row = row
		self.column = column
		self.position = (column, row)

		self.reward = reward
		self.colour = colour

		self.leftEdge = 0 # These get changed later on
		self.topEdge = 0
		self.width = 0
		self.height = 0


# Finder cell
class FinderCell:
	def __init__(self, startingPosition):
		self.position = startingPosition
		self.colour = (255, 0, 0)

		self.startingPosition = startingPosition


# Create reward list
def createRewardList(columns, rows, colour):

	rewardList = [
		[(0, columns-1), -100, colour.RED],
		[(rows-1, 0), -100, colour.RED],
		[(rows-1, columns-1), 100, colour.GREEN]
	]

	# rewardList = [[(3, 0), 100, colour.GREEN],
	# 			  [(3, 1), -200, colour.RED]]

	# rewardList = [
	# 	[(2, 2), -100, colour.RED],
	# 	[(2, 0), -100, colour.RED],
	# 	[(6, 2), -100, colour.RED],
	# 	[(6, 4), -100, colour.RED],
	# 	[(columns-1, rows-1), 100, colour.GREEN]
	# ]

	return rewardList


# Create list of random blocks on the grid
def createRandomBlockList(columns, rows, colour, blocks, rewardList):
	# Set up warning if too many blocks are entered
	if ((rows * columns) - len(rewardList)) < blocks:
		print('WARNING: TOO MANY BLOCKS CHOSEN')

	# Randomly create block list
	blockList = list()

	while len(blockList) < blocks:
		blockPosition = (int(random() * columns), int(random() * rows))
		blockList.append(blockPosition)

		# Stop block going over spawn point
		if blockPosition == (0, 0):
			blockList.remove(blockPosition)

		# Stop block going over reward cell
		for rewardCell in rewardList:
			if blockPosition == rewardCell[0]:
				blockList.remove(blockPosition)

		# Stop block overlaying each other
		for existingBlock in blockList[:-2]:
			if blockPosition == existingBlock:
				blockList.remove(blockPosition)

	return blockList


def createBlockList():

	blockList = [(1, 1)]

	return blockList


# Create stateList
def createStateList(columns, rows, edgeMargin, WINDOWHEIGHT, WINDOWWIDTH, colour, rewardList, blockList):
	stateList = list()

	for column in range(columns):
		stateList.append(list())

		for row in range(rows):
			stateList[column].append(State(column, row, -1, colour.WHITE))

			# Sort out cell sizes and window positions
			cell = stateList[column][row]

			cell.height = (WINDOWHEIGHT - (2*edgeMargin)) / rows
			cell.width = (WINDOWWIDTH - (2*edgeMargin)) / columns

			cell.leftEdge = edgeMargin + (column * cell.width)
			cell.topEdge = edgeMargin + (row * cell.height)

	# Set up reward cells
	for cell in rewardList:
		stateList[cell[0][0]][cell[0][1]].reward = cell[1]
		stateList[cell[0][0]][cell[0][1]].colour = cell[2]

	# Set up block cells
	for block in blockList:
		stateList[block[0]][block[1]].colour = colour.BLACK

	return stateList


# Update cell colour
def updateCellColour(finderCell, actions, columns, rows, stateList, rewardList, Q):
	newColour = 0

	for action in range(actions):
		newColour += (100 - Q[finderCell.position[0]][finderCell.position[1]][action]) * 2.55 / actions

	newColour = int(newColour)

	# If newColour < colour in green, else in red

	if newColour <= 255:
		stateList[finderCell.position[0]][finderCell.position[1]].colour = (newColour, 255, newColour)
	else:
		newColour = 510 - newColour
		stateList[finderCell.position[0]][finderCell.position[1]].colour = (255, newColour, newColour)

	# Keeps reward cells properly coloured
	for rewardCell in rewardList:
		if finderCell.position == rewardCell[0]:
			stateList[rewardCell[0][0]][rewardCell[0][1]].colour = rewardCell[2]

	return stateList
