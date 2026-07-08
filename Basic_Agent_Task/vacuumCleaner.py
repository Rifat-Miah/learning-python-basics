'''In this task, you have to design and implement an intelligent Vacuum Cleaning Agent using fundamental principles of Artificial Intelligence. 
The agent should operate in a simple two-dimensional environment (such as a grid-based world) where each cell can either be clean or dirty. 
The agent must be capable of navigating through the environment and cleaning the dirty cells efficiently. 
You must program the agent to perceive its current location's status (clean or dirty), decide its next action (move left, right, up, down, or clean), and execute the action accordingly. 
The agent should use a simple rule-based approach. Do the implementation using Python.'''


# Agent Actions
'''Suck → Clean the current position.
   Right → Move from A to B.
   Left → Move from B to A.'''
'''
def vacuum_agent(location, status):
    if status.lower() == "dirty":
        return "Stuck"
    elif location.upper() == "A":
        return "Move Right"
    elif location.upper() == "B":
        return "Move Left"
    else:
        return "Invalid Input"
print("Location A, Dirty: ", vacuum_agent("A", "Dirty"))
print("Location A, Clean: ", vacuum_agent("A", "CLean"))
print("Location B, Dirty: ", vacuum_agent("B", "Dirty"))
print("Location B, Clean: ", vacuum_agent("B", "Clean"))
'''

# reflex Vacuum Agent (2D grid) : my task required
'''2D Grid
   (0, 0) (0, 1)
   (1, 0) (1, 1)
'''
def vacuum_agent(location, status):
    if status.lower() == "dirty":
        return "Clean"
    elif location == (0, 0):
        return "Move Right"
    elif location == (0, 1):
        return "Move Down"
    elif location == (1, 1):
        return "Move Left"
    elif location == (1, 0):
        return "Move Up"
    else:
        return "Stop"
print(vacuum_agent((0, 0), "Dirty"))
print(vacuum_agent((0, 0), "Clean"))
print(vacuum_agent((0, 1), "Dirty"))
print(vacuum_agent((0, 1), "Clean"))
print(vacuum_agent((1, 1), "Dirty"))
print(vacuum_agent((1, 1), "Clean"))
print(vacuum_agent((1, 0), "Dirty"))
print(vacuum_agent((1, 0), "Clean"))