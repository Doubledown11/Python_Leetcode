"""
Leetcode Q 191 -- Number of 1 Bits.


Follow-up:
    If this question is called many times, how would you optimize it?  


Constraints:
    1 <= n <= 231 - 1

Simplified Time Complexity:
    O(n) -- CHECK 

"""

def hammingweight(n): 

    # Converts the integer to a binary number.
    # We have to be sure to remove the first 2 digits as they
    # are '0b' in python. This is used to represent a binary number to the Python interpreter. 
    n = bin(n)[2:]
    
    # Convert the binary number into a string.
    n = str(n) 
    
    # I just used the count string method to ID how many 1's were in the string representation of 
    # the binary number. 
    return n.count("1")
     
def main():
    """Main Function"""

    n = 128

    output = hammingweight(n)

    print("The number of 1 bits in the binary representation of", n, "is", output)

if __name__ == "__main__":
    main()