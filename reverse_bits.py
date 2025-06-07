"""
Leetcode Q 190 -- Reverse Bits.

Use of int was a lifesaver. It allows us to convert a string of 0s and 1s into
a binary number by specifying the desired base of the resulting number. 
For binary, we choose base 2. 

Constraint:
    The input must be a binary string of length 32

    
Simplified Time Complexity:
O(n)
"""

def reverseBits(n): 
    # Check Constraint
    if (len(n)) != 32:
        print("Invalid input!") 
        exit()

    valid = True
    one = '1'
    zero = '0'
    for x in range(len(n)):
        print(type(n[x]))
        if n[x] != one and n[x] != zero: 
            print("n at idx", x, "results invalid", n[x])
            valid = False
    
    if valid == False:
        print("Invalid input!") 
        exit()

    # Iterate through the bin string, and swap values. 
    # 1 for 0, and 0 for 1.
    new_bin = []
    for x in range(len(n)):
        new_bin.insert(0, n[x])

    # Iterate through the new_bin list and add each val to a new binary string.
    new_n = ''
    for x in range(len(new_bin)):
        new_n+= new_bin[x]

    return new_n

def main():
    """Main Function"""

    n = '00000010100101000001111010011100'
    output = reverseBits(n)
    print("The resulting integer represented when the input integer's bits are reversed is", int(output, 2))

if __name__ == "__main__":
    main()