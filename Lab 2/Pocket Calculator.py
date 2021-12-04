#Lab 2
#Calculator program

current_value = 0
memory_value = 0
prev_value = 0

#Problem 2
def display_current_value():
    print("Current value: " + str(current_value))

#Problem 3
def add(to_add):
    global current_value
    global prev_value
    prev_value = current_value
    current_value += to_add

def subtract(to_subtract):
    global current_value
    global prev_value
    prev_value = current_value
    current_value -= to_subtract

#Problem 4
#This is the error when currnet_value is not declared as global in the add function:
#UnboundLocalError: local variable 'current_value' referenced before assignment

#Problem 5
def multiply(to_multiply):
    global current_value
    global prev_value
    prev_value = current_value
    current_value *= to_multiply

def divide(to_divide):
    global current_value
    global prev_value
    prev_value = current_value
    current_value /= to_divide

#Problem 6
def memory():
    global memory_value
    memory_value = current_value

def recall():
    return memory_value

#Buttons that we have created to better our pocket calculator
def clear():
    global current_value
    global prev_value
    prev_value = current_value
    current_value = 0

def memory_clear():
    global memory_value
    memory_value = 0

#Problem 7
def undo():
    global current_value
    global prev_value
    #Multiple assignment to swap the values
    #Another method
    current_value, prev_value = prev_value, current_value

#Problem 1
if __name__ == "__main__":
    print("Welcome to the calculator program.")
    print("Current value: " + str(current_value))
    display_current_value() # 0
    add(5) # 5
    subtract(2)
    display_current_value() # 3
    undo()
    display_current_value() # 5
    undo()
    display_current_value() # 3
    multiply(10)
    display_current_value() # 30
    undo()
    undo()
    display_current_value() # 30
    undo()
    undo()
    undo()
    display_current_value()#3
    memory()#3 in memory
    clear()#0
    display_current_value()#0
    add(7)#7
    display_current_value()#7
    recall()
    undo()
    subtract(recall())#4
    display_current_value()#4
    multiply(recall())#12
    display_current_value()#12
    memory_clear()#0 in memory
    divide(120)#0.1
    display_current_value()#0.1
    multiply(20)#2
    display_current_value()#2
    add(3)#5
    display_current_value()#5
    undo()
    display_current_value()#2
    add(7)#9
    display_current_value()#9
    subtract(recall())#9
    display_current_value()#9
    memory()#9 in memory
    clear()#0
    display_current_value()#0
    add(recall())#9
    display_current_value()#9

"""
#(homework to swap values)
#way for int/float
a = 100
b = 70
a = a + b
b = a - b
a = a - b
print(a,b)

#way for string
c = "car"
d = "truck"
val1 = len(d)
val2 = len(c)
c = c + d
d = c[:val2]
c = c[-val1:]
print(c)
print(d)
"""