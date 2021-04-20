def solution(citations):
    citations.sort()
    if citations[0] > len(citations):
        return len(citations)

    max = 0
    # h = 0 to len(citations)
    for h in range(len(citations) + 1):
        # find the index 0f (num >= h)
        bigger_point = -1
        for num in citations:
            if num >= h:
                bigger_point = citations.index(num)
                break
        if bigger_point != -1 and len(citations[bigger_point:]) >= h:
            max = h
        else:
            return max

# others
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer