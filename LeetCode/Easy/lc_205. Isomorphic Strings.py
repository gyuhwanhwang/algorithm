from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = defaultdict(str)
        for i in range(len(s)):
            # 처음 변환하는 단어
            if not table[s[i]]:
                # 그런데 값이 이미 다른 키와 매핑되있으면 중복
                if t[i] in table.values():
                    return False
                table[s[i]] = t[i]
            # 변환한 단어일 경우 변환 값이 맞는지 확인
            elif table[s[i]] != t[i]:
                return False
        return True