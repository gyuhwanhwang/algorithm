import re
def solution(files):
    files.sort(key=lambda x: (re.findall('[a-zA-Z.\- ]+', x)[0].lower(), int(re.findall('[0-9]+', x)[0])))
    return files

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["ba af3.png", "cd-ef10.png", "aa.a02.png", "aab1.png", "a-z01.GIF", "A2.JPG"])