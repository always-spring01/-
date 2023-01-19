'''
Title : 819. Most Common Word.py
Date : 23.01.20
Description
    - 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
    - 대소문자 구분은 하지 않으며, 구두점 또한 무시한다
Input / Output
    Input)
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
    Output) "ball"
'''
import collections
import re


#1. 리스트 컴프리헨션, Counter 객체 사용
def mostCommonWords1(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r"[^\w]", ' ', paragraph)
             .lower().split() if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

#2. Counter 객체 없이
def mostCommonWords2(paragraph : str, banned: list[str]) -> str:
    words = [word for word in re.sub(r"[^\w]", " ", paragraph)
             .lower().split() if word not in banned]

    word_dict = {}
    for word in words:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    # 딕셔너리 자료형에서 Values값 최대인 Key 찾기
    return [k for k,v in word_dict.items() if max(word_dict.values())== v]

#Debug
if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWords1(paragraph, banned))
    print(mostCommonWords2(paragraph, banned))