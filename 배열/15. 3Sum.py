'''
Title : 15. 3Sum.py
Date : 23.01.21
Description
    - 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
Input / Output
    Input) nums = [-1, 0, 1, 2, -1, -4]
    Output)
        [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
'''
#1. 브루트 포스로 계산
def threeSum1(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            for z in range(j+1, len(nums)):
                if z > j+1 and nums[z] == nums[z-1]:
                    continue
                if nums[i] + nums[j] + nums[z] == 0:
                    result.append([nums[i], nums[j], nums[z]])
    return result # 시간이 너무 소모되어 결국엔 TIMEOUT

#2. 투 포인터로 계산
def threeSum2(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복 제거
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums) -1
        while (left < right) :
            if nums[i] + nums[left] + nums[right] < 0:
                left += 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while (left < right) and (nums[left] == nums[left+1]):
                    left += 1
                while (left < right) and (nums[right] == nums[right-1]):
                    right -= 1
                left += 1
                right -= 1
    return result

#Debug
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum1(nums))
    print(threeSum2(nums))