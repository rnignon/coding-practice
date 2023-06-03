def solution(board, moves):
    stack = []
    for move in moves :
        for b in board :
            if b[move-1] != 0 :
                stack.append(b[move-1])
                b[move-1] = 0
                break
    pointer = 0
    counter = 0
    while 1 :
        if pointer + 1 >= len(stack) : break
        if stack[pointer] == stack[pointer + 1] :
            del stack[pointer : pointer + 2]
            pointer = 0 if pointer == 0 else pointer - 1
            counter += 1
        else : pointer += 1
    return counter * 2