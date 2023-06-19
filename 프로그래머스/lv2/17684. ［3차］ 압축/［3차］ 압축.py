def solution(msg):
    dictionary = [chr(i) for i in range (65, 91)]
    msg_list = list(msg)
    tmp = []
    answer = []
    
    partition = 1
    while msg_list :
        msg_token = msg_list[:partition]
        tmp.append(''.join(msg_token))
        if ''.join(msg_token) in dictionary :
            partition += 1
            if len(msg_list) == len(msg_token) :
                answer.append(dictionary.index(tmp[-1]) + 1)
                break
        else :
            dictionary.append(''.join(msg_token))
            answer.append(dictionary.index(tmp[-2]) + 1)
            msg_list = msg_list[partition-1:]
            partition = 1
    return answer