"""
Leetcode Q 206 -- Reverse Linked List.


Was not entirely sure how to implement the recursive aspect of the follow-up question.
So I used code in the solutions from here: 
    https://leetcode.com/problems/reverse-linked-list/solutions/4227749/o-n-recursive-approach-python-step-by-step-explanation/
    https://leetcode.com/problems/reverse-linked-list/solutions/6705038/understanding-the-recursive-solution/

Honestly, I struggled with the recursive solution. 
I have doubts that I will remember this method.

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

    
Simplified Time Complexity:
O(n)

"""
import LinkedList

def reverseList(head):
    """
    Performs the LinkedList reversal iteratively.
    """

    values = []

    head2 = head
    # Iterate through the list saving data elements to values list.
    while head2:
        values.append(head2.data)
        head2 = head2.next

    # Init a new Linked List 
    new_list = LinkedList()
    
    # Iterate through the values list inserting a new node at idx 0 for each data point in the values list. 
    for x in range(0, len(values) - 1):
        new_list.add(0, values[x])


def revLinkedList_recursively(head): 
    """
    Performs the LinkedList reversal recursively.
    """

    # Base Case: Head has reached the end of the list.
    if head == None:
        return None
    
    # Init a 2nd pointer for the head node.
    head2 = head 

    # If the head node isn't at the second last node in the list.
    if head.next != None:
        head2 = revLinkedList_recursively(head.next)
        head.next.next = head # We re-assign the former null pointer at the end of the list with the current head node.

    # The above if statement in conjuction with the recursive function calls 
    # Moves the head pointer to the end of the list, in the last recursive call in the recursive chain.
    head.next = None

    return head2

def main():
    """Main Function"""

    
if __name__ == "__main__":
    main()