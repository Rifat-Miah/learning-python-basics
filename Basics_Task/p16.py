# Impliment queue using list [Hints: It is also possible to use a list as a queue, where the first element added is the first element retrieved ("first-in, first-out")]

queue = []

queue.append("AIUB")
queue.append("CSE")
queue.append("AI")

print("\nInitail queue = ", queue)
print("Removed item: ", queue.pop(0))
print("Removed item: ", queue.pop(0))
print("Final queue = ", queue)



from collections import deque
queue = deque()
queue.append("IUB")
queue.append("IUB")
print("\nInitail queue = ", queue)
queue.popleft() # it works fast to the pop(0) 
print("Final queue = ", queue)