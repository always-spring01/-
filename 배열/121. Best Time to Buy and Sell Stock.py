'''
Title : 121. Best Time to Buy and Sell Stock.py
Date : 23.01.21
Description
    - 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
Input / Output
    Input) [7,1,4,3,6,4]
    Output) 5
'''
import sys


#1. 브루드 포스 기법으로 풀이
def maxProfit1(nums: list[int]) -> int:
    max_price = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            max_price = max(max_price, nums[j] - nums[i])
    return max_price # TIMEOUT

#2. 계속 갱신하는 방법으로 풀이
def maxProfit2(nums: list[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in nums:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit

#Debug
if __name__ == "__main__":
    prices = [7,1,4,3,6,4]
    print(maxProfit1(prices))
    print(maxProfit2(prices))