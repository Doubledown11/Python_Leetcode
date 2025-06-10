"""
Leetcode Q 263 -- Ugly Number.

Simplified Time Complexity: 
O(n)

Constraints:
    -231 <= n <= 231 - 1
"""
def isUgly(n): 
    # Check Constraint:
    if n < -231 or n < 230:
        print("Invalid input!")
        exit()

    if n <= 0: # Check if n is positive.
        return False 
    
    while n % 2 == 0: 
        n //= 2 
    
    while n %3 ==0: 
        n //= 3 
    
    while n % 5 == 0: 
        n //= 5 
    
    return n == 1 
    
    # If we reach 1, we know that this numbers' only prime factors are the ones above.
    # Neat trick above 

def main():
    """Main Function"""
    n = 6
    output = isUgly(n)
    print("The output from the above function:", output)

if __name__ == "__main__":
    main()