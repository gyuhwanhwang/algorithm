from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 1 투 포인터를 최대로 이동
        """
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), \
                                  max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
        """

        # 2 스택 쌓기
        stack = []
        volume = 0

        for i in range(len(height)):
            print(f'i는 {i}입니다', end=' ')
            print(f'현재 스택 {stack}', end=' ')
            # 변곡점을 만나는 경우( 스택이 존재하고, 현재가 이전보다 높음)
            while stack and height[i] > height[stack[-1]]:
                print('조건 충족')
                # 스택에서 꺼낸다
                top = stack.pop() # 바로 전 높이
                print(f'top은 {top}입니다')

                if not len(stack):  # 첫번째 빈거 방지
                    print('break합니다')
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
                print(f'distance는 {distance}, waters는 {waters}, volume은 {volume}')
            stack.append(i)
            print('')
        return volume



sol = Solution()
sol.trap([0,1,0,2,1,0,1,3,2,1,2,1,4])