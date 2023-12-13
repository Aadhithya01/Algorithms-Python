"""
This code is mainly about Left Truncatable prime and Right Truncatable prime. Where  
"""

# Function to generate a boolean list representing prime numbers up to 'num'
def sieve(num):
    # Initialize a boolean list with all elements set to True
    l = [True for i in range(num + 1)]
    # 0 and 1 are not prime numbers
    l[0], l[1] = False, False
    p = 2

    # Iterate through numbers up to the square root of 'num'
    while p * p <= (num - 1):
        # If 'p' is marked as prime, mark its multiples as not prime
        if l[p] == True:
            for i in range(p * p, num + 1, p):
                l[i] = False
        p += 1
    return l

# Function to check if a number is left truncatable prime
def l_prime(l, num):
    res = []
    s = len(str(num)) - 1
    res.append(num)

    # Generate left truncations of the number
    while num > 0 and s > 0:
        temp = 10 ** s
        num = num % temp
        res.append(num)
        s -= 1

    # Check if all left truncations are prime
    flag = 1
    for i in res:
        if l[i] == False:
            flag = 0
    return True if flag == 1 else False

# Function to check if a number is right truncatable prime
def r_prime(l, num):
    res = []
    s, r = len(str(num)) - 1, 0

    # Generate right truncations of the number
    while num > 0 and s >= r:
        temp = 10 ** r
        temp1 = num // temp
        res.append(temp1)
        r += 1

    # Check if all right truncations are prime
    flag = 1
    for i in res:
        if l[i] == False:
            flag = 0
    return True if flag == 1 else False

# Example usage
num = 293
# Generate the sieve of Eratosthenes up to 'num'
l = sieve(num)
# Check if 'num' is both left and right truncatable prime
print("Left Truncatable Prime:", l_prime(l, num))
print("Right Truncatable Prime:", r_prime(l, num))
