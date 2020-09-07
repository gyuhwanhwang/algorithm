from itertools import permutations

items = 'ABCD'
items.split()

items = list(map(''.join, permutations(items))) # items의 모든 원소를 가지고 순열을 만든다.
# print(list(map(''.join, permutations(items, 2)))) # 2개의 원소를 가지고 순열을 만든다

for item in items:
    print(item)
