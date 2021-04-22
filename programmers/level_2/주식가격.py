def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for index, price in enumerate(prices):
        # print("index:", index, "stack:", stack)
        if not stack:
            stack.append((index, price))
            continue
        # current price is lower than prev
        while stack and price < stack[-1][1]:
            prev_index = stack.pop()[0]
            answer[prev_index] = index - prev_index
        stack.append((index, price))
    while stack:
        index = stack.pop()[0]
        answer[index] = len(prices) - 1 - index
    return answer