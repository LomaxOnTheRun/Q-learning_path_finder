# Q-learning_path_finder

## Requirements

- Python (2.7 or 3.x)
- Pygame

## Overview

The agent will always start on the same place, takes steps until it hits a termination square (positive or negative), where it will start over again. As the agent learns internal values for non-termination squares, these internal values will be reflected in the colour of the squares.

### Squares:
- Blue (agent)
- Green (positive termination)
- Red (negative termination)
- Black (block, can't move into)
- White (free square, can move through)

### Variables:
- rows
  - Number of rows in maze
- columns
  - Number of columns in maze
- blocks
  - Number of randomly placed blocks
  - **NOTE:** These *can* make the maze unsolvable, so if this happens, just rerun the program
- step_reward
  - Penalty for taking each step
  - This encourages agent to find most direct path
- greediness
  - Between 0.0 and 1.0
  - The higher it is, the more likely it is to pick the best step instead of a random step
- speed
  - Number of steps taken per second
