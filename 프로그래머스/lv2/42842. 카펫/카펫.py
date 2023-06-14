def solution(brown, yellow):
    a = 0
    answer = []
    if (yellow == 1) :
        answer.append((brown + yellow) ** 0.5)
        answer.append((brown + yellow) ** 0.5)
    else :
        for i in range(2, yellow + 1) :
            if yellow % i == 0 :
                j = yellow // i
                if (brown + yellow) % (j + 2) == 0:
                    a = (brown + yellow) // (j + 2)
                    break
        answer.append(a)
        answer.append((brown + yellow) // a)
    return sorted(answer, reverse = True)