def solution(numbers, target):
    answer = []

    def dfs(index, sum):
        if index == len(numbers) and sum == target:
            answer.append(True)
            return

        if index < len(numbers):
            dfs(index + 1, sum + numbers[index])
            dfs(index + 1, sum - numbers[index])

    dfs(0, 0)
    return sum(answer)

def solution(numbers, target):
		num_list = [(x, -x) for x in numbers]
		return list(map(sum, product(*num_list))).count(target)