'''
try: Runs the risky code that might cause an error.
except: Catches and handles the error if one occurs.
else: Executes only if no exception occurs in try.
finally: Runs regardless of what happens useful for cleanup tasks like closing files.
'''

try:
    n = 0
    ans = 10 / n

except ZeroDivisionError:
    print("Cannot possible divide by zero")
except ValueError:
    print("Enter a valid number!")
else:
    print("Division is", ans)
    
finally:
    print("Execution complete.")