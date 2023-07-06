def solution(binomial):
    token = binomial.split()
    a = int(token[0])
    b = int(token[2])
    answer = a + b if token[1] == '+' else (a - b if token[1] == '-' else a * b) 
    return answer