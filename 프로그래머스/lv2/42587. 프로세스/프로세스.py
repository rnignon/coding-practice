def solution (priorities, location) :
    count = 0 
    index = location
    while 1 :
        max_v = max(priorities)
        pop = priorities.pop(0)
        index -= 1
        if (max_v == pop) :
            count += 1
            if index < 0 : break
        else :
            priorities.append(pop)
            if index < 0 :
                index = len(priorities) - 1
    return count