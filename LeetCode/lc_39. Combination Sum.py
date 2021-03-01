class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ## my code
        result = []

        def dfs(elements=[], start=0):
            if sum(elements) > target:
                return
            elif sum(elements) == target:
                result.append(elements[:])

            for i in range(start, len(candidates)):
                elements.append(candidates[i])
                dfs(elements, i)
                elements.pop()

        dfs()
        return result

        ## book's code
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result
