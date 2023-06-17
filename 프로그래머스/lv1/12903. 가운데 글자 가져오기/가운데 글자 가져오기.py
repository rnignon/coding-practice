def solution(s):
    answer = ''
    center = len(s) // 2
    return s[center] if len(s) % 2 != 0 else s[center - 1:center + 1]