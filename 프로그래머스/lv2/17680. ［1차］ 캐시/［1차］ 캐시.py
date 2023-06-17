from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    if cacheSize == 0 :
        return 5 * len(cities)
    for city in cities :
        city = city.lower()
        if city not in cache :
            if cache and len(cache) >= cacheSize :
                cache.popleft()
            cache.append(city)
            answer += 5
        else :
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer