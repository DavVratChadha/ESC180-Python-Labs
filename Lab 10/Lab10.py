#Problem 1
def power(x,n):
    if n == 0: #base case
        return 1
    res = x*power(x,n-1)
    return res

#Problem 2
def interleave(L1, L2):
    L = []
    if len(L1) == 0: #base case
        return []
    if len(L1) == 1: #base case
        return [L1[0],L2[0]]

    #List concatination
    L.extend([L1[0],L2[0]])
    L.extend(interleave(L1[1:],L2[1:]))
    return L

#Problem 3
def reverse_rec(L):
    return helper_fcn(L,-1)

def helper_fcn(L,n):
    if n == len(L)*-1: #base case
        return [L[0]]

    res_L = []
    res_L.append(L[n])
    res_L.extend(helper_fcn(L, n-1))
    return res_L

#Problem 4
def zigzag(L):
    #base cases
    if len(L) == 0:
        print("")
    elif len(L) == 1:
        print(L[0], end = " ")
    else:
        print(L[len(L)//2], L[len(L)//2-1], end = " ")
        L.remove(L[len(L)//2])
        L.remove(L[len(L)//2-1])
        zigzag(L)

#Problem 5
def is_balanced(s):
    #t = deleter(s)
    return helper_fcn2(s,0,0)


# def deleter(s):
#     seq = "abcdefghijklmnopqrstuvwxyz1234567890 "
#     if len(s) > 0 and s[0] in seq:
#         t = s.replace(s[0], "")
#         return deleter(t)
#     return s

def helper_fcn2(s,n_l, n_r):
    if len(s) == 0:
        return n_l == n_r


    if s[0] == "(":
        n_l += 1
    elif s[0] == ")":
        n_r += 1
    if n_l < n_r:
        return False

    s = s[1:]
    return helper_fcn2(s, n_l, n_r)
    # n_l += y[0]
    # n_r += y[1]
    # if n_r > n_l:
    #     return False, False
    # return n_l, n_r

if __name__ == "__main__":
    print(power(3,5))#243
    print(power(0,0))#1

    L1 = [1,2,3]
    L2 = [7,8,9]
    print(interleave(L1, L2))
    print(interleave(L1, L1))

    print(reverse_rec(L1))

    L3 = ["a","b","c","d","e","f","g","h","i"]
    zigzag(L3)

    s = "(well (I think), recursion works like that (as far as I know)"
    print("\n" + str(is_balanced(s)))

    s = ""
    print("\n" + str(is_balanced(s)))

#
# def help(L,n):
#     if n == L//2:
#         return L
#     L[i], L[-1-i] = L[-1-i], L[i]
#     return help(L,n+1)
#s = "(well (I think), recursion works like that (as far as I know)"