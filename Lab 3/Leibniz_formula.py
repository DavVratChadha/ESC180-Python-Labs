# Leibniz formula for computing the value of Pi
#Problem 3

def Leibniz_formula(n):
    """This def function gives an approximate value of Pi/4"""
    result = 0 #Local variable
    for i in range(n+1):
        result += ((-1)**i)/(2*i + 1)
    return result


if __name__ == "__main__":
    res = Leibniz_formula(1000) #Pi/4
    val_of_pi = res * 4 #Pi
    print(val_of_pi) #Pi