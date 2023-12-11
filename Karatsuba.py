def karatsuba(a, b):
    """
    Karatsuba Algorithm for Multiplication

    This algorithm is a fast multiplication algorithm discovered by Anatolii Alexeevitch Karatsuba in 1960.
    It's a divide-and-conquer approach that improves the efficiency of multiplying large numbers by
    reducing the number of recursive multiplications.

    Args:
        a (int): First number to be multiplied.
        b (int): Second number to be multiplied.

    Returns:
        int: The product of the two input numbers.
    """
    # Find the maximum number of digits in a and b
    n = max(len(str(a)), len(str(b)))

    # Base case: if the number has only one digit, perform regular multiplication
    if n < 2:
        return a * b

    # Split the numbers into high-order and low-order halves
    if n % 2 == 0:
        a_high, a_low = divmod(a, 10 ** (n // 2))
        b_high, b_low = divmod(b, 10 ** (n // 2))
    else:
        a_high, a_low = divmod(a, 10 ** ((n - 1) // 2))
        b_high, b_low = divmod(b, 10 ** ((n - 1) // 2))

    # Recursively calculate three products
    p1 = karatsuba(a_high, b_high)
    p2 = karatsuba(a_low, b_low)
    p3 = karatsuba((a_high + a_low), (b_high + b_low))

    # Combine results using the Karatsuba formula
    result = p1 * 10 ** (2 * (n // 2)) + (p3 - p2 - p1) * 10 ** (n // 2) + p2

    return result


# Example usage and output
result = karatsuba(1234, 5678)
print("Karatsuba Result:", result)

"""
The Karatsuba algorithm has a time complexity of approximately O(n^(log2(3))), which is more efficient 
than the regular multiplication algorithm (O(n^2)) for large numbers. This is due to the reduction in the 
number of recursive multiplications from four to three.
"""
