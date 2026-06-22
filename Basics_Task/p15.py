# Implement stack  using list [Hints: The list methods make it is very easy  to use a list as a stack, where the last element retrieved ("last-in, first-out"). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index]

stack = []

stack.append("AIUB")
stack.append("CSE")
stack.append("AI")

print("\nInitial Stack = ", stack)

print("\nPopped item = ", stack.pop())
print("Popped item = ", stack.pop())

print("\nFinal Stack = ", stack)

print("Popped item = ", stack.pop())

print("\nFinal Stack = ", stack)