from itertools import product
def solution(word):
    dic = []
    words = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6) :
        for j in product(words, repeat=i):
            dic.append(''.join(j))
    dic = sorted(set(dic))
    return dic.index(word) + 1
