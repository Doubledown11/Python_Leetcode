"""
Leetcode Q 217 -- Contains Duplicates.


Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109

    
Simplified Time Complexity:
O(n)

"""

def checkDup(nums):
    # Dict to hold the values and their frequencies in the nums list. 
    freq = {}

    for num in nums:
        # If we iterate over a num which has already been added to the freq 
        # dict, thus we know that this value is a duplicate.
        if freq.get(num) == 1:
            return True
        
        else:
            # If the num hasn't been added to freq yet, we add it and give it a count of 1.
            freq[num] = 1


def main():
    """Main Function"""

    nums = [1,2,3,1]

    output = checkDup(nums)
    if output == True:
        print("The list contains duplicates!")
    else:
        print("The list does not contain duplicates!")



if __name__ == "__main__":
    main()