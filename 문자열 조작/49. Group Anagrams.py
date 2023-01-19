'''
Title : 49. Group Anagrams.py
Date : 23.01.20
Description
    - 문자열 배열을 받아 에너그램 단위로 그룹핑하라
    - 애너그램 ? 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 의미한다
Input / Output
    Input) ["eat", "tea", "ate", "tan", "nat", "bat"]
    Output)
        [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ]
'''

#1. 정렬하여 딕셔너리에 추가하는 방법
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    for s in strs:
        if ''.join(sorted(s)) in anagrams.keys():
            anagrams[''.join(sorted(s))].append(s)
        else:
            anagrams[''.join(sorted(s))] = [s]
    return list(anagrams.values())

#Debug
if __name__ == "__main__":
    strs = ["eat", "tea", "ate", "tan", "nat", "bat"]
    print(groupAnagrams(strs))