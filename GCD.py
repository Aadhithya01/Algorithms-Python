"""
The greatest common divisor (GCD) of two or more numbers is the greatest common factor number that divides them, exactly.
It is also called the highest common factor (HCF).

20/10 = 2

10/10 = 1

If a and b are two numbers then the greatest common divisor of both the numbers is denoted by gcd(a, b).
To find the gcd of numbers, we need to list all the factors of the numbers and find the largest common factor.

Suppose, 4, 8 and 16 are three numbers. Then the factors of 4, 8 and 16 are:

4 → 1,2,4

8 → 1,2,4,8

16 → 1,2,4,8,16

Therefore, we can conclude that 4 is the highest common factor among all three numbers.
"""

def gcd(a,b):
    if(a == 0):
        return b
    return gcd(b%a,a)

# This above code can be used to find the GCD of 2 numbers if GCD of multiple numbers needs to be found then this can be modified.

def multipleGCD(*nums):
    # *nums is arguement unpacking where the number of arguements need not be specified
    if(len(nums) < 2 ):
        print("Not possible to find a GCD with less than 2 numbers")
    else:
        result = nums[0]
        for i in nums[1:]:
            result = gcd(result,i)
        print(result)

multipleGCD(20,30,4,23)