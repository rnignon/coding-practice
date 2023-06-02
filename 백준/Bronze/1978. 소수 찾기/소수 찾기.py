def solution () :
    n = int(input())
    n_input = input().split()
    nums = [int(i) for i in n_input]
    count = 0
    for num in nums :
        count += prime(num)
    print(count)

def prime (num) :
    if num == 1 : return 0
    for i in range (2, int(num ** 0.5 + 1)) :
        if num % i == 0 :
            return 0
    return 1

solution()

