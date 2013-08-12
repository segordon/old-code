
from math import sqrt

n = 600851475143 # Number to compute

def main(n): #our factoring algorithm from Euler Project #3
    return set(x for gen in ([i, n//i]
        for i in range(1, int(sqrt(n))+1) if n % i == 0) for x in gen)

#our timer is below. It begins timing and calls our main function
#it then displays the output of main, and the time it took

if __name__ == "__main__":
    import time
    tStart = time.time()
    print(main(n))
    print("Run time = " + str(time.time() - tStart))

