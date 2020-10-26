import re
def solution(n, arr1, arr2):
    arr1 = [int(format(x, 'b')) for x in arr1]
    arr2 = [int(format(x, 'b')) for x in arr2]
    arr1 = [str(x + y) for x, y in zip(arr1, arr2)]
    for i in range(len(arr1)):
        arr1[i] = arr1[i].rjust(n, '0')
        # while len(arr1[i]) < n:
        #     arr1[i] = '0' + arr1[i]
        arr1[i] = re.sub('(1|2)', '#', arr1[i])
        arr1[i] = re.sub('0', ' ', arr1[i])
    return arr1