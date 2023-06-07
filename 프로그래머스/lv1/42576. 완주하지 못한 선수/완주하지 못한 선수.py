def solution(participant, completion):
    participants = {}
    for i in participant :
        if i in participants.keys() :
            participants[i] += 1
        else :
        	participants[i] = 1
    for i in completion :
        participants[i] -= 1
        
    answer = ''
    for i in participants :
        if participants[i] != 0 :
            answer = i
            break
    
    return answer