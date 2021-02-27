class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                result.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        prev_elements = []
        result = []

        dfs(nums)
        return result
