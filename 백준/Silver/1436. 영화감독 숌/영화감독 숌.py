from sys import stdin
def solution () :
    n = int(input())
    num = 666
    count = 0
    
    while 1 :
        if str(666) in str(num) :
            count += 1
        if count == n :
            break
        num += 1
    print(num)
solution()
