"""
Leetcode Q 69 -- Sqrt(x).

You must NOT use any built-in exponent function or 
operator for this solution.

We are using an adjusted binary search.

Simplified Time Complexity:
O(n)

Constraints:
    0 <= x <= 231 - 1
"""
def mySqrt(x):
    # Check constraint 1: 
    if x < 0  or x > 230:
        print("Invalid input!")
        exit()

    # Init 2 variables 1 at 0, and the other at our target integer.
    left = 0
    right = x

    # We iterate through the numbers of 0 to our target number.
    while left <= right:
        # Calculate the middle value between left and right.
        mid = (left + right) // 2

        # We continue to perform this loop's operation until the mid val squared
        # equals our target integer. 
        if mid * mid == x:
            print(mid, 'Val we are looking for')
            return mid
        
        # If mid squared is less then our target integer, we know that the expected 
        # return value is greater than the middle value.
        elif mid * mid < x:
            left = mid + 1
        
        # If mid squared is greater then our target integer, we know that the expected 
        # return value is smaller than the middle value.
        else:
            right = mid - 1

def main():
    """Main Function"""

    x = 4
    output = mySqrt(x)
    print("The output from the above function is:", output)


if __name__ == "__main__":
    main()