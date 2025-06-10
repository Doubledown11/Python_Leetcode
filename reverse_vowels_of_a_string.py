"""
Leetcode Q 345 -- Reverse Vowels of a String.

Simplified Time Complexity:
O(n^2)

Constraints:
    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
"""

def rev_vowel(s): 
    vowels = ['a' , 'e', 'i', 'o', 'u']
    
    # Move chars in s to a list.
    letters = []
    for x in range(len(s)):
        letters.append(s[x])
    
    # Init 2 vars that are used to iterate through the list; One at the 
    # start and 1 at the end.
    l = 0 
    r = len(s) -1  
    while l < r: 
        x = True

        # Move until left pointer is at a vowel
        while x: 
            if letters[l].lower() not in vowels: 
                l +=1 
            else: 
                x = False

        x = True
        # Move until right pointer is at a vowel 
        while x: 
            if letters[r].lower() not in vowels: 
                r -=1 
            else:
                x = False             

        # Swap vowels
        tmp = letters[l] 
        letters[l] = letters[r]
        letters[r] = tmp 
        l+=1 
        r-=1

    # Create new string once vowels have been swapped.
    new_s = ''
    for x in range(len(letters)):
        new_s+=letters[x]

    return new_s

def main():
    """Main Function"""
    s = "IceCreAm"
    output = rev_vowel(s)
    print("The output from the above function:", output)

if __name__ == "__main__":
    main()