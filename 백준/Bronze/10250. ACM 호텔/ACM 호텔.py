def solution():
    case = int(input())
    for i in range (case) :
        h, w, n = map(int, input().split())
        answer = str(h) if n % h == 0 else str(n % h)
        answer += str(n // h).zfill(2) if n % h == 0 else str(n // h + 1).zfill(2)
        print(answer)
    
solution()
