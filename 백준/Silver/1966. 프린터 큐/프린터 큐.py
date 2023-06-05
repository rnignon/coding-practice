def solution () :
    case = int(input())
    for c in range(case) :
        n, index = map(int, input().split())
        queue = list(map(int, input().split()))

        count = 0
        while 1 :
            max_v = max(queue)
            pop = queue.pop(0)
            index -= 1
            if (max_v == pop) :
                count += 1
                if index < 0 : break
            else :
                queue.append(pop)
                if index < 0 : index = len(queue) - 1
        print(count)
        
solution()
