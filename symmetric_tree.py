"""
Leetcode Q 101 -- Symmetric Tree.


Simplified Time Complexity:


Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

    
Follow-Up:
    Could you solve it both recursively and iteratively?
    
"""

def isMirror(left, right): 
    """
    Implements the solution to the problem recursively.
    """

    # If both the child nodes contain null / dont exist return True
    # BC the tree is still seen as symmetric, and we have reached both bottoms
    if not left and not right: 
        return True 
    
    # If one of the child nodes reaches the bottom (A None node), 
    # but the other doesn't. The tree is not symmetrical.
    if not left or not right: 
        return False 
    
    return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    # return true if the left val = right val AND 
    # if the rest of both the left and right subtrees are symmetrical 
    # (Return true from recursive function calls).
 
def isSymmetric(root): 
    """
    Helper function to the recursive solution.
    """

    if not root: # If node val = null
        return True 
    return isMirror(root.left, root.right)




def main():
    """Main Function"""
    tree_vals = [1,2,2,3,4,4,3]
    # Build binary tree TODO L8TR

    ##########################
    output = isSymmetric(root)
    if (output == True):
        print("The given binary tree is a mirror of itself.")
    else: 
        print("The given tree is not a mirror of itself.")



if __name__ == "__main__":
    main()