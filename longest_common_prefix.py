"""
Leetcode Q 14 -- Longest Common Prefix.

Simplified Time Complexity:
    Ignoring the 3rd constraint check, it's in O(n log(n)) time.
            This is due to the sorted function.

        Else it is in O(n^2) time.  

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty
"""
def longestCommonPrefix(strs): 
    # Check constraint 1: 
    if len(strs) < 1 or len(strs) > 200:
        print("Invalid input!")
        exit()

    # Init string to store the current common prefix. 
    ans = ''

    # Sorts the list alphabetically aka sorts ascending order by 
    # default just like .sort()  
    list = sorted(strs) 

    # Init a pointer to the first word and the last word in the strs list.
    first = list[0]
    last = list[-1]

    # Only need to check the first and last words of the list 
    # since after being sorted alphabetically, any similarities 
    # they contain will be shared between all words in the list. 
    # THIS IS KEY TO THIS SOLUTION!!!


    # Check constraint 2:
    for x in range(len(strs)):
        if len(strs[x]) < 0 or len(strs[x]) > 200:
            print("Invalid input!")
            exit()
        
        # Check constraint 3:
        for y in strs[x]:
            if y.isupper() == True:
                print("Invalid input!")
                exit() 

    # Only check # of chars = len of smallest word.
    # If we do not find a common prefix within the length of that smallest word, 
    # we know that there is no common prefix in the list. Since all chars of that smallest word
    # are not found in every other word.  
    for i in range(min(len(first), len(last))): 
        if (first[i] != last[i]): 
            if i == 0:
                return ''
            
            return ans 

        else:
            ans+=first[i]

    return ans


def main():
    """Main Function"""
    strs = ["flower","flow","flight"]
    output = longestCommonPrefix(strs)
    if output == '':
        print("There is no common prefix among the elements of strs!")
    
    else:
        print("The output from the above function is:", output)

if __name__ == "__main__":
    main()