'''A door agent, if any person is found within 1 meter, this agent will open the door. 
Otherwise, it will close the door automatically. 
The agent will check which side the person is standing on and it will always open the door on the opposite side of the person. 
Make an intelligent agent of above features.'''

# Agent Logic:
'''
    If a person is within 1 meter, open the door.
    If the person is on the left, open the right door.
    If the person is on the right, open the left door.
    Otherwise, close the door.
'''

door_table = {
    ("left", True): "Open Right Door.",
    ("right", True): "Open Left Door.",
    ("left", False): "Close Door.",
    ("right", False): "Close Door.",
    ("none", False): "Close Door."
}

def door_agent(person_side, within_1m):
    action = door_table.get((person_side.lower(), within_1m), "Close Door")
    return action

print(door_agent("left", True))
print(door_agent("right", True))
print(door_agent("left", False))
print(door_agent("right", False))
print(door_agent("none", False))