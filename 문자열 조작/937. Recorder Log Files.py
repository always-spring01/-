'''
Title : 937. Recorder Log Files.py
Date : 23.01.20
Description
    - 주어진 로그 파일을 재정렬 하라
    - 로그의 가장 앞 부분은 식별자이다
    - 문자로 구성된 로그가 숫자로 구성된 로그보다 앞에 온다
    - 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다
    - 숫자 로그는 입력 순서를 유지한다
Input / Output
    Input) log = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig"]
    Output) ["let1 art can", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
'''

#1. 람다와 + 연산자를 이용
def recorderLogFiles1(logs: list[str]) -> list[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # TODO : Lambda 사용법에 대해 추가 공부 필요
    # 2개의 키를 람다 표현식으로 정렬
    # x.split()[1:]을 1번째 key, 이게 동일하다면 x.split()[0]을 2번째 key로 설정해서 정렬한다
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

#Debug
if __name__ == "__main__":
    log = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig"]
    print(recorderLogFiles1(log))