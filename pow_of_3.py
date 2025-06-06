"""
Leetcode Q 326 -- Power of Three

I used an arbitrarily high power of 3 to determine if a given input is a power of 3.
My chosen power, was the value given at the upper bound.


Constraint:
    -2^31 <= n <= 2^31 - 1

Simplified Time Complexity: 
O(1) 
"""
def isPowerOfThree(n):
    if (pow(3,31) % n == 0):
        return True
    else:
        return False

def main():
    """Main Function"""
    
    n = 27
    output = isPowerOfThree(n)

    if output == False:
        print(n, 'is not a power of three!')
    else: 
        print(n, "is a power of three!")

if __name__ == "__main__":
    main()