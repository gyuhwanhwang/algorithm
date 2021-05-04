﻿def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    last_camera = -30001  # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer