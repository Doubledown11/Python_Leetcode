"""
Leetcode Q 121 -- Best Time to Buy and Sell a Stock.

Simplified Time Complexity:
O(n)

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104
"""

def maxProfit(prices): 
    # Check Constraint 1:
    if len(prices) < 1 or len(prices) > 105:
        print('Invalid input!')
        exit()

    # Init min_price to a random very high value ie) infinity.
    min_price = float('inf') 
    
    # Init max profit to 0.
    max_profit = 0 
    
    # Iterate through the prices list, and check to find a price with a lower value than the current minimum price. 
    for price in prices: 
        # Check Constraint 2:
        if price < 0 or price > 104:
            print("Invalid input!")
            exit()

        if price < min_price: 
            # Update min price if current price is lower.
            min_price = price 
        
        # Calc profit if selling today -- Take current price and subtract the minimum price from it!
        profit = price - min_price 

        if profit > max_profit: 
            max_profit = profit # Update max_profit if current price is greater than it.
        
    return max_profit

def main():
    """Main Function"""

    prices = [7,6,4,3,1]
    output = maxProfit(prices)
    print("The output from the above function is:", output)

    
if __name__ == "__main__":
    main()

