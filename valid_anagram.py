"""
Leetcode Q 242 -- Valid Anagram

This question is a great example of the .get() function. 
Which is a fantastic dictionary method in Python.

From the leetcode question page: 
    An anagram is a word or phrase formed by rearranging
    the letters of a different word or phrase, using all 
    the original letters exactly once.

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters

Simplified Time Complexity:
    O(n)

    

Follow-Up:
    What if the inputs contain Unicode characters? 
    How would you adapt your solution to such a case?

    I might be able to use ord() to convert the unicode characters too 
    their respective ascii integer values, then perform the same frequency operation.
"""

def isAnagram(s, t):
    # Check constraint 1
    if (len(s) < 1) or (len(t) > (5 * pow(10,4))):
        print("Invalid input sizes!")
        exit()

    # Check if lengths of both strings are equal.
    # If not, they can't be anagrams.
    if (len(s) != len(t)):
        return False 

    # Init a dict to hold the characters and their frequencies from s.
    checker = {}
    for char in s:
        # Check constraint 2
        if char.islower() == False or char.isalpha() == False:
            print("Invalid input!")
            exit()

        # For each val in s, check to see if it is found within the 
        # checker dict if not add it and place 0. If found, increment by 1.
        checker[char] = checker.get(char, 0) + 1

    # Iterate through t, and for each char in t, 
    # reduce a frequency count from the checker dict. 
    for char in t:
        # Check constraint 2
        if char.islower() == False or char.isalpha() == False:
            print("Invalid input!")
            exit()

        # If a value is not in checker, or its current frequency has reached 0
        # s and t can not be anagrams.
        if checker.get(char) == None or checker[char] == 0:
            return False
        else: 
            checker[char]-=1

    # If we can fully iterate through t without returning false, then they must be anagrams.
    return True


def isAnagram_unicode(s, t):
    """
    Function which should address the follow-up!
    Same as above function, but converts the characters to their ascii integers.
    """

    # Check constraint 1
    if (len(s) < 1) or (len(t) > (5 * pow(10,4))):
        print("Invalid input sizes!")
        exit()

    # Check if lengths of both strings are equal.
    # If not, they can't be anagrams.
    if (len(s) != len(t)):
        return False 

    # Init a dict to hold the characters and their frequencies from s.
    checker = {}
    for char in s:
        # Check constraint 2
        if char.islower() == False or char.isalpha() == False:
            print("Invalid input!")
            exit()

        # For each val in s, check to see if it is found within the 
        # checker dict if not add it and place 0. If found, increment by 1.
        checker[ord(char)] = checker.get(ord(char), 0) + 1

    # Iterate through t, and for each char in t, 
    # reduce a frequency count from the checker dict. 
    for char in t:
        # Check constraint 2
        if char.islower() == False or char.isalpha() == False:
            print("Invalid input!")
            exit()

        # If a value is not in checker, or its current frequency has reached 0
        # s and t can not be anagrams.
        if checker.get(ord(char)) == None or checker[ord(char)] == 0:
            return False
        else: 
            checker[ord(char)]-=1

    # If we can fully iterate through t without returning false, then they must be anagrams.
    return True



def main():
    """Main Function"""

    s = "anagram"
    t = "nagaram"

    output = isAnagram(s, t)
    if output == True:
        print(s, "and", t, "are anagrams!")
    else: 
        print(s, "and", t,"are not anagrams!")

if __name__ == "__main__":
    main()