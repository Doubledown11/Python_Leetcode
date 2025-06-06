"""
Leetcode Q 1 -- TwoSum

I think this is more of a brute force-y method. 

Consider every pair and check if their sum equals the target with nested loops.

Time complexity = O(n^2) 
    Because it's a nested for loop.
    
"""

def twoSum(nums, target): 
    n = len(nums) 
    for i in range(n-1): # Pointer 1 iterate from start of list
        for j in range(i + 1, n): # Pointer 2 iterate from 2nd pos in list
            if nums[i] + nums[j] == target: 
                return [i,j] 
    
    return [] # no solution found.


def main():
    """Main Function"""
    
    nums = [3,2,4]
    target = 6

    print("The sum is = ", twoSum(nums,target))



if __name__ == '__main__':
    main()