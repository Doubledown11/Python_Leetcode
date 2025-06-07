"""
Leetcode Q 171 -- Excel Sheet Column Number.


Constraints:
    1 <= columnTitle.length <= 7
    columnTitle consists only of uppercase English letters.
    columnTitle is in the range ["A", "FXSHRXW"]

Simplified Time Complexity:



Some Sources Used: 
    https://www.w3schools.com/python/ref_func_reversed.asp
    https://www.w3schools.com/python/ref_string_isupper.asp
    https://www.w3schools.com/python/ref_func_ord.asp
    https://stackoverflow.com/questions/18815820/how-to-convert-string-to-binary
"""

def titleToNumber(columnTitle): 
    # Check constraint 1
    if len(columnTitle) < 1 or len(columnTitle) > 7:
        print("Invalid Input!")
        exit()

    # Check constraint 3
    if ''.join(format(ord(x), 'b') for x in columnTitle) < ''.join(format(ord('A'), 'b')):
        print("Invalid input!")
        exit()
    if ''.join(format(ord(x), 'b') for x in columnTitle) > ''.join(format(ord(x), 'b') for x in 'FXSHRXN'):
        print("Invalid Input!")
        exit()

    ans = 0 
    pos = 0 
    # We iterate backwards through the given column sheet title number.
    # Since each number version of a letter in the title contributes to the number
    # of the letter following, we iterate backwards. Since the only value which the final letter contributes to 
    # is itself. 
    # IE) A Z in position idx 0 (from left to right) entails we are at least at page 26. 
    # Thus, the z (26) affects what the overall value is going to be since we need to add the value of the next character 
    # to 26. 
    for letter in reversed(columnTitle):
        # Check constraint 2:
        if letter.isupper() == False:
            print("Invalid Input!")
            exit()

        # Convert the letter to a number and then we 
        # subtract 64 to ensure it remains in the range of 1 - 26. 
        # This is becuase the input strings only contain capital letters,  
        # which map to ASCII integer values of 65 to 90.
        digit = ord(letter) - 64 
    
        # Add the digit answer after multiplying by 26 to the power of the letters position in the input string.
        ans += digit * pow(26, pos) 
    
        pos +=1 
    
    return ans 

def main():
    """Main Function"""    
    
    columnTitle = "AB"
    output = titleToNumber(columnTitle)
    print("The column number for the given title is", output)

if __name__ == "__main__":
    main()