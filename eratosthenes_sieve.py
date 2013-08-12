# Goal : Sieve of Eratosthenes implementation in Python3
#        (Efficient prime number generator to about 10-100million)
# PSEUDOCODE SKELETON
# Input: an integer n > 1
# 
# Let A be an array of Boolean values, indexed by integers 2 to n,
# initially all set to true.
# 
# for i = 2, 3, 4, ..., √n :
#   if A[i] is true:
#     for j = i2, i2+i, i2+2i, ..., n:
#       A[j] := false
# 
# Now all i such that A[i] is true are prime.

largerthan1 = 0

while largerthan1 == 0:
    n_str = input("Type a number larger than 1.\n")
    n = int(n_str)

    if n > 1:
        largerthan1 = largerthan1 + 1

    else:
        print("LARGER than 1..")
