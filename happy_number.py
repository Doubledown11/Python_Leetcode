"""
Leetcode Q 202 -- Happy Number.


Constraints:
    1 <= n <= 231 - 1


Simplified Time Complexity:
O(2)
"""

def isHappy(n): 
    # Check constraint 1:
    if n < 1 or n >= 231:
        print("Invalid Input!")
        exit()

    current_number = n # holds the current value of the number following a calculation.
    numbers = {} # Holds all previously calculated values. 
    
    while True:
        sum_sq = 0
        for i in str(current_number): 
            # Sums the square of each digit.
            sum_sq+= int(i) **2 
            
        # After summing the squares, if sum_sq = 1 we know it's happy.            
        if sum_sq == 1: 
            return True 

        # If we see the number before, it can not be happy.            
        if sum_sq in numbers: 
            return False 

        # Add the key of sum_sq to the dict with a value of 0 (val dont matter)        
        numbers[sum_sq] = 0 

        # Change our current number to equal the sum_sq value after squaring the sum of the digits.
        current_number = sum_sq 

def main():
    """Main Function"""

    n = 2

    output = isHappy(n)

    if output:
        print("The number", n, "is happy!")
    else:
        print("The number", n, "is not happy!")

if __name__ == "__main__":
    main()