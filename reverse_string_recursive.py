"""
Leetcode Q 344 -- Reverse String
 
This question must be solved by modifying the algorithm in place, 
with O(1) extra memory. 

Constraint:
    1 <= s.length <= 10^5

I use a 2 pointer method with recursion.

Time Complexity:
O(n)


My understanding of the analysis time complexity:
    Since the function calls itself n/2 times before reaching the bascase,
    it is simplified to O(n). Becuase n/2 is still reliant on the value of n.
"""

def reverseString(s, l, r):
    # Base Case: l >= r
    if l >= r:
        return s

    else:
        # Checks constraint 
        if s[l].isascii() == False or s[r].isascii == False:
            print("Input string is invalid")
            exit()

        tmp = s[l]
        s[l] = s[r]
        s[r] = tmp
        l+=1
        r-=1
        return reverseString(s, l, r)

def main():
    """Main Function"""

    s = ["h","e","l","l","o"]
    l = 0 
    r = len(s) - 1

    # Check constraint:
    if len(s) >= pow(10,5) or len(s) <= 1:
        print("Invalid list size.")
        exit()

    output = reverseString(s, l , r)

    print('The output of the above function is: ', output)


if __name__ == "__main__":
    main()