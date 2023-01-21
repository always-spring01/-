'''
Title : 1. Two Sum.py
Date : 23.01.21
Description
    - 덧샘하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
Input / Output
    Input) nums = [2, 7, 11, 15], target = 9
    Output) [0, 1] (2 + 7 = 9)
'''

#1. 브루드 포스 방식 이용
def twoSum1(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

#2. in을 이용한 탐색
def twoSum2(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums): # enumberate : 열거형 자료형, (index, value) 형식의 튜플로 반환한다
        complement = target - n
        if complement in nums[i+1:]:
            return [i, nums[i+1:].index(complement) + (i+1)]

#3. 첫 번째 수를 뺀 결과 키 조회
def twoSum3(nums: list[int], target: int) -> list[int]:
    nums_dic = {}
    for i, n in enumerate(nums):
        nums_dic[n] = i

    for i, n in enumerate(nums):
        if target - n in nums_dic and i != nums_dic[target - n]:
            return [i, nums_dic[target - n]]

#Debug
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum1(nums, target))
    print(twoSum2(nums, target))
    print(twoSum3(nums, target))
