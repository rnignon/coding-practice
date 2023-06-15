def solution(ingredient):
    count = 0
    answer = [1, 2, 3, 1]
    ing_list = []
    for ing in ingredient :
        ing_list.append(ing)
        if (ing_list[-4:] == answer) :
            count += 1
            for i in range(4) :
                ing_list.pop()
    return count