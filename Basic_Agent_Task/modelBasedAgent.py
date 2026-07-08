'''If a mars lander finds a rock in a specific place it needed to collect, then it will collect the rock. 
If it finds the same rock in a different place it will not pick it up as it considers that it already picked it up. 
Make an intelligent agent of above features.'''

# agent logic:
'''
Collect the rock only if it is found at the required location.
Store the collected rock in memory.
If the same rock is found again, ignore it.
'''

class marssLanderAgent:
    def __init__(self):
        self.collected_rocks = []
    def collected_rock(self, rock_id, location, target_location):
        if rock_id in self.collected_rocks:
            return f"Rock {rock_id} already collected. Ignore!"
        if location == target_location:
            self.collected_rocks.append(rock_id)
            return f"Rock {rock_id} collected from {location}."
        
        return f"Rock {rock_id} not collected (wrong loaction)."
    
lander = marssLanderAgent()

print(lander.collected_rock("R1", "A", "A"))
print(lander.collected_rock("R1", "B", "A"))
print(lander.collected_rock("R2", "B", "A"))
print(lander.collected_rock("R2", "A", "A"))        
