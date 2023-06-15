def solution(today, terms, privacies):
    answer = []
    kind = {}
    today_sum = 0
    
    tmp = today.split('.')
    today_sum += (int(tmp[0]) - 2000) * 12 * 28
    today_sum += (int(tmp[1])) * 28
    today_sum += (int(tmp[2]))
    
    for t in terms :
        kind[t.split()[0]] = int(t.split()[1]) * 28
    
    for p in range(len(privacies)) :
        k = kind[privacies[p][-1]]
        tmp = ''.join(privacies[p].split()[:-1]).split('.')
        day_sum = 0
        day_sum += (int(tmp[0]) - 2000) * 12 * 28
        day_sum += (int(tmp[1])) * 28 
        day_sum += (int(tmp[2]))
        if today_sum - k >= day_sum :
            answer.append(p + 1)
        
    return answer