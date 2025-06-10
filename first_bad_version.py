"""
Leetcode Q 278 -- First Bad Version.

Simplified Time Complexity:
O(n) --- I think?
Constraints:
    1 <= bad <= n <= 231 - 1
"""
def firstBadVersion(n): 
    i = 1 
    j = n 
    while (i<j):
        pivot = (i + j) // 2 
        if (isBadVersion(pivot)): 
            j = pivot  # Keeps track of the leftmost bad version
        else: 
            i = pivot + 1  # the one after the rightmost good version.
        
        return i

def main():
    """Main Function"""
    n = 5 
    bad = 4
    output = firstBadVersion(n)
    print("The output from the above function:", output)

if __name__ == "__main__":
    main()