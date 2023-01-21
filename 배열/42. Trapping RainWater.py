'''
Title : 42, Trapping RainWater
Date : 23.01.21
Description
    - 높이를 입력받아 비가 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라
Input / Output
    Input) [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    Output) 6
'''

#1. 투포인터를 이용한 풀이
def trap1(height: list[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume

#Debug
if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap1(height))