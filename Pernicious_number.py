"""
A pernicious number is a positive integer which has prime number of ones in its binary representation.
The first pernicious number is 3 since 3 = (11)(in binary representation) and 1 + 1 = 2, which is a prime.
"""

def sieve(limit):
    """
    Implement the Sieve of Eratosthenes algorithm to find prime numbers up to a given limit.

    Parameters:
    - limit (int): The upper limit for finding prime numbers.

    Returns:
    - List[bool]: A boolean list indicating whether each number up to the limit is prime or not.
    """
    # Create a boolean list 'l' initialized with True for numbers from 0 to 'limit'
    l = [True for i in range(limit + 1)]

    # Mark 0 and 1 as not prime
    l[0], l[1] = False, False

    # Start with the first prime number, 2
    p = 2

    # Iterate while the square of the current prime 'p' is less than the limit
    while p * p <= limit:
        # If 'p' is marked as prime
        if l[p] == True:
            # Mark multiples of 'p' as not prime
            for i in range(p * p, limit + 1, p):
                l[i] = False
        # Move to the next number
        p += 1

    return l

def pernicious_numbers(prime_flags, limit):
    """
    Find and print pernicious numbers up to a given limit.

    Parameters:
    - prime_flags (List[bool]): A list indicating whether each number is prime or not.
    - limit (int): The upper limit for finding pernicious numbers.
    """
    n = 2
    result_count = 0

    # Iterate through numbers up to the limit
    while n < limit:
        # Convert the number to binary and count the number of '1's
        binary_representation = str(bin(n).replace("0b", ""))
        count_ones = binary_representation.count("1")

        # If the count of '1's is prime, print the number
        if prime_flags[count_ones] == True:
            result_count += 1
            print(n, end=" ")

        n += 1

# Example usage
limit = 100
prime_flags = sieve(limit)
pernicious_numbers(prime_flags, limit)
