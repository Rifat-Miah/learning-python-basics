'''If the agent finds that there is no one in the room, it will turn off the lights and the fan. 
If any person is found in the room, the agent will check whether it is day or night. 
If night, it will turn on the light and fan both. If it is Day, then agent will turn on the fan only. 
Make an intelligem agent of above features.'''

# agent logic:
'''
    No person → Turn OFF light and fan.
    Person present + Night → Turn ON light and fan.
    Person present + Day → Turn ON fan only.
'''

def room_agent(person_present, time_of_day):
    if person_present == False:
        return "Light OFF, Fan OFF."
    elif time_of_day.lower() == "night":
        return "Light ON, Fan ON."
    elif time_of_day.lower() == "day":
        return "Light OFF, Fan ON."
    else:
        return "invalid Input."
    
print("No persion inside the room: ", room_agent(False, "Day"))
print("Night: person present inside the room: ", room_agent(True, "night"))
print("Day: person present inside the room: ", room_agent(True, "day"))