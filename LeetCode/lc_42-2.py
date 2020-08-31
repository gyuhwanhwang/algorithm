from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) -1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), \
                                  max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else :
                volume += right_max - height[right]
                right -= 1
        return volume
        """

        volume = 0
        stack = []
        for i in range(len(height)):
            # 변곡점을 만나는 경우  ( stack이 존재하고, 이전 값보다 높아야함 )
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):  # 뒤에가 비어있으면 안된다
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] -1 # 왼쪽 기둥
                # 왼쪽, 오른쪽 기둥 중에 낮은거에서 이전 높이 뺌
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume


sol = Solution()
sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])