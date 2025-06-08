"""
Leetcode Q 94 -- Binary Tree inorder Traversal.

Simplified Time Complexity:
O(2^n)

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Follow up: 
    Recursive solution is trivial, could you do it iteratively?

I don't know where I got the idea to use nested functions. 
But this seemed to make a few questions significantly easier. 
"""

def inoderTrav(root): 
    # Init var to count number of nodes for constraint 1.
    node_count = 0 

    def trav(node, result):
        # Bottom of the tree 
        if node is None:  
            return 
        
        # Check constraint 2:
        if (node.data < -100 or node.data > 100):
            print("Invalid input!")
            exit()

        trav(node.left, result)
        result.append(node.val) 
        trav(node.right, result) 
        
    result = [] 
    trav(root, result) 

    # Check constraint 1:
    if (node_count < 0 or node_count > 100):
        print("Invalid input!")
        exit()  
    
    return result 


def main():
    """Main Function"""


if __name__ == "__main__":
    main()