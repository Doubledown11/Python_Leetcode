"""
Leetcode Q 169 -- Majority Element. 


Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

Simplified Time Complexity:
O(n)

Follow-up: 
    Could you solve the problem in linear time and in O(1) space?
    
Sources:
    https://leetcode.com/problems/majority-element/solutions/5845732/video-2-solutions-using-hashmap-o-n-space-and-without-hashmap-o-1-space/
"""

def majElement(nums): 
    m = {}
    
    for num in nums: 
        # Constraint 3:
        if num < -pow(10,9) or num > pow(10,9):
            print("Invalid input!")
            exit()
        
        else: 
            m[num] = m.get(num, 0) + 1
            # # Check if num has already been added to the dict.
            # if m.get(num) == 0:
            #     m[num] = 1
            # else:
            #     m[num]+=1

                
    
    n = len(nums)
    # Constraint 2:
    if n < 1 or n > (5*pow(10,4)):
        print("Invalid input!")
        exit()

    for key, value in m.items(): 
        # So if the element has a count greater than the half of the amount 
        # of the array, we say its the element and return it.
        if value > (n // 2): # Constraint 1
            return key 
    
    return 0


def maj_element_(nums):
    """
    Implements the majority element function, but does so with O(1) space.
    
    Adds to a running sum as we iterate through the list if we encounter a duplicate value to the current.
    Subtracts from sum if we find a non-duplicate val from current.
    When the running sum reaches 0, we have to swap which value is considered the return value. (The val with highest frequency)
    At the end of the list, the value with the highest frequency will be returned. As there was not enough 
    not duplicates to reduce its count to 0, before the end of the list. 
    """

    # Result = the value to be returned.
    result = 0 
    # Majority = Frequency of the majority number.
    majority = 0

    for num in nums:

        if majority == 0:
            result = num
        
        # Each time the current number, n, is the same as result
        # we add +1 to majority. If not, we -1 from majority.
        majority += 1 if num == result else -1
    
    return result


def main():
    """Main Function."""

    nums = [3,2,3]
    output = majElement(nums)
    if output == 0:
        print("There is no majority element.")
    else:
        print("Output from the above function is:", output)

if __name__ == "__main__":
    main()