def solution(phone_book):
    phone_book.sort(key=lambda x: (x, len(x)))
    for i, j in zip(phone_book[:-1], phone_book[1:]) :
        if j.startswith(i) :
            return False
    return True