"""
Leetcode Q 231 -- Power of Two.

Simplified Time Complexity:
O(log n)

Constraints:
    -231 <= n <= 231 - 1
 

Follow up:  
    Could you solve it without loops/recursion?

Got my iterative solution from here: 
    https://leetcode.com/problems/power-of-two/solutions/6116153/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step/

"""

def powerOfTwo(n):
    """
    Solves the problem recursively.
    """
    # Check Constraint 1: 
    if n < -231 or n > 230:
        print("Invalid input!")
        exit()

    # Base Cases 
    if n <= 0: 
        return False 
    
    if n == 1: 
        return True 
    

    return (n % 2 == 0) and powerOfTwo(n // 2) 


def pow2(n):
    """
    Solves the problem iteratively.
    """
    # Check Constraint 1: 
    if n < -231 or n > 230:
        print("Invalid input!")
        exit()

    if (n <= 0):
        return False 
    
    while (n % 2 == 0):
        n = n/2

    if (n == 1):
        return True
    else:
        return False


def main():
    """Main Function"""

    n = 1 
    output = powerOfTwo(n)
    if output == True:
        print("The given integer is a power of 2!")
    else:
        print("The given integer is not a power of 2!")


if __name__ == '__main__':
    main()