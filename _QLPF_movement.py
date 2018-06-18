# All things movement

from random import random

# Find the maximum value and its position from a list of numbers
def findMax(aList):
	maxValue = aList[0]
	maxPosition = 0

	for i in range(1, len(aList)):
		if aList[i] > maxValue:
			maxValue = aList[i]
			maxPosition = i

	return [maxValue, maxPosition]


# Define function for moving randomly
def randomMove(columns, rows, actions, finderCell):
	randomNo = random()

	if randomNo < 0.25: # North
		finderCell.position[1] -= 1
		action = 0
	elif randomNo < 0.5: # East
		finderCell.position[0] += 1
		action = 1
	elif randomNo < 0.75: # South
		finderCell.position[1] += 1
		action = 2
	else: # West
		finderCell.position[0] -= 1
		action = 3

	# Stop position from going off side of grid
	if finderCell.position[0] < 0:
		finderCell.position[0] = 0
	elif finderCell.position[0] >= columns:
		finderCell.position[0] = columns - 1

	if finderCell.position[1] < 0:
		finderCell.position[1] = 0
	elif finderCell.position[1] >= rows:
		finderCell.position[1] = rows - 1

	return [finderCell, action]


# Move the finder cell greedily
def greedyMovement(columns, rows, actions, greedyFactor, finderCell, blockList, Q):
	# Find the highest action Q-value
		# If other Q-values match the highest, randomly choose between them

	QActions = Q[finderCell.position[0]][finderCell.position[1]]
	[maxValue, maxAction] = findMax(QActions)

	maxActionList = list()
	otherActionList = list()

	for action in range(actions):
		if QActions[action] == maxValue:
			maxActionList.append(action)
			# I now have a list of all the highest actions...
		else:
			otherActionList.append(action)
			# ...and also a list of other actions

	randomNo = random()
	maxActions = len(maxActionList)
	otherActions = len(otherActionList)

	if (random() < (1.0 - greedyFactor)) and (otherActions > 0):
		# If not greedy and not all actions are equal
		for i in range(otherActions):
			if (float(i) / otherActions) <= randomNo < ((float(i) + 1) / otherActions):
				action = otherActionList[i]
				# Randomly chooses between 'other' actions
	else:
		# If greedy:
		for i in range(maxActions):
			if (float(i) / maxActions) <= randomNo < ((float(i) + 1) / maxActions):
					action = maxActionList[i]
					# Randomly chooses between best actions

	# Add possibility of sliding
		# There's a 0.8 chance of doing what you want, and 0.1 chance of sliding in either direction
	randomNo = random()

	if randomNo < 0.3:
		action -= 1
		if action == -1:
			action = 3
	elif randomNo < 0.6:
		action += 1
		if action == 4:
			action = 0

	# Actually move finder cell
	newPosition = [finderCell.position[0], finderCell.position[1]]

	if action == 0: # North
		newPosition[1] = finderCell.position[1] - 1
	elif action == 1: # East
		newPosition[0] = finderCell.position[0] + 1
	elif action == 2: # South
		newPosition[1] = finderCell.position[1] + 1
	elif action == 3: # West
		newPosition[0] = finderCell.position[0] - 1
	else:
		print('WARNING: ACTION NOT DETECTED')

	# Stop position from going off side of grid
	if (newPosition[0] < 0) or (newPosition[0] >= columns):
		newPosition[0] = finderCell.position[0]

	if (newPosition[1] < 0) or (newPosition[1] >= rows):
		newPosition[1] = finderCell.position[1]

	# Stop finder cell from going into block cell
	for block in blockList:
		if (newPosition[0], newPosition[1]) == block:
			newPosition[0] = finderCell.position[0]
			newPosition[1] = finderCell.position[1]

	# Update finder cell position
	finderCell.position = (newPosition[0], newPosition[1])

	return [finderCell, action]


def finishPointReached(run, runningTotal, score, finderCell):
	run += 1
	# print(run)
	finderCell.position = finderCell.startingPosition
	score.append(runningTotal)
	runningTotal = -1
	return [run, runningTotal, score, finderCell]
