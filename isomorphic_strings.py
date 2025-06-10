"""
Leetcode Q 205 -- Isomorphic Strings.


Simplified Time Complexity:
O(n)

Constraints:
    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character
"""


def isIsomorphic(s, t): 
    # Check constraint 1:
    if len(s) < 1 or len(s) > 5:
        print("Invalid input!")
        exit()
    
    # Check constraint 2:
    if len(s) != len(t):
        print("Invalid input!")
        exit()


    indexS = [0] * 200 
    indexT = [0] * 200
    # I am unsure as to how these above lists are used to store the char mappings, check back later.
    
    length = len(s)
    
    if length != len(t): # if words are not equal length can not be isomorphic
        return False 
    
    for i in range(length): # Iterate through each character in the strings.
        # Check constraint 3: 
        if s[i].isascii() == False:
            print("Invalid input!")
            exit()

        if t[i].isascii() == False:
            print("Invalid input!")
            exit()
        
        
        if indexS[ord(s[i])] != indexT[ord(t[i])]: # Check if the index of the current character in string s is different from the index of the corresponding character in string t 
            return False 
    
    indexS[ord(s[i])] = i + 1 # Updating the position of the current character. 
    indexT[ord(t[i])] = i + 1 
    
    return True # If the loop completes without returning False, strings are isomorphic.

def main():
    """Main Function"""

    s = "egg"
    t = "add"

    output = isIsomorphic(s, t)
    print("The output from the above function is:", output)


if __name__ == "__main__":
    main()

