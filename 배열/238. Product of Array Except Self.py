'''
Title : 238. Product of Array Except Self.py
Date : 23.01.21
Description
    - 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
Input / Output
    Input) [1,2,3,4]
    Output) [24,12,8,6]
'''

#1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
def productExceptSelf1(nums: list[int]) -> list[int]:
    out = []
    p = 1
    #왼쪽 먼저 곱셈
    for i in nums:
        out.append(p)
        p = p * i

    p = 1
    #왼쪽 값에 오른쪽 값을 곱해서 결과 구하기
    for i in range(len(nums)-1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out

#Debug
if __name__ == "__main__":
    nums = [1,2,3,4]
    print(productExceptSelf1(nums))