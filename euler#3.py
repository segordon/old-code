# Project Euler # 3
# The prime factors of 13195 are 5 , 7 , 13 and 29.
# What is the largest prime factor of the number 600851475143

def factors():
    return set(x for gen in ([i, 600851475143//i]
        for i in range(1, int(600851475143**0.5)+1) if 600851475143 % i == 0) for x in gen)
#Print the factors.
print(factors())