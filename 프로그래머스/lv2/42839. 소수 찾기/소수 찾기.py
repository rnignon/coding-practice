from itertools import permutations
def solution(numbers):
    token = [num for num in numbers]
    prime = []
    for i in range(1, len(numbers) + 1) :
        for j in permutations(token, i) :
            p = int(''.join(j))
            if isprime(p) :
                prime.append(p)
    return len(set(prime))

def isprime(num) :
    if num < 2 :
        return False
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True