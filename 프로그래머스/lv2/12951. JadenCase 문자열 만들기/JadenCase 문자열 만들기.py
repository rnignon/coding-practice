def solution(s):
    s_list = s.split(' ')
    print(s_list)
    for i in range(len(s_list)) :
        if s_list[i] == '' :
            continue
        s_list[i] = s_list[i][0].upper() + s_list[i][1:].lower()
    return ' '.join(s_list)