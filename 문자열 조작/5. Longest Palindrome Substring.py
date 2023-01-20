'''
Title : 5. Longest Palindrome Substring.py
Date : 23.01.20
Description
    - 가장 긴 팰린드롬 부분 문자열을 출력하라
Input / Output
    Input) "babad"
    Output) "bab"
'''

#1. 중앙을 중심으로 확장하는 풀이
def longestPalindrome1(s: str) -> str:
    #팰린드롬 판별 및 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) -1) :
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result

#Debug
if __name__ == "__main__":
    strs = "babad"
    print(longestPalindrome1(strs))