"""
Leetcode Q 344 -- Reverse String
 
This question must be solved by modifying the algorithm in place, 
with O(1) extra memory. 

Constraint:
    1 <= s.length <= 10^5

I use a 2 pointer method.

Time Complexity:
O(n)
"""

def reverseString(s):
    # Check constraint:
    if len(s) >= pow(10,5) or len(s) <= 1:
        print("Invalid list size.")
        exit() 

    l = 0 
    r = len(s) - 1
    
    while (l <= r):
        # Checks constraint 
        if s[l].isascii() == False or s[r].isascii == False:
            print("Input string is invalid")
            exit()

        else: 
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l+=1
            r-=1
    
    return s


def main():
    """Main Function"""

    s = ["h","e","l","l","o"]
    output = reverseString(s)

    print('The output of the above function is: ', output)


if __name__ == "__main__":
    main()