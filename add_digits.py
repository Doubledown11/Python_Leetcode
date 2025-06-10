"""
Leetcode Q 258 -- Add Digits.


Simplified Time Complexity:
O(n^2)

Constraints:
    0 <= num <= 231 - 1
 

Follow up: 
    Could you do it without any loop/recursion in O(1) runtime?

    Used the solution for the follow-up from here: 
        https://leetcode.com/problems/add-digits/solutions/5412232/python-100-beat-100-efficient-optimal-solution-easy-to-understand/
"""

def addDigits(num):
    # Check Constraint:
    if num < 0 or num > 230:
        print("Invalid input!")
        exit()

    new = 0
    i = True
    while i:
        for x in str(num):
            a = x
            new += int(a)

        if len(str(new)) == 1:
            break

        else:
            num = new
            new = 0
            pass


def addDigits_followUp(num):
    if num == 0: 
        return 0
    
    if num % 9 == 0: 
        return 9
    
    else: 
        return (num % 9)       


def main():
    """Main Function"""
    
    num = 38
    output = addDigits(num)
    print("The output from the above function:", output)

if __name__ == "__main__":
    main()

