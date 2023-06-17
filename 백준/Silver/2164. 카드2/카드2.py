from collections import deque
def solution() :
    n = int(input())
    cards = deque([i + 1 for i in range(n)])

    while len(cards) > 1 :
        cards.popleft()
        card = cards.popleft()
        cards.append(card)

    print(cards.popleft())
solution()
