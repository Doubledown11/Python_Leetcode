"""
Leetcode Q 118 -- Pascal's Triangle.

Simplified Time Complexity:
O(n)- I think?

Constraints:
    1 <= numRows <= 30

I struggled with this one. It's been some time however, and I do not 
know where I got this solution from unfortunately.
"""

def generate(numRows): 
    # Check Constraint 1: 
    if numRows < 1 or numRows > 30:
        print("Invalid input!")
        exit()

    if numRows == 0: 
        return [] 
    
    if numRows == 1: 
        return [[1]]

    # prevRows is a list which holds the row lists and represents the triangle itself.    
    prevRows = generate(numRows -1) 
    

    # Create a new row filled with 1’s in len of the current row count. 
    # so we have a row with 5 possible values in it.
    newRow = [1] * numRows 
    
    for i in range(1, numRows - 1): 
        # We start at 1, BC first val (index 0) in row is auto = to 1. 
        # and we only go to the second last val since the last in the row is also = 1 
        # IE) [1,_,_,_,1]
        newRow[i] = prevRows[-1][i-1] + prevRows[-1][i]
        
    # After a row is created and filled, we append it to the end of the triangle list, and thus say we have created another row or layer to the triangle.
    prevRows.append(newRow)

    return prevRows


def main():
    """Main Function"""

    numRows = 5
    output = generate(numRows)

    print("The rows of the output triangle are as follows:")
    for row in output:
        print(row)
        print('\n')


if __name__ == "__main__":
    main()