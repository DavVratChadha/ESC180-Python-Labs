#Problem 1

import lab02

if __name__ == '__main__':
    lab02.initialize()#assigning values to the variables
    lab02.add(42)
    if lab02.get_current_value() == 42:
      print("Test 1 passed")
    else:
      print("Test 1 failed")
    lab02.subtract(2)
    lab02.divide(4)
    if lab02.get_current_value() == 11:#Should print Test 2 failed because current_value == 10
      print("Test 2 passed")
    else:
      print("Test 2 failed")
    lab02.divide(0)
    if lab02.get_current_value() == "ERROR":
      print("Test 1 passed")
    else:
      print("Test 1 failed")
