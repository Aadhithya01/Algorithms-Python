"""
Mersenne Prime is a prime number that is one less than a power of two.
In other words, any prime is Mersenne Prime if it is of the form 2^k-1 where k is an integer greater than or equal to 2.
First few Mersenne Primes are 3, 7, 31 and 127.
"""
# Sieve of Eratosthenes function to generate a list of prime numbers up to 'num'
def sieve(num):
    # Initialize a boolean list, assuming all numbers are prime initially
    l = [True for i in range(num + 1)]

    # Mark 0 and 1 as not prime
    l[0], l[1] = False, False

    p = 2
    # Iterate through numbers up to the square root of 'num'
    while p * p < num:
        # If 'p' is marked as prime, mark its multiples as not prime
        if l[p] == True:
            for i in range(p * p, num, p):
                l[i] = False
        p += 1

    return l


# Mersenne Prime generator function
def Mersenne(num, l):
    res = []
    k = 1
    # Check for Mersenne primes up to 'num'
    while (1 << k) - 1 <= num:
        n = (1 << k) - 1
        # If the corresponding Mersenne number is prime, add it to the result
        if l[n]:
            res.append(n)
        k += 1
    return res


# Example usage
limit = 100
# Generate the Sieve of Eratosthenes up to the limit
sieve_result = sieve(limit)
# Find and print Mersenne primes up to the limit
print(Mersenne(limit, sieve_result))
