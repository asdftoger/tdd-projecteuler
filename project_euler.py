# %%
import math
#%%
def sum_natural_multiples(n: int, mults: list[int]):
    acc = 0
    for i in range(n+1):
        for mult in mults:
            if i % mult == 0:
                acc += i
                break
    return acc


def fib_even_sum(n_max):
    a, b = 1, 2
    n_sum = 0
    while b < n_max:
        a, b = b, a+b
        if a % 2 == 0:
            n_sum += a
    return n_sum


def largest_prime_factor(n):
    prime_factors=[]
    for i in range(2,math.ceil(math.sqrt(n))):
        if n % i ==0: 
            for j in prime_factors:
                if i%j==0:
                    break
            else:
                prime_factors.append(i)
    
    #Empty list
    return prime_factors[-1] if prime_factors else n

def is_prime(n):
    for i in range(2,int(n/2)+1):
        if n % i ==0: 
            return False

    return True


# %%
