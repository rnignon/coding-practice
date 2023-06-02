def solution(survey, choices):
    scores = {'RT' : 0, 'CF' : 0, 'JM' : 0, 'AN' : 0}
    for s, c in zip(survey, choices) :
        if 'R' in s :
            if s[0] == 'R' :
                scores['RT'] += -c + 4
            else :
                scores['RT'] += c - 4
        elif 'C' in s :
            if s[0] == 'C' :
                scores['CF'] += -c + 4
            else :
                scores['CF'] += c - 4
        elif 'J' in s :
            if s[0] == 'J' :
                scores['JM'] += -c + 4
            else :
                scores['JM'] += c - 4
        elif 'A' in s :
            if s[0] == 'A' :
                scores['AN'] += -c + 4
            else :
                scores['AN'] += c - 4
    return ''.join(k[0] if scores[k] >= 0 else k[1] for k in scores.keys())