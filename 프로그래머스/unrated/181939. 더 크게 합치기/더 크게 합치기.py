def solution(a, b):
    c = int(str(a) + str(b))
    d = int(str(b) + str(a))
    return c if c > d else d