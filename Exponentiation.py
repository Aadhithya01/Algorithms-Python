"""
Exponentiation is a mathematical operation that involves repeatedly multiplying a base number by itself a certain number of times, known as the exponent. 
In this script, we explore two methods for exponentiation: the normal exponentiation operator and an optimized function using a technique known as "fast exponentiation" 
or "exponentiation by squaring."

1. Normal Exponentiation Operator:
   The normal exponentiation operator, denoted as '**' in Python, performs exponentiation in a straightforward manner. 
   However, its time complexity is O(n), where n is the exponent. This is due to the direct multiplication of the base number by itself n times.

2. Fast Exponentiation Function:
   The 'power' function in this script utilizes a recursive approach based on the fast exponentiation algorithm. 
   This algorithm significantly reduces the number of required multiplications by dividing the exponent in half at each step. 
   Consequently, its time complexity is O(log n), where n is the exponent. The recursive nature of the algorithm creates a binary tree structure, making it more efficient than the normal exponentiation operator for large exponents.

"""

def power(a, n):
    # Base case: anything to the power of 0 is 1
    if n == 0:
        return 1
    # Base case: anything to the power of 1 is itself
    elif n == 1:
        return a
    else:
        # Recursively calculate the result for the exponent divided by 2
        res = power(a, n // 2)

        # If the exponent is even, square the result
        if n % 2 == 0:
            return res * res
        # If the exponent is odd, multiply the result by the base and then square it
        else:
            return res * a * res


# Example usage
result = power(4, 15)
print(result)

