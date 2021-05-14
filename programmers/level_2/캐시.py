from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    time = 0
    for city in [city.lower() for city in cities]:
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        elif len(cache) < cacheSize:
            cache.append(city)
            time += 5
        elif cache:
            cache.popleft()
            cache.append(city)
            time += 5
        else:
            time += 5
    return time

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time