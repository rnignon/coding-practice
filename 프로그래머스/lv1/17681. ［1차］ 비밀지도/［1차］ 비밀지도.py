def solution(n, arr1, arr2):
    
    answer = []
    for i, j in zip(arr1, arr2) :
        arr = str(bin(i|j))[2:]
        arr = arr.rjust(n, '0')
        arr = arr.replace('0', ' ')
        arr = arr.replace('1', '#')
        answer.append(arr)
        
    return answer