#Lab 5

#Problem 1
def list1_start_with_list2(list1, list2):
    """Return True iff length of list1 >= length of list2 and first len(list2) elements in list1 are same as in list2"""
    if len(list1) < len(list2):
        return False
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            return False
    return True

#Problem 2
def match_pattern(list1, list2):
    """Return True if list1 contains the pattern list2 in it"""
    if len(list1) < len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] == list2[0]: #first element of list2 matches
            temp_list1 = list1[i:(i + len(list2))] #slicing list1
            if temp_list1 == list2:
                return True
    return False

#Problme 3
def repeats(list0):
    """Return True if an element in the list0 repeat immediately after itself"""
    for i in range(len(list0)-1): #because there is no element at list0[len(list0)]
        if list0[i] == list0[i + 1]:
            return True
    return False #else False

#Problem 4(a)
def print_matrix_dim(M):
    i = len(M) #length of row
    j = len(M[0]) #length of column
    for row in M:
        if len(row) != j: #If rows are of uneven lengths
            print("This is not a Matrix")
            return
    #else print
    print(str(i) + "x" + str(j))
    return

#Problem 4(b)
def mult_M_v(M, v):
    if len(M[0]) != len(v):
        return "Product cannot be calculated!"

    #else
    res_vector = list() #empty list
    for n in range(len(M)): #for each row
        row_sum = 0
        for m in range(len(M[n])): #element in that row
            row_sum += M[n][m] * v[m] #multiply with corres. element of v
        res_vector.append(row_sum)
    return res_vector

#Problem 4(c)
def mult_M_N(M, N):
    if len(M[0]) != len(N): #Matrix multiplication not possible
        return "Product cannot be calculated!"

    #else
    """res_matrix = list()
    row_list = list()
    for i in range(len(N[0])):
        row_list.append(0)
    for j in range(len(M)):
        res_matrix.append(row_list)
    print(res_matrix)"""
    #res_matrix = [[0,0],[0,0]]
    res_matrix = [[0]*len(N[0])]*len(M)
    print(res_matrix)
    #aXb and cXd, product dimensions are aXd
    for a in range(len(M)): #for each row of M
        for d in range(len(N[0])):#for each column of N
            for index in range(len(M[0])):#len(N)
                res_matrix[a][d] += M[a][index] * N[index][d]
    #res_matrix[a][d] = M[a][0]xN[0][d] + M[a][1]xN[1][d] +
    #                 + M[a][2]xN[2][d] + M[a][3]xN[3][d]
    return res_matrix
######
def dot_product(a, b):
    '''Return the dot product of the vectors a and b

    Arguments:
    a, b -- vectors represented as lists, which must be of the same length
    '''

    s = 0
    for i in range(len(a)):
        s += a[i]*b[i]

    return s


def mult_M_v1(M, v):
    '''Return the product Mv of the matrix M and the vector v.

    Arguments:
    M -- a matrix, represented as a list of lists, of size nxm
    v -- a vector, represented as a list, of size m
    '''

    prod = []
    for i in range(len(M)):
        prod.append(dot_product(M[i], v))

    return prod
############

if __name__ == "__main__":
    L1 = [2,3,4,5,6,7,8]
    L2 = [2,3,4]
    print(list1_start_with_list2(L1,L2)) #True
    L3 = [1,2,3]
    print(list1_start_with_list2(L2,L3)) #False

    L4 = [1,2,3,4,5,6,7,8]
    L5 = [4,5,6]
    print(match_pattern(L4,L5)) #True

    L6 = [1,2,3,4,4,5]
    print(repeats(L6))
    print(repeats(L4))

    M = [[5,  6, 7],
        [0, -3, 5]]
    print_matrix_dim(M)
    N = [[1,2],
        [3],
        [5,6]]
    print_matrix_dim(N)

    M = [[5,  6, 7],
        [0, -3, 5]]
    v = [-2,1,2]
    print(mult_M_v(M,v))
    print(mult_M_v1(M,v))

    M = [[2,3],
        [4,5]]

    N = [[1,0],
        [0,1]]
    print(mult_M_N(M, N))



"""
def match_pattern2(list1, list2):
    if len(list1) < len(list2):
        return False
    for j in range(len(list1)):
        if list1[j] == list2[0]: #i = 0
        #first element of list2 matches
            counter = 0
            for i in range(len(list2)):
                if list1[i + j] == list2[i]:
                    counter += 1
            if counter == len(list2):
                return True
    return False
"""