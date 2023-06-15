from itertools import product
def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    result = {}
    for c in product(discount, repeat = len(emoticons)) :
        result[c] = [0] * 2
        for user in users :
            pay = 0
            for e in range(len(emoticons)) :
                if c[e] >= user[0] :
                    pay += int(emoticons[e] - (emoticons[e] * (c[e] / 100)))
            if pay >= user[1] :
                result[c][0] += 1
            else :
                result[c][1] += pay
    answer = sorted(result.values(), key=lambda x:(x[0], x[1]))
    return answer[-1]