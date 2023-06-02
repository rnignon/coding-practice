import re
def solution(dartResult):
    scores = []
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    dartReg = re.compile('[0-9]+[SDT][*#]?')
    tokens = re.findall(dartReg, dartResult)
    for token in tokens :
        score = int(re.sub('\D', '', token)) ** bonus[re.sub('[^SDT]', '', token)]
        if token[-1] == '*' :
            score *= 2
            if scores : scores[-1] *= 2
        elif token[-1] == '#' :
            score *= -1
        scores.append(score)
    return sum(score for score in scores)