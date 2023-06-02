def solution(numbers, hand):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left = '*'
    right = '#'
    answer = ''
    for n in numbers :
        if n in [1, 4, 7] :
            answer += 'L'
            print (answer)
            left = n
        elif n in [3, 6, 9] :
            answer += 'R'
            right = n
        else :
            for k in keypad :
                for l in k :
                    if l == n :
                        location = [keypad.index(k), k.index(l)]
                    if l == left :
                        location_l = [keypad.index(k), k.index(l)]
                    if l == right :
                        location_r = [keypad.index(k), k.index(l)]

            gap_l = sum([abs(a - b) for a, b in zip (location_l, location)])
            gap_r = sum([abs(a - b) for a, b in zip (location_r, location)])

            if gap_l < gap_r :
                answer += 'L'
                left = n
            elif gap_r < gap_l :
                answer += 'R'
                right = n
            else :
                if hand == 'left' :
                    answer += 'L'
                    left = n
                else :
                    answer += 'R'
                    right = n
                    
    return answer