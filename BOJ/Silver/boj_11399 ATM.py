length = int(input())
wait = sorted(list(map(int, input().split())))

print(sum([sum(wait[:i+1]) for i in range(length)]))
