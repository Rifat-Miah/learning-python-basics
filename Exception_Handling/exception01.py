import logging

values = [66, 33, 76, 95, 0, 2, -3, "Rifat"]

for value in values:
    try:
        print(101 / int(value))
    except ValueError as v:
        print("Value Error!")
    except ZeroDivisionError as z:
        print("Zero division error!")
    except Exception as e:   # attribute error
        logging.exception(e)

