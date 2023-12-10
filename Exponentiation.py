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
