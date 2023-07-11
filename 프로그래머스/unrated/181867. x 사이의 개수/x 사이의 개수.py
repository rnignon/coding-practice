def solution(myString):
    answer = []
    os = myString.split('x')
    answer = [len(i) for i in os]
    return answer