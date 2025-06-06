"""
Leetcode Q 349 -- Intersection of Two Arrays


Time complexity:
O(n^2)

"""

def intersect(nums1, nums2): 
    result = []
    for x in range(len(nums2)):
        if nums2[x] in nums1:
            result.append(nums2[x])

    return result 


def main():
    """Main Function"""

    nums1 = [1,2,2,1]
    nums2 = [2,2]

    output = intersect(nums1, nums2) 

    print("The output from the above function is: ", output)


if __name__ == "__main__":
    main()