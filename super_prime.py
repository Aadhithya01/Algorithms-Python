"""
Super-prime numbers (also known as higher order primes) are the subsequence of prime numbers that occupy prime-numbered
positions within the sequence of all prime numbers. First few Super-Primes are 3, 5, 11 and 17.
"""

def sieve_of_eratosthenes(num):
    """
    Implement the Sieve of Eratosthenes algorithm to find prime numbers up to a given limit.

    Parameters:
    - num (int): The upper limit for finding prime numbers.

    Returns:
    - Tuple[List[bool], List[int]]: A tuple containing a boolean list representing prime status and a list of prime numbers.
    """
    # Create a boolean list 'l' initialized with True for numbers from 0 to 'num'
    l = [True for i in range(num + 1)]

    # Mark 0 and 1 as not prime
    l[0], l[1] = False, False

    # Iterate through numbers up to the square root of 'num'
    p = 2
    while p * p <= num:
        # Mark multiples of the current prime 'p' as not prime
        for i in range(p * p, num + 1, p):
            if l[i] == True:
                l[i] = False
        p += 1

    # Create a list 'res' containing prime numbers
    res = [i for i in range(len(l)) if l[i] == True]
    return l, res

def superprime(l, res):
    """
    Find superprime numbers based on prime numbers obtained from the Sieve of Eratosthenes.

    Parameters:
    - l (List[bool]): Boolean list representing prime status.
    - res (List[int]): List of prime numbers.

    Returns:
    - List[int]: List of superprime numbers.
    """
    # Create a list 'r' containing superprime numbers
    r = [res[i - 1] for i in range(1, len(res) + 1) if l[i] == True]
    return r

# Perform Sieve of Eratosthenes up to 241
l, res = sieve_of_eratosthenes(241)

# Find and print superprime numbers
print(superprime(l, res))
