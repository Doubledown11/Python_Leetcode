"""
Leetcode Q 104 -- Maximum Depth of Binary Tree. 

Simplified Time Complexity:
O(2^n)

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100.

"""
import BinaryTree
def maxDepth(root): 
    if root == None: 
        return 0 
    
    # Check Constraint 2: 
    if (root.value < -100 or root.value > 100):
        print("Invalid input!")
        exit()

    # From the root node of each recursive call we calculate the depth of 
    # its left and right sub trees.   
    left_depth = maxDepth(root.left) 
    right_depth = maxDepth(root.right)
    
    # With the depths of the right and left subtrees, we return the depth with 
    # the larger value to the prior function call. 
    # We also add 1 to this max depth value, this ensures the current level is 
    # also being added to the current max depth sum before it is returned 
    # to the prior recursive level.   
    return 1 + max(left_depth, right_depth) 


def main():
    """Main Function"""

    # Still have to built the binary tree.
    root = [3,9,20,None,None,15,7]
    
    # Can check constraint 1 here in main, but I feel that isn't in the spirit of leetcode.
    # So I think I am going to skip it for now.

if __name__ == "__main__":
    main()