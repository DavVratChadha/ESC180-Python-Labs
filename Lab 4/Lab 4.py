import math

#Problem 1
def sum_nums(L):
    """Calculate the sum of all the numbers in the list"""
    s = 0
    for num in L:
        s += num
    return s

def count_evens(L):
    """Count the number of even integers in the list"""
    count = 0
    for i in L:
        if i % 2 == 0:
            count += 1
    return count

#Problem 2
def list_to_str(lis):
    """Convert list into string"""
    string_lis = "[" #Beginning of list to be returned
    for index in range(len(lis)):
        string_lis += str(lis[index]) #string concatination
        if index == (len(lis) - 1): #If we have concatenated the last item in the list
            string_lis += "]"
        else: #If there are more items
            string_lis += ", "
    return string_lis

#Problem 3
def lists_are_the_same(list1, list2):
    """Check if the two lists are same or not"""
    if len(list1) == len(list2):#If the lenght is not same,\
    #it will go to the else statement and return False\
    #because lists are different
        for i in range(len(list1)):#checking indiviual items
            if list1[i] != list2[i]:
                return False
        return True #If all items are same, for loop will\
        #complete and True is returned
    else: #if the lengths are different
        return False

#Problem 4
def simplify_fraction(n, m): #n/m
    """Return fraction n/m in simplified form"""
    sign = "" #"-" if the final answer is negative

    #Assigning sign for final answer
    if (n < 0 and m < 0) or (n > 0 and m > 0):
        sign = "" #positive
    else:
        sign = "-"
    n = abs(n)
    m = abs(m)

    if m == 0:
        print("ERROR! Division by zero DNE\n")
        return "ERROR"
    elif n == m: #If numbers are same
        print(sign + "1/1" + " is the simplest form.\n")
        return 1 #Number of steps

    smaller_num = min(n,m)
    steps = 0
    for i in range(smaller_num,1,-1):#descending order
        steps += 1
        if n % i == 0 and m % i == 0: #Highest Common Factor
            n = int(n/i)
            m = int(m/i)
            print(sign + str(n) + "/" + str(m) + " is the simplest form.\n")
            return steps #Number of steps
    print(sign + str(n) + "/" + str(m) + " is already the simplest form.\n")
    return 1

#Problem 5
def pi_from_Leibniz_formula(n):
    """Return an approximate value of Pi/4"""
    result = 0 #Local variable
    for i in range(n+1):
        result += ((-1)**i)/(2*i + 1)
    val_of_pi = result*4 #result = pi/4
    return val_of_pi


def pi_equator(n): #n refers to the number of sig digits
    """Return number of terms for Leibniz formula to approximate Pi to n significant digits"""
    k = 1 #number of terms for Leibniz formula
    m_pi = math.pi
    while True:
        lf_pi = pi_from_Leibniz_formula(k)
        if int(lf_pi*10**(n-1)) == int(m_pi*10**(n-1)):
            #Note: (n-1) because 10^(1-1) = 1 which would\
            #check the first digit of pi's.
            return k
        k += 1

#Problem 6
def Euclid_algo(n,m):
    """Calculate the GCD and number of steps to get n/m in simplified form via Eulid's Algorithm"""
    sign = "" #"-" if the final answer is negative
    if m == 0:
        print("ERROR! Division by zero DNE\n")
        return "ERROR"

    #Assigning sign for final answer
    if (n < 0 and m < 0) or (n > 0 and m > 0):
        sign = "" #positive
    else:
        sign = "-" #negative
    n = abs(n)
    m = abs(m)
    a = max(n,m) #larger number
    b = min(n,m) #smaller number

    step = 0
    while a >= b and b != 0:
        rem = a % b #remainder
        a,b = b,rem #Euclid's algorithm
        step += 1
    print("GCD is " + str(a) + "\n")
    print(sign + str(int(n/a)) + "/" + str(int(m/a)) + " is the simplest form calculated via Euclid Algorithm.\n")
    print("Number of Steps = " + str(step))
    return step

def check_steps(n,m):
    """Compare the number of steps taken by Euclid_algo() and simplify_fraction()"""
    ea_steps = Euclid_algo(n,m) #Euclid's Algorithm,
    nm_steps = simplify_fraction(n,m) #NM = Naive Method = simplify_fraction
    if ea_steps == "ERROR" or nm_steps == "ERROR":
        return #To end the computaion
    diff = nm_steps - ea_steps
    if diff > 0:
        print("Naive method takes " + str(diff) + " more steps than Euclid's Algorithm\n")
    elif diff < 0:
        print("Naive method takes " + str(-diff) + " less steps than Euclid's Algorithm\n")
    else: #diff == 0
        print("Both, Naive method and Euclid's Algorithm take equal number of steps = " + str(nm_steps) + "\n")

if __name__ == "__main__":
    L=[-1, -2, -3, -4, -5, -6]
    print(sum_nums(L))
    print(count_evens(L))
    print()

    L1 = ["a", 2, 7, "c"]
    L2 = ["a", 2, 7, "c"]
    print(list_to_str(L1) + "\n")

    L3 = [True, False, False, True, True]
    L4 = [True, False, False, False, True]
    print(lists_are_the_same(L1,L2))
    print(lists_are_the_same(L3,L4))
    print()

    simplify_fraction(-12,36)
    simplify_fraction(-3,5)

    n = 2
    k = pi_equator(n)
    print("k = " + str(k) + " terms are required to compute value of Pi correct to " + str(n) + " significant figures.\n")

    Euclid_algo(2322,654)
    check_steps(24,24)