"""
Leetcode Q 20 -- Valid Parentheses.

Simplified Time Complexity:
O(n^2)

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""
def isValid(s): 
    # Check constraint 1:
    if len(s) < 1 or len(s) > 104:
        print("Invalid input!")
        exit()

    # Init a stack to hold the characters encountered within the string.
    stack = []

    # Init a dict to store the mappings of open bracket to close brackets. 
    mapping = {")":"(", "}":"{", "]":"["}
    
    # Iterate through each character in the string s.
    for char in s: 
        # Check constraint 2: 
        if char not in mapping.values() and char not in mapping.keys():
            print('Invalid input!')
            exit()

        # Checks to ensure the char in s is one of the valid open parentheses.
        if char in mapping.values():  
            # Stack ensure we close brackets in the same order we open them.
            stack.append(char) 

        # If the char is a close 
        elif char in mapping.keys(): 
            # If the char is not an open parenthesis, or if there is no accompanying 
            # close parenthesis then we stop and say the string is not valid. 
    
            # Since this checks close brackets, the top of the stack should be the 
            # corresponding open bracket for the current char.
            # 'If not stack' checks to see if the stack is empty (Which returns true if it isnt)
            if not stack or mapping[char] != stack.pop():
                return False
    
    # After we finish iterating through all the chars and 
    # if there is no chars left over in the stack, 
    # this returns true if the string is valid.
    return not stack 

def main():
    """Main Function"""
    s = "()[]{}"
    output = isValid(s)
    print("The output from the above function is:", output)

if __name__ == "__main__":
    main()