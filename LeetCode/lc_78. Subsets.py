class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # my code
        def dfs(elements, start):

            result.append(elements[:])

            for i in range(start, len(nums)):
                elements.append(nums[i])
                dfs(elements, i + 1)
                elements.pop()

        result = []
        dfs([], 0)
        return result

        # book's code
        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)

            # 경로 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        result = []
        dfs(0, [])
        return result