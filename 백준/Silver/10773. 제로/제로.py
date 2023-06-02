stack = []
for i in range(int(input())) :
    num = input()
    if num == '0' :
        stack.pop()
    else :
        stack.append(int(num))
print(sum(i for i in stack))
