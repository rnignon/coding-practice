def solution(arr, query):
    arr_q = arr
    for q in range (len(query)) :
        if q % 2 == 0 :
            arr_q = arr_q[:query[q] + 1]
        else :
            arr_q = arr_q[query[q]:]
    return arr_q