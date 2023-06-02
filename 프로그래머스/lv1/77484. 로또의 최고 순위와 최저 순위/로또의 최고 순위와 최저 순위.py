def solution(lottos, win_nums):
    zero = 0
    equ = 0
    for l in lottos :
        zero += 1 if l == 0 else 0
        equ += 1 if l in win_nums else 0
        
    answer = [0, 0]
    answer[0] = 7 - (equ + zero) if (equ + zero) != 0 else 6
    answer[1] = 7 - equ if equ != 0 else 6
    
    return answer