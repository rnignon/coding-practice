import re
def solution(files):
    tokens = []
    for f in files :
        token = []
        token.append(re.findall('^\D+', f)[0])
        token.append(re.findall('\d+', f)[0])
        token.append(re.sub('^\D+\d+', '', f))
        tokens.append(token)

    tokens_r = sorted(tokens, key=lambda x:(x[0].upper(), int(x[1])))
    answer = [''.join(token) for token in tokens_r]
    return answer