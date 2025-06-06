"""
Leetcode Q 283 -- Move Zeroes

This was a good help to learn how to move value in a list in-place.

Constraints:
   1 <= nums.length <= 104
   -231 <= nums[i] <= 231 - 1


Simplified Time Complexity:
O(n) 

I don't completely understand the follow-up on the question. 
Maybe I will return to do it later.
"""

def moveZeroes(nums):
    # Check constraint 1
    if 1 > len(nums) or len(nums) > pow(10,4):
        print("Input list is invalid!")
        exit()
    
    
    last = 0 # Used to hold the idx of the last non-zero value found.

    for x in range(len(nums)):
        # Check constraint 2
        if (nums[x] <= pow(-1, 31)) or (nums[x] >= pow(2,31)-1):
            print("Input list is invalid!")
            exit()

        # If x iterates over a value of zero, we do not iterate the last pointer but we continue to iterate with x.

        # If x iterates over a value other than zero, we swap the value at the x pointer 
        # with the value at the last pointer. We then iterate the last pointer ahead an idx.
        if nums[x] != 0:
            nums[last], nums[x] = nums[x], nums[last]
            last +=1 

    # This process slowly moves all zeroes towwards the end of the list.
    # In some cases, this may take multiple swaps to move a given 0 value to the end of the list. 
    return nums


def main():
    """Main Function"""
    
    nums = [0]
    output = moveZeroes(nums)
    print("The output from the above function is: ", output)

if __name__ == "__main__":
    main()