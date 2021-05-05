def solution(s):
    string = ""
    count = 1
    min_len = len(s)
    for cut in range(1, len(s)//2 + 1):
        for i in range(0, len(s) - cut, cut):
            # s[0:2] == s[2:4] ...
            if s[i : i+cut] == s[i+cut : i+ 2*cut]:
                count += 1
            else:
                string += str(count) + s[i : i+cut] if count > 1 else s[i : i+cut]
                count = 1
            if i >= len(s) - 2*cut: # 마지막 비교일때 남은것 다 털어넣기
                string += str(count) + s[i+cut : i+ 2*cut] if count > 1 else s[i+cut : i+ 2*cut]
                count = 1
        min_len = min(min_len, len(string))
        string = ""
    return min_len