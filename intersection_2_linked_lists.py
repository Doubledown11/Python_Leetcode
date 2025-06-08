"""
Leetcode Q 160 -- Intersection of Two Linkedlists.

Simplified Time Complexity: 
    O(n + m) 
        Since we have 2 pointers which traverse 2 separate lists, which may be of different sizes.

Constraints: 
    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 104
    1 <= Node.val <= 105
    0 <= skipA <= m
    0 <= skipB <= n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


Follow-Up:
    Could you write a solution that runs in O(m + n) time and use only O(1) memory?

    Source: Received some help from the solution below: 
        https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/6812910/beats-95-beginner-friendly-explanation-python-only/
"""


def getIntersectionNode(headA, headB): 
    
    
    
    if (headA == False) or (headB == False):
        return None
    
    l1 = headA
    l2 = headB

    while l1 != l2:
        if (l1 == True):
            l1 = l1.next
        else:
            l1 = headB 
        
        if (l2 == True):
            l2 = l2.next 
        else:
            l2 = headA
        
        return l1


def main():
    """Main Function"""

    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5] 
    skipA = 2 
    skipB = 3

    outcome = getIntersectionNode()


if __name__ == "__main__":
    main()