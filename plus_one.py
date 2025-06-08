"""
Leetcode Q 66 -- Plus One.

The digits are ordered from most significant to to least significant in left to right order. 
Might need to add a check to ensure that the digits are ordered most to least significant
The large integer does not contain any leading 0s.
Increment the large integer by 1 and return the resulting array.

Simplified Time Complexity:
O(n)

Constraints:
    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain any leading 0's.
"""
def plusOne(digits): 
    # Check constraint 1:
    if len(digits) < 1 or len(digits) > 100:
        print("Invalid input!")
        exit() 

    # Check Constraint 3:
    if digits[0] == 0:
        print("Invalid input!")
        exit()

    # Init a var to hold the string representation of the number 
    # contained within the digits list. 
    number = ''

    # Iterate through the list and add each digit to a string 
    # which will represent the number contained inside the list.
    for i in range(len(digits)):
        # Check constraint 2:
        if digits[i] < 0 or digits[i] > 9:
            print("Invalid input!")
            exit()

        number += str(digits[i])
    
    # Increment the above number by 1.
    number = str(int(number)+1)
    
    # Init another list to hold the number's digits.
    new_list = []
    
    # Iterate through the string number and append each digit to the new_list.
    for i in range(len(number)): 
        new_list.append(number[i]) 
    
    return new_list 

def main():
    """Main Function"""

    digits = [1,2,3]
    output = plusOne(digits)
    print("The output list from the above function is:")
    print(output)

if __name__ == "__main__":
    main()