def solution(s):
    answer = [0, 0]
    cnt = 0
    st = s
    while st != '1' :
        count = st.count('1')
        answer[1] += st.count('0')
        cnt += 1
        st = bin(count)[2:]
    answer[0] = cnt 
    return answer