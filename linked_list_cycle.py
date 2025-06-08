"""
Leetcode Q 141 -- Linked List Cycle.


Simplified Time Complexity: 


Constraints:
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list

Follow-Up:
    Can you solve it using O(1) (i.e. constant) memory?


"""

def hasCycle(head): 
    """
    The linked list cycle check using a 2 pointer method 
    which implements a tortoise and hare algorithm.

    Can not remember where I found the idea/solution for this code originally. 
    It has been much time.  

    The code uses 2 pointers which move at different speeds.
        Slow moves ahead 1 node at a time.
        Fast moves ahead 2 nodes at a time.
        
    If there is a cycle in the linked list, the fast node will eventually catch up to the slow node.
        That is, the fast pointer traverses until it cycles to the slow node or 
        until its next pointer equals None. Which means that it has reached the end of the list. 
        And thus, there is no loop!


    Simplified Time Complexity: 
        O(n)
    """

    slow = head 
    fast = head 

    # If fast reaches the tail (= to None and thus false) the loop wll end 
    # and thus theres no cycle.	 
    while fast and fast.next: 
        slow = slow.next 

        # So if slow reaches the tail, it will equal None and thus return false and end the loop. 
        fast = fast.next.next 
        if slow == fast: 
            return True 
        
    return False 


def main():
    """Main Function"""

    head = [3,2,0,-4]
    pos = 1


if __name__ == "__main__":
    main()