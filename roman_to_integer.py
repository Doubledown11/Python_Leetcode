"""
Leetcode Q 13 -- Roman to Integer.

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
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Sources:
    Used an idea from here:     
"""

def romanToInt(roman):
    # # Below dict contains the integer to roman numeral mappings
    # used for the solution.
    # int_roman_map = {1000:"M", 900:"CM", 500:"D", 400:"CD", 
    #                 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X',
    #                 9:'IX', 5:'V', 4:'IV', 1:'I'}


    total = 0
    
    # Check 1000
    if (roman[0] == 'M'):
        count_M = 1 
        # Check ahead to see how many are found within.
        if (roman[1] == 'M'):
            count_M+=1

            for x in range(2, len(roman)):
                if roman[x] == 'M':
                    count_M+=1
                
        # Now we get the value that is represented by the collected characters.
        total += (1000 * count_M)
        
        # Now we remove the above characters from the roman numeral.
        roman = roman[count_M:] 


    if len(roman) <= 0:
        return total


    # Check 900
    if len(roman) >= 2:
        if (roman[:2] == 'CM'):
            count_CM = 1 
            
            total += (900 * count_CM)
            
            roman = roman[count_CM:] 


    # Check to ensure that there are still characters inside the roman
    # numeral string to convert to integer.
    if len(roman) <= 0:
        return total


    # Check 500
    if (roman[0] == 'D'):
        count_D = 1 
                
        total += (500 * count_D)
        
        roman = roman[count_D:] 

    
    if len(roman) <= 0:
        return total


    # Check 400
    if len(roman) >= 2:
        if (roman[:2] == 'CD'):
            count_CD = 1 
                    
            total += (400 * count_CD)
            
            roman = roman[count_CD:]


    if len(roman) <= 0:
        return total


    # Check 100
    if (roman[0] == 'C'):
        count_C = 1 

        if (roman[1] == 'C'):
            count_C+=1

            for x in range(2, len(roman)):
                if roman[x] == 'C':
                    count_C+=1

        total += (100 * count_C)
        
        roman = roman[count_C:] 


    if len(roman) <= 0:
        return total


    # Check 90
    if len(roman) >= 2:
        if (roman[:2] == 'XC'):
            count_XC = 1
            
            total += (90 * count_XC)
            
            roman = roman[count_XC:]


    if len(roman) <= 0:
        return total


    # Check 50
    if (roman[0] == 'L'):
        count_L = 1 

        total += (50 * count_L)
        
        roman = roman[count_L:] 


    if len(roman) <= 0:
        return total


    # Check 40
    if len(roman) >= 2:
        if (roman[:2] == 'XL'):
            count_XL = 1 
                    
            total += (40 * count_XL)

            roman = roman[count_XL:]


    if len(roman) <= 0:
        return total


    # Check 10
    if (roman[0] == 'X'):
        count_X = 1 

        if (roman[1] == 'X'):
            count_X+=1

            for x in range(2, len(roman)):
                if roman[x] == 'X':
                    count_X+=1
                
        total += (10 * count_X)
        
        roman = roman[count_X:] 


    if len(roman) <= 0:
        return total


    # Check 9
    if len(roman) >= 2:
        if (roman[:2] == 'IX'):
            count_IX = 1 
            
            total += (9 * count_IX)
            
            roman = roman[count_IX:]


    if len(roman) <= 0:
        return total


    # Check 5
    if (roman[0] == 'V'):
        count_V = 1 
                
        total += (5 * count_V)
        
        roman = roman[count_V:]


    if len(roman) <= 0:
        return total


    # Check 4
    if len(roman) >= 2:
        if (roman[:2] == 'IV'):
            count_IV = 1 
            
            total += (4 * count_IV)
            
            roman = roman[count_IV:]


    if len(roman) <= 0:
        return total


    # Check 1
    if (roman[0] == 'I'):
        count_I = 1

        if len(roman) == 2: 
            count_I+=1

        elif len(roman) == 3:
            count_I+=2
        
        total += (1 * count_I)
        
        roman = roman[count_I:]

    return total


def main():
    """Main Function"""

    roman = "LVIII"
    output = romanToInt(roman)
    print("The output from the above function is:", output)

if __name__ == "__main__":
    main()