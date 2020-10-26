def solution(arr):
    answer = []
    for item in arr:
        if not answer or answer[-1] != item:
            answer.append(item)
    return answer