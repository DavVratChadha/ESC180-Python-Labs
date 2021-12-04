from numpy import *

#problem 1
def print_matrix(M_lol):
    print(array(M_lol))



#problem2
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i

    return len(row) #else


#problem3
def get_row_to_swap(M, start_i):
    L = []

    for i in range(start_i,len(M)):
        L.append(get_lead_ind(M[i]))

    min_value = min(L)
    return L.index(min_value) + start_i


#problem4
def add_rows_coefs(r1, c1, r2, c2):
    new_row = []
    for i in range(len(r1)):
        new_row.append(r1[i]*c1 + r2[i]*c2)
    return new_row


#problem5
def eliminate(M, row_to_sub, best_lead_ind):
    if M[row_to_sub][best_lead_ind] == 0:
        print("ERROR")
        return

    for i in range(row_to_sub+1,len(M)):
    # +1 becasue row_to_sub should not change, else error of div by 0
        c = M[i][best_lead_ind]/M[row_to_sub][best_lead_ind]
        for j in range(best_lead_ind, len(M[0])):
            M[i][j] -= c*M[row_to_sub][j]
    return M


#problem 6
def forward_step(M):
    print("The matrix is currently:")
    print_matrix(M)

    for row in range(len(M)):
        print("Now looking at row " + str(row))
        n_row = get_row_to_swap(M,row)

        #Swaping rows
        #if row != n_row:
        print("Swapping rows %d and %d so that entry %d in the current row is non-zero"%(row, n_row, get_lead_ind(M[n_row])))
        M[row], M[n_row] = M[n_row], M[row]
        print("The matrix is currently:")
        print_matrix(M)


        lead_ind = get_lead_ind(M[row])
        print("Adding row %d to rows below it to eliminate coefficients in column %d"%(row,lead_ind))
        eliminate(M,row,lead_ind)
        print("The matrix is currently:")
        print_matrix(M)
    print("""==================================""")


    print("Done with the forward step")
    print("The matrix is currently:")
    print_matrix(M)

    return M



#Problem 7
def backward_step(M):
    print("The matrix is currently:")
    print_matrix(M)
    print("==================================")
    print("Now performing the forward step")

    M = forward_step(M)
    if M == "END": #infinite many or no solution
        return

    print("==================================")
    print("Now performing the backward step")

    for row in range(len(M)-1,-1,-1):
        lead_ind = get_lead_ind(M[row])
        print("Adding row %d to rows above it to eliminate coefficients in column %d"%(row,lead_ind))
        backward_eliminate(M,row,lead_ind)
        print("The matrix is currently:")
        print_matrix(M)
        print("""==================================""")

    #Dividing leading coeffs
    print("Now dividing each row by the leading coefficient")
    for row in range(len(M)):
        c = M[row][get_lead_ind(M[row])]
        for column in range(len(M[row])):
            M[row][column] /= c

    print("The matrix is currently:")
    print_matrix(M)
    return M


def backward_eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub-1,-1,-1):
        c = M[i][best_lead_ind]/M[row_to_sub][best_lead_ind]
        for j in range(best_lead_ind, len(M[0])):
            M[i][j] -= c*M[row_to_sub][j]
    return M

#Problem 8
def solve(M,b):
    #Creating blank matrix A of form [M|b]
    A = []
    x = []

    for i in range(len(M)):
        A.append([0] * (len(M[0]) + 1))

    for row in range(len(A)):
        for column in range(len(A[row])-1):
            A[row][column] = M[row][column]
        A[row][-1] = b[row]

    #A = backward_step(A)
    A = direct_step(A)
    if A == "not unique":
        return

    for row in A:
        x.append(row[-1])
    print("\nx is: " + str(x))

    #testing
    tester(M,x,b)

    return x


def substep(M):
    sample = [0] * (len(M[0]) - 1)

    for row in M:
        row_list = []
        for i in range(len(row) - 1):
            row_list.append(row[i])
        if row_list == sample:
            if row[-1] == 0:
                print("System has Infinte many solutions!!")
            else:
                print("System has no solution!!")
            return "stop"
    return "continue"


def direct_step(M):
    print("The matrix is currently in [M|b] form:")
    print_matrix(M)

    for row in range(len(M)):
        n_row = get_row_to_swap(M,row)

        #Swaping rows
        M[row], M[n_row] = M[n_row], M[row]

        lead_ind = get_lead_ind(M[row])
        ans = substep(M)
        if ans != "continue":
            return "not unique" #no unique solution
        #else
        eliminate(M,row,lead_ind)


    for row in range(len(M)-1,-1,-1):
        lead_ind = get_lead_ind(M[row])
        backward_eliminate(M,row,lead_ind)

    #Dividing leading coeffs
    for row in range(len(M)):
        c = M[row][get_lead_ind(M[row])]
        for column in range(len(M[row])):
            M[row][column] /= c

    print("The matrix is currently in [R|d] form I.e. in RNF:")
    print_matrix(M)
    return M




def tester(M,x,b):
    if dot(M,x).tolist() == b: #array.tolist() converts array into a list
        print("\nTest PASSED")
    else:
        print("\nTest Failed")
    return


if __name__ == "__main__":

    #Problem 1
    print_matrix([[1,2,3],[1,2,3],[1,2,3]])

    #Problem 2
    get_lead_ind([0,0,0,1,2,3,4,5,6])
    get_lead_ind([0,0,0])

    #Problem 3
    M = [[5, 6, 7, 8],[0, 0, 0, 1],[1, 0, 5, 2],[0, 1, 0, 0]]
    print(get_row_to_swap(M,1))

    #Problem 4
    r1=[1,2,3]
    r2=[2,3,4]
    c1 = 1
    c2 = 2
    print(add_rows_coefs(r1, c1, r2, c2))

    #Problem 5
    M1 = [[5, 6, 7, 8],    #[[5, 6, 7, 8],
          [0, 0, 1, 1],    # [0, 0, 1, 1],
          [0, 0, 5, 2],    # [0, 0, 0, -3],
          [0, 0, 7, 0]]    # [0, 0, 0, -7]]
    print_matrix(eliminate(M1,1,2))

    M2 = [[5, 6, 7, 8],
    [0, 0, 1, 1],
    [0, 0, 0, 2],
    [0, 0, 7, 0]]
    print_matrix(eliminate(M2,1,2))

    M3 = [[5, 6, 7, 8],
    [0, 0, 0, 1],
    [0, 0, 0, 2],
    [0, 0, 7, 0]]
    print(eliminate(M3,1,2))

    #Problem 6
    M = [[0., 0., 1., 0., 2.],
        [1., 0., 2., 3., 4.],
        [3., 0., 4., 2., 1.],
        [1., 0., 1., 1., 2.]]
    forward_step(M)

    #Problem 7
    M = [[1, -2, 3, 22],
        [3, 10, 1, 314],
        [1, 5, 3, 92]]
    backward_step(M)

    #Problem 8
    # x - 2y = 1
    #3x + 2y = 11
    #solutin to this system: x = 3 & y = 1
    M = [[1, -2],
        [3, 2]]
    b = [1, 11]
    solve(M,b)

    # x - 2y = 1
    #2x - 4y = 2
    #Infinite solutins
    M = [[1, -2],
         [2, -4]]
    b = [1, 2]
    solve(M,b)

    # x - 2y = 1
    #2x - 4y = 3
    #No solutins
    M = [[1, -2],
         [2, -4]]
    b = [1, 3]
    solve(M,b)