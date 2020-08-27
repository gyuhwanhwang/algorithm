nums = []
i = str(input())
while(i != str(0)):
    nums.append(i)
    i = str(input())

for num in nums:
    if num == num[::-1]:
        print('yes')
    else:
        print('no')