def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {1:0, 2:0, 3:0}
    for i in range(len(answers)) :
        if answers[i] == a[i%len(a)] :
            count[1] += 1
        if answers[i] == b[i%len(b)] :
            count[2] += 1
        if answers[i] == c[i%len(c)] :
            count[3] += 1
    answer = []
    max_v = sorted(count.items(), key=lambda x:x[1], reverse=True)[0][1]
    for i in count :
        if count[i] == max_v :
            answer.append(i)
    return answer