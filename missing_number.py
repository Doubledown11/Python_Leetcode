"""
Leetcode Q 268 -- Missing Number

The question had a bit of a tricky wording regarding the content of the list.
Though once I understood it, it made the solution significantly easier to develop. 

The list contains values in the range of 0 to n, but 1 value in that range is missing.
So we can use another list, with size of len(nums) + 1, which will hold all value in the range. 
Except for the missing value which will be set to some other arbitrary element.

Simplified Time Complexity:
O(n) 
"""

def missingNumber(nums):
    n = len(nums)
    # Init list list2 with 1 more space then does the nums list.
    # This extra space will hold a value of X where the missing num in nums is.
    list2 = ['X'] * (n+1)
        
    # Iterate through nums and place each element at its position in list2. 
    # Element of 1, would be at idx 1 in list2. ELement of 3, would be at idx 3 in list2.
    for num in nums:
        list2[num] = num # Sets the value in nums to the idx represented by that value in list2.

    # Iterate through list2 until we find the idx with the X value.
    # This is our missing number. 
    for x in range(len(list2)):
        if list2[x] == 'X':
            return x

def main():
    """Main Function"""

    nums = [0,1]

    output = missingNumber(nums)

    print("The output of the above function is: ", output)



if __name__ == "__main__":
    main()