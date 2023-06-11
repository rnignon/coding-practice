def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x : (x * 4)[:4], reverse = True)
    answer = ''.join(numbers)
    return "0" if int(answer) == 0 else answer 