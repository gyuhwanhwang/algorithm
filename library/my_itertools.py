import itertools

count = 0
for i in itertools.count(10, 2):
    print(i, end=" ")
    if i == 20: break
print()

count = 0
for i in itertools.cycle("10ABC"):
    print(i, end=" ")
    count += 1
    if count == 10: break
print()

count = 0
nums = [1, 3, 5, 7, 9]
for i in itertools.cycle(nums):
    print(i, end=" ")
    count += 1
    if count == 10: break
print()

for i in itertools.repeat(10, 3):
    print(i, end=" ")
print()

for i in itertools.accumulate("ABCD", lambda x, y: x+y):
    print(i, end=" ")
print()

for i in itertools.accumulate([1, 2, 3, 4, 5]):
    print(i, end=" ")
print()

for i in itertools.chain("ABC", "DEF"):
    print(i, end=" ")
print()

for i in itertools.chain.from_iterable([[1, 3], [5, 7], [9, 11]]):
    print(i, end=" ")
print()

for i in itertools.compress("012345", [1, 0, 1, 0, 1]):
    print(i, end=" ")
print()

print(list(itertools.product('ABCD', repeat=2)))
print(list(itertools.permutations('ABCD', 2)))
print(list(itertools.combinations('ABCD', 2)))
print(list(itertools.combinations_with_replacement('ABCD', 2)))
