'''
Title : 561. Array Partition I.py
Date : 23.01.21
Description
    - n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
Input / Output
    Input) [1,4,3,2]
    Output) 4
'''

#1. 오름차순 계산
def arrayPairSum1(nums: list[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum

#2. 짝수 번째 값 계산 + 가장 파이썬 다운 방식으로 해결
def arrayPairSum2(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])

#Debug
if __name__ == "__main__":
    nums = [1,4,3,2]
    print(arrayPairSum1(nums))
    print(arrayPairSum2(nums))