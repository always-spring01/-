'''
Title : 125. Vaild Palindrome.py
Date : 23.01.19
Description
    - 주어진 문자열이 팰린드롬인지 확인하라
    - 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다
    - 팰린드롬? 앞뒤가 똑같은 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 팰린드롬이라 한다
Input / Output
    Input) "race a Car"
    Output) false

    Input) "A man, a plan, a canal: Panama"
    Output) true
'''
import collections
import re
from typing import Deque


#1. 리스트로 변환
def isPalindrome1(s: str) -> bool:
    strs = [] #숫자+알파벳만 남길 문자열 생성
    for char in s:
        if char.isalnum(): #char이 숫자 혹은 알파벳일 경우에 True 리턴
            strs.append(char.lower())

    while len(strs) > 1: #0번째를 pop하고, pop()은 index 마지막을 pop한다
        if strs.pop(0) != strs.pop() :
            return False
    return True

#2. 데크 자료형을 이용한 최적화
def isPalindrome2(s: str) -> bool:
    #자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

#3. 슬라이싱 사용
def isPalindrome3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s) #정규 표현식으로 소문자,숫자 제외하고 모두 삭제

    return s == s[::-1] #슬라이싱으로 뒤집기

#Debug
if __name__ == "__main__":
    strs = "CACS"
    print(isPalindrome1(strs))
    print(isPalindrome2(strs))
    print(isPalindrome3(strs))