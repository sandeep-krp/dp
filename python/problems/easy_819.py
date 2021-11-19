"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the 
stock at 5 dollars and sell it at 10 dollars.
"""

# Start at the first element -> calculate the distance to each of elements on the right side
def solve_819(prices):
    min_maxs = find_local_min_and_maxs(prices)
    return solve(min_maxs)

def solve(arr):
    arr_len = len(arr)
    max_profit = 0
    lowest_hit = arr[0]
    for x in range(arr_len):
        if arr[x] > lowest_hit:
            continue
        for y in range(x+1,arr_len):
            if arr[y] - arr[x] > max_profit:
                max_profit = arr[y] - arr[x]
                if arr[x] < lowest_hit:
                    lowest_hit = arr[x]
    return max_profit
# Find only the peaks and lows. Ignore the inbetween
def find_local_min_and_maxs(prices):

    result = [prices[0]]
    if not prices:
        return result
    for x in range(1,len(prices)-1):
        #print("Running for index:{} and value {}".format(x,prices[x]))
        if (prices[x] >= prices[x+1] and prices[x] >= prices[x-1] and prices[x] != prices[x-1]) or (prices[x] <= prices[x+1] and prices[x] <= prices[x-1] and prices[x] != prices[x-1]):
            result.append(prices[x])
    result.append(prices[len(prices)-1])
    return (result)