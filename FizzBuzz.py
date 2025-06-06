"""
Leetcode Q 412 -- FizzBuzz

A nice intro to using modulation to ID if a number is divisible by another.

Time Complexity == O(n)
"""

def fizzBuzz(n): 
    ans = [] 

    for i in range(1,n+1):
        if (i % 3 == 0) and (i % 5 == 0): 
            ans.append("FizzBuzz") 

        elif i % 3 == 0: 
            ans.append("Fizz") 
            # % modulo returns 0 if the dividend can be divided by the divisor 

        elif i % 5 == 0: 
            ans.append("Buzz") 

        else: 
            ans.append(i)
        
    return ans 


def main():
    """Main Function"""

    n = 5
    print("The output list is as follows")

    output = fizzBuzz(n)
    for x in output: 
        print(x, ' ') 


if __name__ == '__main__':
    main()