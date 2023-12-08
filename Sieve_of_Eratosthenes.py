# The Sieve of Eratosthenes is an elegant and efficient algorithm for finding all prime numbers less than or equal to a given number.
def sieve_of_eratosthenes(n):
    """
    This function implements the Sieve of Eratosthenes algorithm to find all prime numbers less than or equal to a given number "n".

    Args:
        n: An integer representing the upper limit for prime number search.

    Returns:
        None
    """
    l = [True for i in range(n+1)]
    # Initialize an array "l" of size n+1 with all elements True.
    # This array will be used to track prime numbers.

    l[0] = False
    l[1] = False
    # Mark 0 and 1 as non-prime, as they are not considered prime numbers.

    p = 2
    # Initialize the variable "p" to start iterating from 2 (first prime number).

    while(p*p < n-1):
        # Loop until p^2 becomes greater than n-1.
        # This ensures we only mark multiples of primes less than or equal to the square root of n.

        if(l[p] == True):
            # If the current number "p" is marked as prime:
            # Mark all its multiples (p*2, p*3, p*4, ...) as non-prime in the array "l".
            for i in range(p*p,n+1,p):
                l[i] = False
        p += 1
    # After the loop finishes, all remaining elements marked as True in the "l" array represent prime numbers.

    for i in range(len(l)):
        # Iterate through the "l" array and print all elements marked as True (prime numbers).
        if(l[i]):
            print(i, end=" ")

sieve_of_eratosthenes(23)
"""
The Time complexity drastically varies from normal aproach 
Time complexity of sieve of eratosthenes : O(n*log(log(n)))
Time complexity of normal approach : O(n^2)
"""