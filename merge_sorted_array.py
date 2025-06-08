"""
Leetcode Q 88 -- Merge Sorted Array.

Simplified Time Complexity: 
Solution 1: O(m*n)
Solution 2: O(m+n)

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109


Follow up: 
    Can you come up with an algorithm that runs in O(m + n) time?

    Had to lookup a new solution for the follow-up question.
        https://leetcode.com/problems/merge-sorted-array/solutions/6787257/in-place-merge-of-two-sorted-arrays-beats-100/

Sources:
    https://www.geeksforgeeks.org/merge-sort/
"""

def mergeSort(nums1, nums2, m, n):
    """
    Implements the solution in O(m*n) time.
    """
    
    # Check Constraint 1: 
    if len(nums1) != m+n:
        print("Invalid input!")
        exit()
    
    # Check constraint 2:
    if len(nums2) != n:
        print("Invalid input!")
        exit()
        
    # Check constraint 3: 
    if (m < 0 or n > 200):
        print("Invalid input!")
        exit()
    
    # Check constraint 4:
    if (m+n) < 1 or (m+n) > 200:
        print("Invalid input!")
        exit()

    #Should replace the 0s in nums1 with the nums2 vals -> Merged 
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            # Check constraint 5:
            if nums1[i] < -pow(10,9):
                print("Invalid input!")
                exit()

            if nums2[j] > pow(10,9):
                print("Invalid input!")
                exit()

            if nums1[i] == 0:
                nums1[i] = nums2[j]
                # Bottom loop should be changed to A while loop. 
                # As this will keep adding the first value in nums2 to nums1
                # in place of the 0  while loop can the be manually iterated each 
                # time we add a new Val to nums1.
    
    # With lists merged we should now ensure they are sorted 
    # in non-decreasing (ascending) order and we use .sort() to do so.
    nums1.sort()


def merge_sort(nums1, nums2, m, n):
    """
    Implements the solution in O(m+n) time.
    """

    # Init 2 pointers to the idx at the end of both nums lists.
    x = m-1
    y = n-1

    # Iterate through the length of nums1 (which is m+n) from its would be 
    # final idx, to the idx 0. This is iterating backwards.
    for z in range(m+n-1, -1, -1):
        if x < 0:
            nums1[z] = nums2[y]
            y-=1 
        
        elif y < 0:
            break 
            
        elif nums1[x] >= nums2[y]:
            nums1[z] = nums1[x]
            x -=1 
        
        else:
            nums1[z] = nums2[y]
            y-=1
    
    return nums1




def main():
    """Main Function"""

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    output = mergeSort(nums2, nums2, m, n)


if __name__ == "__main__":
    main() 