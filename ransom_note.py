"""
Leetcode Q 383 -- Ransom Note.

Simplified Time Complexity: 
O(n)

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters
"""
def ransom(ransom, magazine): 
    # Check constraint 1:
    if len(ransom) < 1 or len(ransom) > 105 or len(magazine) < 1 or len(magazine) > 105:
        print("Invalid input!")
        exit()

    chars_ransom = {}
    
    for i in range(len(magazine)): 
        # Check constraint 2: 
        if magazine[i].isalpha() == False or magazine[i].islower() == False:
            print("Invalid input!")
            exit()
        
        # Checks if the current char in mag is in the dict, if not adds it if so adds a tally. 
        chars_ransom[magazine[i]] = chars_ransom.get(magazine[i], 0) + 1 
    
    for j in range(len(ransom)): 
        # Check constraint 2: 
        if ransom[i].isalpha() == False or ransom[i].islower() == False:
            print("Invalid input!")
            exit()

        if ransom[j] in chars_ransom: 
            # We can only use a letter once, so when we run out of a letter this may prev us from fin ransom word.
            if chars_ransom[j] == 0: 
                return False
    
            chars_ransom[ransom[j]] -= 1 

        # Letter in the ransom note not found in the mag.    
        if ransom[j] not in chars_ransom:
            return False 
    
    return True

def main():
    """Main Function"""
    ransomNote = "a"
    magazine = "b"
    output = ransom(ransomNote, magazine)
    print("The output from the above function is:", output)

if __name__ == "__main__":
    main()