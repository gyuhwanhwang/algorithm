class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # second
        answer = [0] * len(T)
        stack = []

        for i, cur in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer

        # first me
        stack = []
        answer = [0] * len(T)

        for i, temper in enumerate(T):
            # 스택에 기온이 남아있고 오늘 날씨가 이전날씨보다 높을때
            while stack and temper > stack[-1][1]:
                # 스택에 기론된 날에 현재 날짜 - 기록된 날짜
                answer[stack[-1][0]] = i - stack[-1][0]
                stack.pop()

            stack.append([i, temper])

        return answer