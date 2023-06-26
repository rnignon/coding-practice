def solution(a, b, c, d):
    num = [a, b, c, d]
    count = [num.count(i) for i in num]
    if max(count) == 4 :
        return 1111 * a
    elif max(count) == 3 :
        answer = 10
        answer *= num[count.index(3)]
        answer += num[count.index(1)]
        return answer ** 2
    elif max(count) == 2 :
        if min(count) == 2 :
            p = num[count.index(max(count))]
            q = num[count.index(min(count))]
            return (a + b) * abs(a - b) if a != b else (a + c) * abs(a - c)
        else :
            p = num[count.index(max(count))]
            return (a * b * c * d) / (p ** 2)
    else :
        return min(num)