"""
Leetcode Q 28 -- Find the Index of the First Occurrence in a String.

Loop through haystack and check substrings for instances of the needle word.     

Simplified Time Complexity: 

Constraints:
    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters
"""

def needleHaystack(needle, haystack):
    # Check constraint 1:
    if len(haystack) < 1 or len(needle) > pow(10,4):
        print("Invalid input!")
        exit()

    # If the length of needle is greater than or equal to the length of haystack
    # needle can not be in haystack, as needle must fit inside of haystack.  
    if len(haystack) <= len(needle): 
        return -1 
    
    # Check constraint 2:
    for x in range(len(haystack)):
        if haystack[x].isupper() == True:
            print("Invalid input!")
            exit()

    for y in range(len(needle)):
        if needle[y].isupper() == True:
            print("Invalid input!")
            exit()

    # In the loop, check substrings of length equal to the length of the needle 
    # starting from the current index i up to i + needle.length() 
    for i in range(0, len(haystack) - len(needle) + 1):
        # If any of these substrings matches the needle, return the index of i.
        if haystack[i:i+len(needle)] == needle:
            return i    




def main():
    """Main Function"""

    needle = 'potent'
    haystack = 'impotent'
    output = needleHaystack(needle, haystack)
    print("The output from the above function is:", output)

if __name__ == "__main__":
    main()