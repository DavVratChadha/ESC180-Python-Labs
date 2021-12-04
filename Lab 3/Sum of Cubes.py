#Problem 2

def sum_of_cubes(n):
    """returns sum of cube of the first n numbers"""
    sum = 0
    for i in range(1,n+1):
        sum += i**3
    return sum #returns int value

def sum_of_cubes2(n):
    """returns sum of cube of the first n numbers"""
    value = (n*(n+1)/2)**2
    return value #return float

def check_sum(n):
    res = sum_of_cubes(n)
    res2 = sum_of_cubes2(n)
    if res == res2:
        return True
    else:
        return False

def check_sums_up_to_n(N):
    for n in range(1,N+1):#N+1 because we need to check for every integer from 1 to N (both inclusive)
        flag = check_sum(n)
        if flag != True:
            return False #False is returned if the results from the two functions dont match, and the process of checking for this N will come to an end
    return True

if __name__ == "__main__":
    print(check_sums_up_to_n(14000))
