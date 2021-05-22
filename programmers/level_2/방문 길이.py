def solution(dirs):
    d = { 'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0] }
    visited = set()
    x, y = 0, 0
    for dir in dirs:
        nx = x + d[dir][0]
        ny = y + d[dir][1]
        if not (-5 <= nx <= 5) or not (-5 <= ny <= 5):
            continue
        visited.add((max(x,nx), min(x, nx), max(y, ny), min(y,ny)))
        x, y = nx, ny
    return len(visited)