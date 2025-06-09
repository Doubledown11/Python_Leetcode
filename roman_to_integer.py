"""
Leetcode Q 12 -- Integer to Roman.

Roman numerals are represented by 7 different symbols: 
    I = 1 
    V = 5 
    X = 10 
    L = 50 
    C = 100 
    D = 500 
    M = 1000  

Simplified Time Complexity: 
O(1)

Constraints:
    1 <= num <= 3999

Sources:
    Used an idea from here: https://leetcode.com/problems/integer-to-roman/description/    
"""

def romanToInt(num):
    # Check constraint 1:
    if num < 1 or num > 3999:
        print("Invalid input!")
        exit()
    
    # Init a dict which holds the integer to roman numeral mappings.
    int_roman_map = {1000:"M", 900:"CM", 500:"D", 400:"CD", 
                    100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X',
                    9:'IX', 5:'V', 4:'IV', 1:'I'}
    
    roman = ''

    # Check if num is divisible by each roman numeral amount, then we do the following: 

    # If num is bigger then 1000 (we can fit a whole number of 1000’s into num).
    if (num // 1000) != 0: 
        # Get number of M values.
        num_M = num // 1000 # = 3 
        
        # Create the M values.
        M_count = num_M * 'M' # 3 M's
        
        # Add M values to the Roman numeral.
        roman += M_count  # roman = MMM
        
        # remove the value created by the sum of the number of M values from the num.
        num -= (1000 * num_M) # num == 749
    

    if (num // 900) != 0:
        num_CM = num // 900
        CM_count = num_CM * 'CM'
        roman += CM_count
        num -= (num_CM * 900)


    if (num // 500) != 0:
        num_D = num // 500
        D_count = num_D * 'D'
        roman += D_count
        num -= (num_D * 500)


    if (num // 400) != 0:
        num_CD = num // 400
        CD_count = num_CD * 'CD'
        roman += CD_count
        num -= (num_CD * 400)


    if (num // 100) != 0:
        num_C = num // 100
        C_count = num_C * 'C'
        roman += C_count
        num -= (num_C * 100)


    if (num // 90) != 0:
        num_XC = num // 90
        XC_count = num_XC * 'XC'
        roman += XC_count
        num -= (num_XC * 90)


    if (num // 50) != 0:
        num_L = num // 50
        L_count = num_L * 'L'
        roman += L_count
        num -= (num_L * 50)


    if (num // 40) != 0:
        num_XL = num // 40
        XL_count = num_XL * 'XL'
        roman += XL_count
        num -= (num_XL * 40)


    if (num // 10) != 0:
        num_X = num // 10
        X_count = num_X * 'X'
        roman += X_count
        num -= (num_X * 10)


    if (num // 9) != 0:
        num_IX = num // 9
        IX_count = num_IX * 'IX'
        roman += IX_count
        num -= (num_IX * 9)


    if (num // 5) != 0:
        num_V = num // 5
        V_count = num_V * 'V'
        roman += V_count
        num -= (num_V * 5)


    if (num // 4) != 0:
        num_IV = num // 4
        IV_count = num_IV * 'IV'
        roman += IV_count
        num -= (num_IV * 4)


    if (num // 1) != 0:
        num_I = num // 1
        I_count = num_I * 'I'
        roman += I_count
        num -= (num_I * 1)


    return roman


def main():
    """Main Function"""

    num = 58
    output = romanToInt(num)
    print("The output from the above function is:", output)

if __name__ == "__main__":
    main()