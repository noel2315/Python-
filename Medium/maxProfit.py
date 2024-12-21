def maxProfit(prices):
    n = len(prices)
    if n == 0:
        return 0
    
    profit1 = [0] * n
    profit2 = [0] * n
    
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        profit1[i] = max(profit1[i-1], prices[i] - min_price)
    
    max_price = prices[n-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        profit2[i] = max(profit2[i+1], max_price - prices[i] + profit1[i])
    
    return profit2[0]

prices = [3, 2, 6, 5, 0, 3]
print(maxProfit(prices))  
