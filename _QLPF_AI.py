# All things AI and learning

# Find the maximum value and its position from a list of numbers
def findMax(aList):
	maxValue = aList[0]
	maxPosition = 0

	for i in range(1, len(aList)):
		if aList[i] > maxValue:
			maxValue = aList[i]
			maxPosition = i

	return [maxValue, maxPosition]


# Initialise Q matrix
def initialiseQ(columns, rows, actions):
	Q = list()

	for column in range(columns):
		Q.append(list())

		for row in range(rows):
			Q[column].append(list())

			for action in range(actions):
				Q[column][row].append(0)

	return Q


# Update Q matrix
def updateQ(thisPosition, nextPosition, learningRate, discountFactor, action, stateList, Q, step_reward):
	# Design shorter names
	thisQ = Q[thisPosition[0]][thisPosition[1]][action]
	nextQ = Q[nextPosition[0]][nextPosition[1]]

	# Find maxQ
	[maxQ, maxAction] = findMax(nextQ)

	# Find nextReward
	nextReward = stateList[nextPosition[0]][nextPosition[1]].reward + step_reward

	# Calculate new Q value
	thisQ = thisQ + (learningRate * (nextReward + (discountFactor * maxQ) - thisQ))

	# Update Q matrix
	Q[thisPosition[0]][thisPosition[1]][action] = thisQ

	return Q
