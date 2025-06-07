"""
Leetcode Q 234 -- Palindrome Linked List

Palindrome: A Word or phrase that reads the same backwards as forwards

This is a singly linked list, and thus can only be traversed in one direction.

Constraints: 
    The number of nodes in the list is in the range [1, 105]
    0 <= Node.val <= 9

Simplified Time Complexity: 
O(n), but in O(1) extra space. So I didn't get the follow-up for this question.

"""


def isPalindrome(self, head): 
    
    values = []

    # Iterate until reach the end of the linked list, adding each node's value to a list.
    while head: 
        if head.data < 0 or head.data > 9:
            print("Invalid input list.")
            exit()
        else:   
            values.append(head.data)
            head = head.next

    # Check constraint 1: 
    if len(values) < 1 or len(values) > pow(10,5):
        print("Invalid input list.")
        exit()

    # Init 2 variables to hold the first and last data point in the values list.
    first = 0
    last = len(values) - 1
    
    # Iterate both pointers towards each other and compare values.
    while first <= last:
        if first != last:
            return False

    # If both pointers can iterate to the middle, all values must be the same. 
    return True 


def main():
    """Main Function"""



if __name__ == "__main__":
    main()