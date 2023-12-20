"""
Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits.
"""

def Narcissistic(num):
    # Save the original number in a temporary variable
    temp = num

    # Calculate the number of digits in the given number
    l = len(str(num))

    # Initialize the sum of digits raised to the power of the number of digits
    s = 0

    # Loop through each digit of the number
    while(num > 0):
        # Add the current digit raised to the power of the number of digits to the sum
        s += pow(num % 10, l)

        # Move to the next digit
        num //= 10

    # Check if the original number is equal to the calculated sum
    return True if temp == s else False

"""
Rather than converting the number to string and measuring the length, we can use the following function using recursion.

def length(num):
    if num == 0:
        return 0
    else:
        return 1 + length(num // 10)
"""

print(Narcissistic(1634))
