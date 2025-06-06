"""
Leetcode Q 387 -- First Unique Character in a String

This solution was found near the top of my solutions document, 
and I started to utilize the dictionary more in my solutions after this! 

Shows how to get the frequency of an element from a data structure/object and 
save it to a dictionary. 

"""


def firstUniqueChar(s): 
    mp = {} 

    # iterate through string and add each char and its count to the dict.
    for char in s: 
        mp[char] = mp.get(char,0) + 1
  
        # Returns the value of the item with the specified key.
        # Returns 0 if no value for the specified key, we can then add 1 to the value saved at the given key.
    
        # mp.get(char,0) 
        # Gets the current count of character ‘char’ from the dict. If not yet in the dict, returns 0.
        # So the word leet, when we reach the second e we will loop through the dict and see that e is already contained and thus the second e’s value will increment to 2. 
    
        # mp.get(char,0) + 1
        # # Updates the dict by incrementing the count of the character ‘char’ 
        # If no duplicates found the val is 0 
    
        # After this loop the dict will contain the frequency of each char in the string.
        # So when we reach a key which does have a value of 1, we know it has to be the first unique char in the string
    

    # then iterate through the dict to see which char has a value of 1.
    for x in range(len(s)):
        if mp[s[x]] == 1:
            return x
    
    return -1
 

def main():
    """Main Function"""

    s = 'loveleetcode'
    output = firstUniqueChar(s)

    print("The output from the above function is: ", output)

if __name__ == "__main__":
    main()