"""
Leetcode Q 26 -- Removes Duplicates From a Sorted Array.

The solution requires you to remove the duplicates in-place, and the 
relative order of the elements should be kept the same. 

Simplified Time Complexity:
O(n)

Constraints:
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
"""

def removeDuplicates(nums):
    # Check constraint 1:
    if len(nums) < 1 or len(nums) > (3 * 104):
        print("Invalid input!")
        exit() 

    # Check constraint 3: 
    if nums.sort() != nums:
        print("Invalid input!")
        exit()
 
    # Init a pointer to the idx of 1 in the list.
    # This determines where the next unique element encountered will be stored.
    # The element at idx 0, is always considered to be unique.
    j = 1 

    for i in range(1, len(nums)):
        # Check constraint 2: 
        if nums[i] < -100 or nums[i] > 100:
            print("Invalid input!")
            exit()

        # If we find a duplicate value, j doesn't move and remains in the
        # location where the next unique value will be stored.  
        if nums[j] == nums[i]:
            j+=1 

    return j

def main():
    """Main Function"""

    nums = [1,1,2]
    output = removeDuplicates(nums)
    print("The output from the above function is:", output)

if __name__ == "__main__":
    main()