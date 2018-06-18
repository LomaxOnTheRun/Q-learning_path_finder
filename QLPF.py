# Find path in grid world

from _QLPF_display import *
from _QLPF_environment import *
from _QLPF_movement import *
from _QLPF_AI import *
from _QLPF_analysis import *

from time import sleep

# Variables
rows = 5
columns = 5
actions = 4  # N, E, S, W

blocks = 5
step_reward = -5  # Penalise agent for taking too long

learningRate = 0.8  # Step size
discountFactor = 0.9
greedyFactor = 0.9

showAnimation = True
edgeMargin = 50
speed = 100



### MAIN CODE ###

# Create stateList
rewardList = createRewardList(columns, rows, colour)
blockList = createRandomBlockList(rows, columns, colour, blocks, rewardList)
# blockList = createBlockList()
stateList = createStateList(columns, rows, edgeMargin, WINDOWHEIGHT, WINDOWWIDTH, colour, rewardList, blockList)

# Initialise Q matrix
Q = initialiseQ(columns, rows, actions)

# Create finder cell
finderCell = FinderCell((0, 0))

# Draw coloured grid and finder cell
drawGrid(columns, rows, edgeMargin, stateList)
showFinderCell(finderCell, stateList)

# Keep a score total
run = 1
score = list()
runningTotal = 0

# Main loop #
while True:
	# Check for events
	for event in pygame.event.get():
		# Check if user tries to quit
		if event.type == QUIT:
			pygame.quit()

	# Draw grid
	if showAnimation == True:
		drawGrid(columns, rows, edgeMargin, stateList)

	# Record position
	oldPosition = (finderCell.position[0], finderCell.position[1])

	# Try a move
#	[finderCell, action] = randomMove(rows, columns, actions, finderCell)
	[finderCell, action] = greedyMovement(columns, rows, actions, greedyFactor, finderCell, blockList, Q)

	# Rerecord position
	newPosition = (finderCell.position[0], finderCell.position[1])

	# Show red cell
	if showAnimation == True:
		showFinderCell(finderCell, stateList)

	# Update Q
	updateQ(oldPosition, newPosition, learningRate, discountFactor, action, stateList, Q, step_reward)

	# Update colour of cell
	if showAnimation == True:
		stateList = updateCellColour(finderCell, actions, columns, rows, stateList, rewardList, Q)

	# Update display
	if showAnimation == True:
		pygame.display.update()

	# Slow the program down
	if showAnimation == True:
		sleep(1.0 / speed)

	# Reset if finish point is reached
	for cell in rewardList:
		if newPosition == cell[0]:
			[run, runningTotal, score, finderCell] = finishPointReached(run, runningTotal, score, finderCell)
			if run % 1000 == 0:
				plot(score)

	# Update running total
	runningTotal += 1
