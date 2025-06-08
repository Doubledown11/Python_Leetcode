"""
Leetcode Q 70 -- Climbing Stairs.


Recursive Method - How do I spot recursive problems in the future?

1) Problem can be broken down into sub-pieces/sub-problems.
   Step down 1 or 2.

2) Need to solve the same sub-problem through each recursive call.
   at each step we need to see how many possible combos of stepping down 1 or 2 there are.

4) Need to backtrack -- Need to undo steps.
   When we reach the bottom step during one such recursive run, we need to return
   to a step previously in the chain where we made a 1 step, and see where the 2 step would go.


   
Components of a recursive function: 
    Base Case: 
        Simplest case at which no further recursion is needed. 
        This terminates the function from further calling itself.
        Without, the function could lead to infinite recursion.

    Recursive Case:
        The function calls itself with the modified arguments.
        This allows the function to break the problem into smaller
        instances of the same problem. 


Simplified Time Complexity:
O(2^k)

Constraints:
    1 <= n <= 45

Sources:
    https://www.geeksforgeeks.org/recursive-functions/
    
"""

def climb(n):
    # Check constraint 1: 
    if n < 1 or n > 45:
        print("Invalid input!")
        exit() 

    # Base Case: From the bottom step (n==1) there is only 1 way to climb down.
    if n <= 1:
        return 1


    else:  # From the top step we
        return climb(n-2) + climb(n-1) 


def main():
    """Main Function"""

    n = 3 
    output = climb(n)
    print("The output from the above function returns:", output)

if __name__ == "__main__":
    main()