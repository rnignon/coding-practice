import re
def solution(str1, str2):
    arr1 = [str1.lower()[i:i+2] for i in range(0, len(str1))]
    arr2 = [str2.lower()[i:i+2] for i in range(0, len(str2))]
    arr1 = list(filter(lambda x : re.search('[a-zA-Z]{2,}', x), arr1))
    arr2 = list(filter(lambda x : re.search('[a-zA-Z]{2,}', x), arr2))
    
    inter = set(arr1) & set(arr2)
    union = set(arr1) | set(arr2)
    
    sum_inter = sum(min(arr1.count(i), arr2.count(i)) for i in inter)
    sum_union = sum(max(arr1.count(i), arr2.count(i)) for i in union)
    
    answer = 1 if sum_union == 0 else sum_inter / sum_union 
    return int(answer * 65536)