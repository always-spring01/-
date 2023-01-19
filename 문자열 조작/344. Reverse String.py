'''
Title : 344. Reverse String.py
Date : 23.01.20
Description
    - 주어진 문자열을 뒤집는 함수를 만들어라
    - 입력값은 문자 배열이며, 리턴 값 없이 주어진 리스트 내부를 수정해야 한다
Input / Output
    Input) ['H', 'e', 'l', 'l', 'o']
    Output) ['o', 'l', 'l', 'e', 'H']
'''

#1. 투 포인터를 이용한 스왑
def reverseString1(s: list[str]) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1; right -= 1

#2. 파이썬다운 방식
def reverseString2(s: list[str]) -> None:
    s.reverse()
    #s[::-1]

#Debug
if __name__ == "__main__":
    test = ['H', "e", 'l', 'l', 'o']
    reverseString2(test)
    print(test)