import re
from itertools import permutations

def solution(user_id, banned_id):
    banned_user = [id.replace('*', '.') for id in banned_id]
    banned_list = []
    
    for i in permutations (user_id, len(banned_id)) :
        check = True
        for j in range(len(i)) :
            if not (re.match(banned_user[j], i[j])
                    and len(banned_user[j]) == len(i[j])) :
                check = False
                break;
        if check and set(i) not in banned_list :
            banned_list.append(set(i))
    return len(banned_list)